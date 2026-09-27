"""Texto de los PDF admitidos por `config.pdf_permitidos_regex`.

Un PDF no puede pasar por el navegador: Chromium devuelve el visor, no el
documento, y el sanitizador se queda en cero caracteres. Por eso el PDF se
baja directo y se extrae aquí su texto.

`pypdf` se importa DENTRO de `texto_de_pdf`, igual que crawl4ai en
`crawler_ai.deep_crawl`. Es lo que mantiene `import crawler_ai` funcionando
sin la dependencia instalada, de lo que dependen la guarda de `tests.yml` y
la ligereza de `paquete.yml`.
"""
import re
import urllib.error
import urllib.request
from io import BytesIO
from urllib.parse import urlparse

# 40 MB. El diccionario de datos de CUCM ronda los 15 MB; el tope está para
# que un enlace a una imagen ISO mal clasificada no llene el disco del
# runner, no para recortar documentos legítimos.
MAX_BYTES = 40 * 1024 * 1024

_ESPACIOS = re.compile(r"[ \t]+")
_LINEAS = re.compile(r"\n{3,}")


def es_pdf(url):
    """Cierto si la RUTA termina en .pdf. Se mira la ruta y no la URL entera
    para que un `?descarga=algo.pdf` no cuente."""
    return urlparse(url).path.lower().endswith(".pdf")


def descargar(url, user_agent, timeout=60, max_bytes=MAX_BYTES):
    """Devuelve `(codigo, datos)`. Un HTTPError devuelve su código y b"",
    para que el llamante lo pase por `fetch_policy.tras_respuesta` igual que
    cualquier otra respuesta: un 403 del WAF tiene que ir a cuarentena, no
    convertirse en una excepción suelta.
    """
    pedido = urllib.request.Request(url, headers={
        "User-Agent": user_agent,
        "Accept": "application/pdf",
    })
    try:
        with urllib.request.urlopen(pedido, timeout=timeout) as respuesta:
            declarado = int(respuesta.headers.get("Content-Length") or 0)
            if declarado > max_bytes:
                raise ValueError(f"PDF de {declarado} bytes, por encima del "
                                 f"tope de {max_bytes}")
            return respuesta.status, respuesta.read(max_bytes)
    except urllib.error.HTTPError as e:
        return e.code, b""


def texto_de_pdf(datos):
    """Texto plano del PDF. Cadena vacía si no se puede extraer nada.

    Un PDF escaneado no lleva capa de texto y devuelve "": el llamante lo
    trata como cualquier otra página sin cuerpo.
    """
    from pypdf import PdfReader

    lector = PdfReader(BytesIO(datos))
    partes = []
    for pagina in lector.pages:
        try:
            trozo = pagina.extract_text() or ""
        except Exception:
            # Una página ilegible no invalida el resto del documento.
            continue
        if trozo.strip():
            partes.append(trozo.strip())

    texto = _ESPACIOS.sub(" ", "\n\n".join(partes))
    return _LINEAS.sub("\n\n", texto).strip()
