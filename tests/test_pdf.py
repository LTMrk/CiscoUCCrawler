"""Extraccion de texto de PDF y la excepcion acotada al veto de `\\.pdf$`.

El PDF de prueba se construye a mano en lugar de guardarlo como binario:
son 700 bytes de sintaxis PDF legible, y asi la prueba no depende de ningun
fichero que nadie pueda regenerar.
"""
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "src"))

from crawler_ai import (
    PDF_PERMITIDOS_REGEX, is_blocked_by_user, url_aceptable,
)
from pdf_texto import es_pdf, texto_de_pdf

TEXTO = "Diccionario de datos de CUCM"


def _pdf_minimo(texto=TEXTO):
    """PDF de una pagina con `texto` en una capa de texto real."""
    contenido = f"BT /F1 24 Tf 72 700 Td ({texto}) Tj ET".encode("latin-1")
    objetos = [
        b"<< /Type /Catalog /Pages 2 0 R >>",
        b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
        b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] "
        b"/Resources << /Font << /F1 4 0 R >> >> /Contents 5 0 R >>",
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
        b"<< /Length %d >>\nstream\n%s\nendstream" % (len(contenido), contenido),
    ]

    salida = bytearray(b"%PDF-1.4\n")
    desplazamientos = []
    for numero, cuerpo in enumerate(objetos, start=1):
        desplazamientos.append(len(salida))
        salida += b"%d 0 obj\n" % numero + cuerpo + b"\nendobj\n"

    inicio_xref = len(salida)
    salida += b"xref\n0 %d\n" % (len(objetos) + 1)
    salida += b"0000000000 65535 f \n"
    for d in desplazamientos:
        salida += b"%010d 00000 n \n" % d
    salida += (b"trailer\n<< /Size %d /Root 1 0 R >>\nstartxref\n%d\n%%%%EOF\n"
               % (len(objetos) + 1, inicio_xref))
    return bytes(salida)


def test_es_pdf_mira_la_ruta_no_la_query():
    assert es_pdf("https://www.cisco.com/x/guia.pdf")
    assert es_pdf("https://WWW.cisco.com/x/GUIA.PDF")
    # Una query que MENCIONA un .pdf no convierte la pagina en un PDF.
    assert not es_pdf("https://www.cisco.com/x/index.html?descarga=guia.pdf")
    assert not es_pdf("https://www.cisco.com/x/guia.html")


def test_texto_de_pdf_extrae_la_capa_de_texto():
    assert TEXTO in texto_de_pdf(_pdf_minimo())


def test_texto_de_pdf_sin_capa_de_texto_devuelve_vacio():
    # Sin operador Tj no hay texto: tiene que dar "", no reventar. Es el
    # caso del PDF escaneado, y el crawler lo trata como pagina sin cuerpo.
    original = b"BT /F1 24 Tf 72 700 Td (%s) Tj ET" % TEXTO.encode("latin-1")
    # Mismo numero de bytes: si cambiara la longitud, se desplazarian todos
    # los objetos posteriores y la xref quedaria mal. Se estaria probando un
    # PDF roto, no un PDF sin texto.
    sin_texto = b"0 0 0 rg 10 10 20 20 re f".ljust(len(original))
    vacio = _pdf_minimo().replace(original, sin_texto)
    assert len(vacio) == len(_pdf_minimo())
    assert texto_de_pdf(vacio) == ""


DICCIONARIO = ("https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/"
               "datadictionary/15_0_1/dd_15_0_1.pdf")


def test_el_pdf_del_diccionario_de_datos_entra():
    assert not is_blocked_by_user(DICCIONARIO)
    assert url_aceptable(DICCIONARIO)


def test_todo_patron_admitido_termina_en_pdf():
    # `is_blocked_by_user` corta los cuatro ultimos caracteres de la URL
    # para reevaluar el resto de vetos. Ese corte solo es correcto si el
    # patron exige la extension; sin esto, un patron sin `\.pdf$` haria
    # que se recortaran cuatro bytes de la ruta y los vetos se evaluaran
    # sobre una URL que no existe.
    for r in PDF_PERMITIDOS_REGEX:
        assert r.pattern.endswith(r"\.pdf$"), r.pattern


def test_el_resto_de_los_pdf_siguen_fuera():
    # Cada guia de Cisco tiene su gemelo en PDF. Si la excepcion se ampliara
    # a todo voice_ip_comm, el corpus se duplicaria entero.
    otros = [
        "https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/"
        "15/ccmsys/cucm_b_system-configuration-guide.pdf",
        "https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/"
        "design/guide/b_15cucdg.pdf",
    ]
    for u in otros:
        assert is_blocked_by_user(u), u


def test_la_excepcion_no_desactiva_los_demas_vetos():
    # Mismo PDF bajo una ruta de idioma: blocked_patterns manda, y se
    # comprueba ANTES que la excepcion.
    assert is_blocked_by_user(DICCIONARIO.replace("/en/us/", "/es-es/"))

    # Y bajo una ruta vetada por blocked_regex, que es la que la excepcion
    # reevalua. Sin la reevaluacion este PDF entraria.
    obsoleto = ("https://www.cisco.com/c/en/us/obsolete/td/docs/"
                "voice_ip_comm/cucm/datadictionary/15_0_1/dd.pdf")
    assert any(r.search(obsoleto) for r in PDF_PERMITIDOS_REGEX), (
        "el caso no prueba nada si la URL no casa con la excepcion")
    assert is_blocked_by_user(obsoleto)


def test_el_html_del_diccionario_no_necesita_la_excepcion():
    # La excepcion es solo para la extension: el HTML equivalente ya pasaba.
    assert url_aceptable(DICCIONARIO[: -len(".pdf")] + ".html")


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
