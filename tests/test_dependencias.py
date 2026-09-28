"""El lock y requirements.txt no pueden divergir en silencio.

`etl.yml` instala desde `requirements.lock.txt`. Si alguien sube la version
de crawl4ai en `requirements.txt` y olvida regenerar el lock, el ETL sigue
instalando la vieja y no falla nada: el sintoma vuelve a ser silencio, no
error. Estas pruebas convierten ese olvido en un fallo de CI.

Sin `packaging`: comprobar que un rango se satisface exigiria un parser de
versiones, y no hay garantia de que ese paquete este instalado en los
workflows. Se comprueba lo que de verdad falla, que es el pin exacto.
"""
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# nombre, operador, version. Basta para `paquete==1.2.3` y `paquete>=1,<2`.
_LINEA = re.compile(r"^([A-Za-z0-9._-]+)\s*(.*)$")


def _leer(nombre):
    ruta = os.path.join(RAIZ, nombre)
    with open(ruta, encoding="utf-8") as fh:
        for linea in fh:
            linea = linea.split("#")[0].strip()
            if not linea:
                continue
            m = _LINEA.match(linea)
            assert m, f"linea no reconocida en {nombre}: {linea!r}"
            yield m.group(1).lower().replace("_", "-"), m.group(2).strip()


def _lock():
    return {n: e.lstrip("=") for n, e in _leer("requirements.lock.txt")}


def test_el_lock_existe_y_esta_todo_fijado():
    bloqueado = _lock()
    assert len(bloqueado) > 50, f"solo {len(bloqueado)} paquetes: el lock esta truncado"
    for nombre, version in bloqueado.items():
        assert version, f"{nombre} sin version en el lock"


def test_cada_dependencia_declarada_esta_en_el_lock():
    bloqueado = _lock()
    for nombre, _ in _leer("requirements.txt"):
        assert nombre in bloqueado, (
            f"{nombre} esta en requirements.txt pero no en el lock: "
            f"regeneralo (ver la cabecera del lock)")


def test_los_pines_exactos_coinciden():
    # crawl4ai==0.9.2 es un pin de seguridad, no una preferencia: las
    # versiones anteriores a 0.8.6 dependian de un `litellm` comprometido.
    # Si el lock se quedara atras, el ETL instalaria la version vieja.
    bloqueado = _lock()
    exactos = [(n, e[2:].strip()) for n, e in _leer("requirements.txt")
               if e.startswith("==")]
    assert exactos, "ningun pin exacto en requirements.txt: revisa el parseo"
    for nombre, version in exactos:
        assert bloqueado[nombre] == version, (
            f"{nombre}: requirements.txt pide {version}, "
            f"el lock trae {bloqueado[nombre]}")


def test_playwright_esta_fijado_aunque_no_se_declare():
    # No se declara a proposito en requirements.txt (lo resuelve crawl4ai),
    # pero es la dependencia cuya version decide que Chromium se descarga.
    # Que flote es justo lo que el lock viene a evitar.
    assert "playwright" in _lock()


def _pruebas():
    return [(n, o) for n, o in sorted(globals().items())
            if n.startswith("test_") and callable(o)]


if __name__ == "__main__":
    fallos = 0
    for nombre, prueba in _pruebas():
        try:
            prueba()
        except AssertionError as e:
            fallos += 1
            print(f"FALLO {nombre}: {e}")
    if fallos:
        sys.exit(1)
    print(f"{len(_pruebas())} PRUEBAS PASARON")
