"""Pruebas offline del pipeline: sanitización, boilerplate y deltas."""
import os
import shutil
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src"))

from sanitizer import DetectorBoilerplate, sanitizar
import state_store
from state_store import ManifestStore


AVISO_LEGAL = ("Cisco and the Cisco logo are trademarks or registered trademarks "
               "of Cisco and/or its affiliates in the U.S. and other countries.")

MENU = "".join(f'<a href="/p{i}">Producto {i}</a>' for i in range(12))


def pagina(titulo, cuerpo, n=1):
    return f"""
    <html><body>
      <header><h1>Cisco</h1><a href="/login">Sign in</a></header>
      <nav>{MENU}</nav>
      <div class="sidebar"><ul>{MENU}</ul></div>
      <div id="onetrust-banner-sdk">We use cookies to improve your experience.</div>
      <main>
        <h1>{titulo}</h1>
        <p>{cuerpo}</p>
        <pre>curl -X GET https://webexapis.com/v1/people</pre>
        <table><tr><th>Code</th><th>Meaning</th></tr><tr><td>429</td><td>Rate limited</td></tr></table>
        <p class="notice">{AVISO_LEGAL}</p>
      </main>
      <div class="related-content">{MENU}</div>
      <footer><p>{AVISO_LEGAL}</p><a href="/privacy">Privacy</a></footer>
    </body></html>
    """


def test_sanitizacion_estructural():
    md, _ = sanitizar(pagina("Crear knowledge base",
                             "Una knowledge base almacena documentos indexados para el AI Receptionist."))
    assert "Producto 3" not in md, "El menú de navegación sobrevivió a la poda"
    assert "cookies" not in md.lower(), "El banner de cookies sobrevivió"
    assert "Sign in" not in md, "La cabecera sobrevivió"
    assert "knowledge base" in md.lower(), "Se perdió el contenido real"
    assert "curl -X GET" in md, "Se perdió el bloque de código"
    assert "429" in md, "Se perdió la tabla"
    print("  OK poda estructural + heurística; código y tablas preservados")
    return md


def test_boilerplate_cross_documento():
    detector = DetectorBoilerplate(umbral_frecuencia=0.25, min_documentos=5)

    corpus = [pagina(f"Guía {i}", f"Contenido único y específico del documento número {i}. " * 6)
              for i in range(12)]

    # Fase BOOTSTRAP: observar sin filtrar.
    for html in corpus:
        _, bloques = sanitizar(html)
        detector.observar(bloques)

    fingerprints = detector.consolidar()
    assert len(fingerprints) > 0, "No se detectó ningún bloque de plantilla"
    assert detector.es_boilerplate(AVISO_LEGAL), "El aviso legal no fue marcado como boilerplate"
    assert not detector.es_boilerplate("Contenido único y específico del documento número 3."), \
        "Se marcó contenido único como boilerplate (falso positivo)"

    # Fase INCREMENTAL: filtrar.
    md_filtrado, _ = sanitizar(corpus[0], detector=detector)
    assert "trademarks or registered trademarks" not in md_filtrado, \
        "El aviso legal sobrevivió al filtro de boilerplate"
    assert "documento número 0" in md_filtrado, "El filtro eliminó contenido legítimo"
    print(f"  OK boilerplate: {len(fingerprints)} fingerprints, aviso legal eliminado, "
          "contenido único intacto")


def test_deltas_incrementales():
    tmp = tempfile.mkdtemp()
    cwd = os.getcwd()
    os.chdir(tmp)
    try:
        os.makedirs("logs", exist_ok=True)
        url_a = "https://help.webex.com/en-us/article/aaa"
        url_b = "https://help.webex.com/en-us/article/bbb"

        # Ejecución 1: BOOTSTRAP
        m = ManifestStore()
        assert m.modo == ManifestStore.MODO_BOOTSTRAP, "Debería arrancar en bootstrap"
        cambio_a, id_a = m.registrar_contenido(url_a, "Contenido A versión 1")
        cambio_b, id_b = m.registrar_contenido(url_b, "Contenido B versión 1")
        assert cambio_a and cambio_b
        m.escribir_documento(id_a, url_a, "Contenido A versión 1")
        m.escribir_documento(id_b, url_b, "Contenido B versión 1")
        r1 = m.guardar_deltas()
        m.guardar()
        assert len(r1["added"]) == 2 and len(r1["modified"]) == 0

        # Ejecución 2: INCREMENTAL, A cambia, B no
        m2 = ManifestStore()
        assert m2.modo == ManifestStore.MODO_INCREMENTAL, "Debería pasar a incremental"
        cambio_a2, _ = m2.registrar_contenido(url_a, "Contenido A versión 2 MODIFICADO")
        cambio_b2, _ = m2.registrar_contenido(url_b, "Contenido B versión 1")
        assert cambio_a2 is True, "No detectó la modificación de A"
        assert cambio_b2 is False, "Reportó cambio falso en B"
        r2 = m2.guardar_deltas()
        assert r2["modified"] == [id_a] and r2["unchanged_count"] == 1

        # TTL adaptativo: B, sin cambios, se revisita más tarde que A
        assert m2.entradas[url_b]["unchanged_runs"] == 1
        assert m2.entradas[url_a]["unchanged_runs"] == 0

        # Ejecución 3: B desaparece -> tombstone
        m3 = ManifestStore()
        m3.registrar_desaparecido(url_b)
        r3 = m3.guardar_deltas()
        assert r3["removed"] == [id_b], "No se emitió tombstone"
        assert not os.path.exists(os.path.join(state_store.DIR_DOCS, f"{id_b}.md")), \
            "El fichero del documento retirado sigue en disco"
        assert m3.debe_visitar(url_b) is False, "Se sigue visitando una URL retirada"

        # Cuarentena por 403: no se reintenta
        m3.registrar_bloqueo("https://developer.webex.com/x", 403)
        assert m3.debe_visitar("https://developer.webex.com/x") is False

        print("  OK deltas: added/modified/unchanged/removed correctos, "
              "tombstone emitido, TTL adaptativo, 403 en cuarentena")
    finally:
        os.chdir(cwd)
        shutil.rmtree(tmp, ignore_errors=True)


def test_backoff_y_clasificacion():
    from fetch_policy import PoliticaAcceso
    p = PoliticaAcceso()
    assert p.tras_respuesta("http://x/1", 200)[0] == "ok"
    assert p.tras_respuesta("http://x/2", 304)[0] == "no_modificado"
    assert p.tras_respuesta("http://x/3", 404)[0] == "desaparecido"
    assert p.tras_respuesta("http://x/4", 403)[0] == "cuarentena"
    assert p.cuarentena.contiene("http://x/4")

    accion, espera = p.tras_respuesta("http://x/5", 429, retry_after="30", intento=0)
    assert accion == "reintentar" and espera == 30.0, "No honró Retry-After"

    accion, _ = p.tras_respuesta("http://x/5", 429, intento=99)
    assert accion == "cuarentena", "Un 429 persistente debería aparcarse"

    # El 403 nunca se reintenta, sea cual sea el intento.
    assert p.backoff.debe_reintentar(0, 403) is False
    print("  OK política: 403->cuarentena sin reintento, 429->backoff con Retry-After, "
          "304->no modificado")


def test_circuit_breaker():
    from fetch_policy import CircuitBreaker
    cb = CircuitBreaker(ventana=20, umbral_error=0.5, minimo_muestras=10)
    for _ in range(5):
        cb.registrar(False)
    assert cb.abierto is False, "Se abrió con muestras insuficientes"
    for _ in range(6):
        cb.registrar(False)
    assert cb.abierto is True, "No se abrió con ratio de error alto"
    print("  OK circuit breaker")


if __name__ == "__main__":
    print("\nsanitizer:")
    md = test_sanitizacion_estructural()
    test_boilerplate_cross_documento()
    print("\nstate_store:")
    test_deltas_incrementales()
    print("\nfetch_policy:")
    test_backoff_y_clasificacion()
    test_circuit_breaker()
    print("\n--- Markdown resultante de ejemplo ---")
    print(md[:600])
    print("\nTODAS LAS PRUEBAS PASARON")
