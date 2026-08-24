"""Prueba el filtrado y el envoltorio de la ingesta de repositorios GitHub,
y la generacion del inventario del RAG."""
import json
import os
import shutil
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))), "src"))

import repos_ingest as ri
import resumen_rag


META = {
    "full_name": "webex/webex-js-sdk",
    "name": "webex-js-sdk",
    "default_branch": "main",
    "description": "JavaScript SDK for Webex",
    "license": {"spdx_id": "MIT"},
}


# ---------------------------------------------------------------------------
# Que ficheros entran
# ---------------------------------------------------------------------------

def test_solo_entra_markdown():
    assert ri._es_ingerible("README.md", 500)
    assert ri._es_ingerible("docs/guia.md", 500)
    assert not ri._es_ingerible("src/index.js", 500)
    assert not ri._es_ingerible("package.json", 500)


def test_gobernanza_del_repo_fuera():
    """CHANGELOG y LICENSE son casi identicos entre repos: como chunk vectorial
    son el mismo boilerplate que el sanitizador persigue en las paginas web."""
    for nombre in ("CHANGELOG.md", "LICENSE.md", "CONTRIBUTING.md",
                   "CODE_OF_CONDUCT.md", "SECURITY.md"):
        assert not ri._es_ingerible(nombre, 500), nombre
        assert not ri._es_ingerible(f"docs/{nombre.lower()}", 500), nombre


def test_directorios_generados_o_de_test_fuera():
    rutas = [
        "node_modules/foo/README.md",
        "packages/x/node_modules/y/README.md",
        "src/test/casos.md",
        "src/__tests__/casos.md",
        "docs/fixtures/ejemplo.md",
        ".github/PULL_REQUEST_TEMPLATE.md",
        "dist/README.md",
    ]
    for r in rutas:
        assert not ri._es_ingerible(r, 500), r


def test_ficheros_enormes_fuera():
    """Un .md de cientos de KB en un repo de codigo suele ser referencia
    autogenerada, no prosa util."""
    assert ri._es_ingerible("docs/api.md", ri.MAX_BYTES_FICHERO)
    assert not ri._es_ingerible("docs/api.md", ri.MAX_BYTES_FICHERO + 1)
    assert not ri._es_ingerible("docs/vacio.md", 0)


def test_readmes_stub_de_monorepo_fuera():
    """webex-js-sdk tiene un README por paquete y muchos son un titulo suelto.
    Son cortos, asi que cualquier consulta que nombre el paquete los puntua
    alto sin que respondan nada."""
    assert not ri._es_ingerible("packages/plugin-foo/README.md", 120)
    assert not ri._es_ingerible("packages/plugin-foo/README.md",
                                ri.MIN_BYTES_FICHERO - 1)
    assert ri._es_ingerible("packages/plugin-foo/README.md",
                            ri.MIN_BYTES_FICHERO)


def test_rutas_con_espacio_se_codifican():
    """webex-js-sdk tiene 'packages/calling/usm sdk flow.md'. Sin codificar,
    urllib lanza InvalidURL y tumba la ingesta del repositorio entero."""
    ruta = "packages/calling/usm sdk flow.md"
    cruda = ri._url_cruda("webex/webex-js-sdk", "next", ruta)
    navegable = ri._url_navegable("webex/webex-js-sdk", "next", ruta)
    assert " " not in cruda and " " not in navegable
    assert "usm%20sdk%20flow.md" in cruda
    # Las barras de la ruta deben sobrevivir: son estructura, no contenido.
    assert "/packages/calling/" in cruda
    assert cruda.startswith("https://raw.githubusercontent.com/")
    assert navegable.startswith("https://github.com/")


def test_slug_estable_y_sin_colisiones():
    a = ri._slug("webex/widgets", "docs/uso.md")
    b = ri._slug("webex/components", "docs/uso.md")
    assert a != b, "dos repos con la misma ruta no pueden compartir doc_id"
    assert a == ri._slug("webex/widgets", "docs/uso.md"), "debe ser estable"
    assert all(c.isalnum() or c == "-" for c in a), a


# ---------------------------------------------------------------------------
# Envoltorio del documento
# ---------------------------------------------------------------------------

def test_documento_lleva_frontmatter_compatible_con_el_corpus():
    """copilot_pack y el consumidor RAG leen source_url y retrieved_at del
    frontmatter: si faltan, estos documentos no se clasifican."""
    doc = ri._documento(META, "docs/uso.md", "Como autenticar el SDK.")
    assert doc.startswith("---\n")
    cabecera = doc.split("---", 2)[1]
    for campo in ("doc_id:", "source_url:", "repo:", "licencia:", "retrieved_at:"):
        assert campo in cabecera, campo
    assert "https://github.com/webex/webex-js-sdk/blob/main/docs/uso.md" in doc
    assert "Como autenticar el SDK." in doc


def test_documento_declara_la_licencia():
    doc = ri._documento(META, "README.md", "texto")
    assert "licencia: MIT" in doc
    sin_licencia = dict(META, license=None)
    assert "licencia: sin declarar" in ri._documento(sin_licencia, "README.md", "t")


# ---------------------------------------------------------------------------
# Cuota de la API
# ---------------------------------------------------------------------------

class _Cabeceras(dict):
    def get(self, k, d=None):
        return dict.get(self, k, d)


def _http_error(codigo, cabeceras=None):
    import urllib.error
    return urllib.error.HTTPError(
        "https://api.github.com/repos/x/y", codigo, "err",
        _Cabeceras(cabeceras or {}), None)


def test_5xx_se_reintenta_y_acaba_pasando():
    """El arbol recursivo de un monorepo devuelve 504 con cierta frecuencia.
    Sin reintento ese repositorio se pierde entero en cada ejecucion y deja un
    hueco permanente que nadie nota."""
    original_open, original_sleep = ri.urllib.request.urlopen, ri.time.sleep
    intentos = {"n": 0}

    class _Resp:
        def read(self): return b'{"ok": true}'
        def __enter__(self): return self
        def __exit__(self, *a): return False

    def _fake(*a, **k):
        intentos["n"] += 1
        if intentos["n"] < 3:
            raise _http_error(504)
        return _Resp()

    try:
        ri.urllib.request.urlopen = _fake
        ri.time.sleep = lambda s: None
        assert ri._get_json("https://api.github.com/repos/x/y") == {"ok": True}
        assert intentos["n"] == 3
    finally:
        ri.urllib.request.urlopen, ri.time.sleep = original_open, original_sleep


def test_4xx_no_se_reintenta():
    """Un 404 o un 401 no se arreglan repitiendo: solo gastan cuota."""
    import urllib.error
    original_open, original_sleep = ri.urllib.request.urlopen, ri.time.sleep
    intentos = {"n": 0}

    def _fake(*a, **k):
        intentos["n"] += 1
        raise _http_error(404)

    try:
        ri.urllib.request.urlopen = _fake
        ri.time.sleep = lambda s: None
        try:
            ri._get_json("https://api.github.com/repos/x/y")
            assert False, "deberia propagar el 404"
        except urllib.error.HTTPError:
            pass
        assert intentos["n"] == 1, f"reintento un 4xx {intentos['n']} veces"
    finally:
        ri.urllib.request.urlopen, ri.time.sleep = original_open, original_sleep


def test_403_por_cuota_se_distingue_de_403_por_permisos():
    """Los dos devuelven 403 pero exigen acciones opuestas: esperar frente a
    revisar el token. Sin distinguirlos, la ingesta parece 'repos que no
    existen' y se diagnostica mal."""
    import urllib.error

    def _lanzar(cabeceras):
        raise _http_error(403, cabeceras)

    original = ri.urllib.request.urlopen
    try:
        ri.urllib.request.urlopen = lambda *a, **k: _lanzar(
            {"X-RateLimit-Remaining": "0", "X-RateLimit-Reset": "1700000000"})
        try:
            ri._get_json("https://api.github.com/repos/x/y")
            assert False, "deberia haber lanzado LimiteApiAgotado"
        except ri.LimiteApiAgotado as e:
            assert "cuota" in str(e)

        # 403 sin agotamiento de cuota: se propaga tal cual, no se enmascara.
        ri.urllib.request.urlopen = lambda *a, **k: _lanzar(
            {"X-RateLimit-Remaining": "57"})
        try:
            ri._get_json("https://api.github.com/repos/x/y")
            assert False, "deberia haber propagado el HTTPError"
        except ri.LimiteApiAgotado:
            assert False, "un 403 por permisos no es agotamiento de cuota"
        except urllib.error.HTTPError:
            pass
    finally:
        ri.urllib.request.urlopen = original


# ---------------------------------------------------------------------------
# Inventario del RAG
# ---------------------------------------------------------------------------

def _escribir_doc(directorio, nombre, url, cuerpo="Contenido de la guia. " * 20):
    os.makedirs(directorio, exist_ok=True)
    with open(os.path.join(directorio, nombre), "w", encoding="utf-8") as fh:
        fh.write(f"---\ndoc_id: {nombre[:-3]}\nsource_url: {url}\n"
                 f"retrieved_at: 2026-08-20T00:00:00+00:00\n---\n\n{cuerpo}\n")


def test_inventario_agrupa_por_producto_y_version():
    tmp = tempfile.mkdtemp()
    cwd = os.getcwd()
    try:
        os.chdir(tmp)
        base = "https://www.cisco.com/c/en/us/td/docs/voice_ip_comm"
        _escribir_doc("docs/pages", "a.md", f"{base}/cucm/admin/15/systemConfig/g.html")
        _escribir_doc("docs/pages", "b.md", f"{base}/cucm/admin/15/featureConfig/g.html")
        _escribir_doc("docs/pages", "c.md", f"{base}/connection/15/administration/guide/g.html")
        os.makedirs("docs/pages/openapi", exist_ok=True)
        with open("docs/pages/openapi/op.md", "w", encoding="utf-8") as fh:
            fh.write("---\ndoc_id: op\napi: Webex Admin\nmethod: GET\n---\n\nGET /x\n")

        ruta, stats = resumen_rag.generar(fecha="2026-08-20 00:00 UTC")
        texto = open(ruta, encoding="utf-8").read()

        assert stats["documentos"] == 3
        assert stats["operaciones"] == 1
        assert "Cisco Unified Communications Manager (CUCM)" in texto
        assert "Cisco Unity Connection" in texto
        assert "Webex Admin" in texto
        assert "no editar a mano" in texto.lower()
    finally:
        os.chdir(cwd)
        shutil.rmtree(tmp, ignore_errors=True)


def test_inventario_avisa_si_el_rastreo_no_ha_terminado():
    """Sin este aviso, las cifras se leen como cobertura final y se prometen
    respuestas que el agente todavia no puede dar."""
    tmp = tempfile.mkdtemp()
    cwd = os.getcwd()
    try:
        os.chdir(tmp)
        _escribir_doc("docs/pages", "a.md",
                      "https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/15/g.html")
        os.makedirs("logs", exist_ok=True)
        with open("logs/frontier.json", "w", encoding="utf-8") as fh:
            json.dump([{"url": f"https://x/{i}"} for i in range(4321)], fh)

        ruta, stats = resumen_rag.generar()
        texto = open(ruta, encoding="utf-8").read()
        assert stats["pendientes"] == 4321
        assert "4.321" in texto, "el separador de miles debe ser el espanol"
        assert "no ha terminado" in texto
    finally:
        os.chdir(cwd)
        shutil.rmtree(tmp, ignore_errors=True)


def test_inventario_sin_frontera_no_avisa():
    tmp = tempfile.mkdtemp()
    cwd = os.getcwd()
    try:
        os.chdir(tmp)
        _escribir_doc("docs/pages", "a.md",
                      "https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/15/g.html")
        ruta, stats = resumen_rag.generar()
        assert stats["pendientes"] == 0
        assert "no ha terminado" not in open(ruta, encoding="utf-8").read()
    finally:
        os.chdir(cwd)
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    pruebas = [v for k, v in sorted(globals().items())
               if k.startswith("test_") and callable(v)]
    for prueba in pruebas:
        prueba()
        print(f"  OK {prueba.__name__}")
    print(f"\n{len(pruebas)} PRUEBAS PASARON")
