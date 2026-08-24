"""
copilot_pack.py — Reempaqueta docs/ para consumo desde Microsoft 365 Copilot.

POR QUE EXISTE
--------------
El corpus de docs/pages + docs/repos son miles de ficheros .md. Eso no es
consumible por Copilot tal cual, por motivos que la documentacion de
Microsoft fija de forma explicita:

  1. `.md` NO esta en la lista de tipos sobre los que Copilot razona. Los
     formatos de texto plano admitidos son .txt (y .html solo via SharePoint).
     Un .md se sube sin error y despues simplemente no responde nada.

  2. Sin licencia de Copilot con agentes, la unica via es un chat normal:
     adjuntar ficheros sueltos (limite de 3 por conversacion cada 24h en la
     version no licenciada) o compartir un enlace a una carpeta de
     OneDrive/SharePoint. Un ZIP no sirve como fuente directa: Copilot no lee
     dentro de un .zip, asi que hay que descomprimirlo en destino.

  3. Copilot no parsea tablas ni formato especial. Las tablas markdown que
     emite el sanitizador hay que linealizarlas o su contenido se pierde.

ESTRATEGIA
----------
Dos perfiles, porque hay dos formas de consumir el resultado con requisitos
opuestos:

  chat (por defecto)  Pensado para un chat normal de Copilot SIN licencia de
                       agentes: pocos ficheros grandes (hasta 20 por
                       producto), empaquetados en un UNICO ZIP final. Se sube
                       ese ZIP a OneDrive/SharePoint, se descomprime y se
                       comparte el enlace a la carpeta.

  sharepoint           Pensado para un agente por producto en Agent Builder
                       (requiere licencia de Copilot con agentes): muchos
                       ficheros pequenos (<=36.000 caracteres) organizados en
                       carpetas, una por producto, para que cada agente
                       referencie solo la suya.

En ambos perfiles se separa `vigente/` de `historico/`:

    dist/copilot/cucm/vigente/...    <- ultima version de cada guia
    dist/copilot/cucm/historico/...  <- versiones anteriores

No se borra nada, pero solo `vigente/` entra en el ZIP final o se referencia
desde un agente, porque seis service releases de la misma guia producen
chunks casi identicos que compiten entre si en el indice y hunden el recall.

Los capitulos consecutivos de un mismo libro se concatenan hasta llenar el
presupuesto de caracteres del perfil, lo que reduce el numero de ficheros sin
cruzar el umbral. Un capitulo que por si solo pase del limite se parte por
parrafos.
"""

import argparse
import collections
import hashlib
import itertools
import json
import os
import re
import sys
import zipfile

# ---------------------------------------------------------------------------
# Parametros
# ---------------------------------------------------------------------------

# Umbral documentado por Microsoft para ficheros referenciados via carpeta de
# SharePoint. Superarlo no da error, pero por encima Copilot deja de escanear
# el contenido completo del fichero.
LIMITE_CHARS = 36_000

# render_paquete separa cada capitulo con una regla de 60 guiones y cuatro
# saltos de linea. Sin reservarlo, un paquete lleno se pasa del limite.
COSTE_SEPARADOR = 70

# PERFILES DE SALIDA
# ------------------
# Copilot tiene dos superficies distintas para consumir ficheros, con limites
# distintos, y lo que sirve para una es contraproducente en la otra:
#
#   sharepoint  El agente referencia una CARPETA como origen de conocimiento.
#               Microsoft recomienda <=36.000 caracteres por fichero; por
#               encima deja de escanear el fichero entero. Muchos ficheros
#               pequenos, sin tope de cantidad.
#
#   chat        Se adjuntan ficheros sueltos a una conversacion. El tope es de
#               20 ficheros por conversacion y 50 MB por fichero, y Copilot
#               indexa 1,8 M de caracteres por fichero. Aqui interesa lo
#               contrario: pocos ficheros y grandes.
#
# En el perfil `chat` se permite mezclar capitulos de libros distintos en el
# mismo fichero, porque con 20 huecos no hay margen para respetar fronteras.
PERFILES = {
    "sharepoint": {"limite": 36_000, "max_ficheros": None, "mezclar_libros": False},
    "chat": {"limite": 1_500_000, "max_ficheros": 20, "mezclar_libros": True},
}

DIR_ENTRADA = os.path.join("docs", "pages")
DIR_ENTRADA_REPOS = os.path.join("docs", "repos")
DIR_SALIDA = os.path.join("dist", "copilot")

FRONTMATTER = re.compile(r"^---\r?\n(.*?)\r?\n---\r?\n", re.S)


# ---------------------------------------------------------------------------
# Clasificacion por producto
# ---------------------------------------------------------------------------

# (clave, etiqueta, regex sobre source_url). El orden importa: gana la primera
# regex que casa, asi que lo especifico va antes que lo generico.
PRODUCTOS = [
    ("uccx", "Cisco Unified Contact Center Express (UCCX)",
     r"/cust_contact/contact_center/crs/|unified-contact-center-express"),
    ("ucce", "Cisco Unified/Packaged Contact Center Enterprise (UCCE, PCCE, ICM)",
     r"/cust_contact/contact_center/(icm_enterprise|pcce)/"
     r"|unified-contact-center-enterprise|packaged-contact-center"),
    ("cvp", "Cisco Unified CVP, Finesse y CUIC",
     r"/cust_contact/contact_center/(customer_voice_portal|finesse|intelligence_suite)/"
     r"|customer-voice-portal|/finesse|intelligence-center|socialminer"),
    ("impresence", "Cisco IM and Presence Service y Jabber",
     r"/cucm/im_presence/|/cups/|/jabber|im-presence"),
    ("cucm", "Cisco Unified Communications Manager (CUCM)",
     r"/voice_ip_comm/cucm/|unified-communications-manager|/cucme/|/cusm/"
     r"|skinny-call-control-protocol"),
    ("cuc", "Cisco Unity Connection",
     r"/voice_ip_comm/connection/|unity-connection|emergency-responder|speechview"),
    ("expressway", "Cisco Expressway, MRA y VCS",
     r"/voice_ip_comm/expressway/|expressway|video-communication-server"),
    ("cube", "Cisco CUBE, IOS Voice y SIP",
     r"/ios-xml/ios/voice/|unified-border-element|session-initiation-protocol"
     r"|ip-telephony-voice-over-ip|call-routing-dial-plans|/voice/h323/"),
    ("endpoints", "Telefonos IP y endpoints de TelePresence",
     r"/cuipph/|/telepresence/|collaboration-endpoints|ip-phone|webex-room"),
    ("cms", "Cisco Meeting Server y conferencing",
     r"/conferencing/|meeting-server"),
    ("plataforma", "Business Edition, UC on UCS y plataforma",
     r"business-edition|/ucs|uc-on-ucs"),
    ("diseno", "Guias de diseno (CVD, SRND, Preferred Architecture)",
     r"/solutions/CVD/|/uc_system/|collaboration-systems-release"),
    ("webexcloud", "Webex Cloud, Control Hub y Webex Calling",
     r"/cloudCollaboration/|help\.webex\.com|webex-control-hub|webex-app"
     r"|webex-teams|/spark|webex-calling|pricing\.webex\.com"),
    ("cc-otros", "Contact Center (otros componentes)",
     r"/cust_contact/"),
]

ETIQUETAS = {clave: etiqueta for clave, etiqueta, _ in PRODUCTOS}
ETIQUETAS["misc"] = "Documentos varios de colaboracion Cisco"
ETIQUETAS["webex-api"] = "APIs REST de Webex (OpenAPI)"
ETIQUETAS["webex-repos"] = "Documentacion de repositorios GitHub (SDKs, ejemplos de integracion)"


def clasificar_producto(url):
    for clave, _, patron in PRODUCTOS:
        if re.search(patron, url, re.I):
            return clave
    return "misc"


# ---------------------------------------------------------------------------
# Deteccion de version y familia documental
# ---------------------------------------------------------------------------

# Un token es "de version" si es numerico con separadores, con o sin sufijo de
# service update: 12_5_1, X15-4, 14SU2, 12x, v15.
TOKEN_VERSION = re.compile(r"^(x?\d+(su\d+)?|\d+x|su\d+|v\d+|release|version)$", re.I)

# Digitos incrustados dentro de un token alfanumerico: uccx_b_1251su1admin.
DIGITOS_INCRUSTADOS = re.compile(r"\d+(su\d+)?", re.I)


def _normalizar_segmento(segmento):
    """Colapsa cualquier marca de version dentro de un segmento de ruta.

    El \\b de las regex no sirve aqui porque el guion bajo es caracter de
    palabra: en `icm_enterprise_12_6_1` no hay frontera entre `e` y `12`. Por
    eso se tokeniza explicitamente por [-_.].
    """
    partes = re.split(r"([-_.])", segmento.lower())
    salida = []
    for parte in partes:
        if parte in "-_.":
            salida.append(parte)
        elif TOKEN_VERSION.match(parte):
            salida.append("#")
        else:
            salida.append(DIGITOS_INCRUSTADOS.sub("#", parte))
    texto = re.sub(r"(#[-_.]?)+", "#", "".join(salida))
    return texto.strip("#-_.")


def familia_documental(url):
    """Clave estable de un documento a traves de todas sus versiones.

    Ademas de colapsar las versiones, unifica los separadores: Cisco alterna
    entre `ucce_b_database-schema` y `ucce-b-database-schema` de una release a
    otra, y sin esto las dos variantes se toman por documentos distintos.
    """
    ruta = re.sub(r"^https?://[^/]+", "", url)
    segmentos = [s for s in ruta.split("/") if s]
    clave = "/".join(_normalizar_segmento(s) for s in segmentos)
    return re.sub(r"[-_.]+", "-", clave)


def clave_version(url):
    """Tupla ordenable con los numeros de la URL. Mas alto = mas reciente."""
    return tuple(int(n) for n in re.findall(r"\d+", url)[:8])


# Un segmento de version es lo que queda tras un prefijo alfabetico opcional:
# `icm_enterprise_15_0_1` -> `15_0_1`, `X15-5` -> `15-5`, `express_12_5_1_su1`.
# Con prefijo alfabetico (`icm_enterprise_15_0_1`, `finesse_1501`) se admite
# tambien la forma condensada de 3-4 digitos: el prefijo garantiza que es una
# release del producto y no otra cosa.
RE_VERSION_CON_PREFIJO = re.compile(
    r"^[a-z][a-z_]*_(x?\d{1,2}(?:[._-]\d+)*(?:[._-]?su\d+)?|\d{3,4}(?:su\d+)?)$",
    re.I)

# Sin prefijo hay que ser mucho mas estricto. El primer componente se limita a
# dos digitos, y la forma condensada de 3-4 digitos NO se admite: los arboles
# de telefonos usan segmentos como `7832`, `8832` o `6800`, que son modelos y
# no releases. Admitirlos llenaba el inventario de versiones inexistentes.
RE_VERSION_SUELTA = re.compile(
    r"^(x\d{1,2}(?:[-_.]\d+)*"
    r"|\d{1,2}(?:[._-]\d+)+(?:[._-]?su\d+)?"
    r"|\d{1,2}su\d+"
    r"|\d{1,2}x"
    r"|\d{1,2})$",
    re.I)


def etiqueta_version(url):
    """Version legible para el encabezado, si se puede deducir de la ruta.

    Cisco no usa una convencion unica: la version puede ser un segmento propio
    (`/15/`, `/X15-5/`) o ir pegada al nombre del arbol (`icm_enterprise_15_0_1`,
    `express_12_5_1_su1`). Sin cubrir el segundo caso, los arboles de Contact
    Center se quedaban sin version en el encabezado, que es justo la metadata
    que permite al agente no mezclar releases.

    Se exige que el primer componente numerico tenga como mucho dos digitos, o
    que el segmento lleve prefijo alfabetico. Asi `7821_7841_7861` (modelos de
    telefono) no se confunde con una version.
    """
    ruta = re.sub(r"^https?://[^/]+", "", url)
    for segmento in ruta.split("/"):
        if not segmento or segmento.endswith((".html", ".htm")):
            continue
        encontrado = (RE_VERSION_CON_PREFIJO.match(segmento)
                      or RE_VERSION_SUELTA.match(segmento))
        if encontrado:
            version = encontrado.group(1).upper()
            # Expressway se nombra oficialmente con guion (X15-5); el resto se
            # normaliza a puntos para que `15-0-1` y `15_0_1` no aparezcan como
            # dos versiones distintas en el inventario.
            if not version.startswith("X"):
                version = version.replace("_", ".").replace("-", ".")
            else:
                version = version.replace("_", "-")
            return re.sub(r"\.?(SU\d+)$", r"\1", version)
    return ""


# ---------------------------------------------------------------------------
# Conversion markdown -> texto plano consumible por Copilot
# ---------------------------------------------------------------------------

RE_IMAGEN = re.compile(r"!\[([^\]]*)\]\([^)]*\)")
RE_ENLACE = re.compile(r"\[([^\]]*)\]\([^)]*\)")
RE_ENFASIS = re.compile(r"(\*\*|__|\*|`)")
RE_SEPARADOR_TABLA = re.compile(r"^\s*\|[\s:|-]+\|\s*$")
RE_INICIO_FILA = re.compile(r"^\s*\|")
RE_ENCABEZADO = re.compile(r"^(#{1,6})\s+(.*)$")
RE_LINEAS_VACIAS = re.compile(r"\n{3,}")


def _celdas(fila):
    return [c.strip() for c in fila.strip().strip("|").split("|")]


def _fila_cerrada(fila):
    """Una fila esta completa cuando lleva su pipe de cierre."""
    return fila.rstrip().endswith("|")


def _linealizar_tabla(filas):
    """Convierte una tabla markdown en lineas 'Cabecera: valor'.

    Copilot no parsea tablas en contenido de SharePoint. Una tabla que se deja
    en pipes se indexa como una tira de simbolos y su informacion se pierde.
    Linealizada, cada fila es una frase autocontenida que si casa con una
    consulta.
    """
    filas = [f for f in filas if not RE_SEPARADOR_TABLA.match(f)]
    if not filas:
        return []
    cabecera = _celdas(filas[0])
    tiene_cabecera = any(cabecera) and len(filas) > 1
    cuerpo = filas[1:] if tiene_cabecera else filas
    salida = []
    for fila in cuerpo:
        celdas = _celdas(fila)
        if not any(celdas):
            continue
        if tiene_cabecera:
            pares = [f"{cabecera[i]}: {celdas[i]}"
                     for i in range(min(len(cabecera), len(celdas)))
                     if celdas[i] and cabecera[i]]
            salida.append("- " + ("; ".join(pares) if pares
                                  else " ".join(c for c in celdas if c)))
        else:
            salida.append("- " + " ".join(c for c in celdas if c))
    return salida


RE_VINETA = re.compile(r"^\s*([-*+]|\d+[.)])\s+")


def _emitir(salida, linea):
    """Anade una linea evitando repetir la anterior.

    Las paginas de Cisco traen el titulo del documento y el del capitulo dos
    veces (una como texto suelto y otra como encabezado H1). Duplicado en cada
    fichero, es una linea que casa con todo y no distingue nada.
    """
    previa = next((x for x in reversed(salida) if x.strip()), None)
    if linea and linea == previa:
        return
    salida.append(linea)


def a_texto_plano(markdown):
    """Markdown -> texto plano: aplana tablas, quita sintaxis, reconstruye los
    parrafos y conserva los encabezados como lineas de texto.

    La reconstruccion de parrafos no es cosmetica. El HTML de Cisco lleva
    saltos de linea y tabuladores dentro de las frases, y el markdown los
    arrastra tal cual ("Cisco\\n\\t\\trecommends performing regular backups").
    Un indice de busqueda que tokeniza eso pierde la frase entera. Markdown ya
    define que las lineas consecutivas son un mismo parrafo, asi que unirlas es
    ademas el renderizado correcto.
    """
    cuerpo = FRONTMATTER.sub("", markdown, count=1)
    salida = []
    buffer_tabla = []
    parrafo = []
    en_codigo = False

    def cerrar_parrafo():
        if parrafo:
            texto = re.sub(r"\s+", " ", " ".join(parrafo)).strip()
            if texto:
                _emitir(salida, texto)
            parrafo.clear()

    for linea in cuerpo.splitlines():
        if linea.strip().startswith("```"):
            cerrar_parrafo()
            en_codigo = not en_codigo
            continue  # se elimina la valla, se conserva el contenido
        if en_codigo:
            salida.append(linea)
            continue

        if RE_INICIO_FILA.match(linea):
            cerrar_parrafo()
            buffer_tabla.append(linea)
            continue
        # Una celda con salto de linea deja la fila sin su pipe de cierre: lo
        # que sigue es la continuacion de esa celda, no un parrafo nuevo.
        if buffer_tabla and linea.strip() and not _fila_cerrada(buffer_tabla[-1]):
            buffer_tabla[-1] += " " + linea.strip()
            continue
        if buffer_tabla:
            salida.extend(_linealizar_tabla(buffer_tabla))
            buffer_tabla.clear()

        linea = RE_ENLACE.sub(r"\1", RE_IMAGEN.sub(r"\1", linea))

        encabezado_md = RE_ENCABEZADO.match(linea)
        if encabezado_md:
            cerrar_parrafo()
            titulo = re.sub(r"\s+", " ", RE_ENFASIS.sub("", encabezado_md.group(2))).strip()
            if titulo:
                salida.append("")
                _emitir(salida, titulo)
            continue

        linea = RE_ENFASIS.sub("", linea)
        if not linea.strip():
            cerrar_parrafo()
            salida.append("")
        elif RE_VINETA.match(linea):
            cerrar_parrafo()
            _emitir(salida, re.sub(r"\s+", " ", linea).strip())
        else:
            parrafo.append(linea)

    cerrar_parrafo()
    if buffer_tabla:
        salida.extend(_linealizar_tabla(buffer_tabla))

    return RE_LINEAS_VACIAS.sub("\n\n", "\n".join(salida)).strip()


# ---------------------------------------------------------------------------
# Lectura del corpus
# ---------------------------------------------------------------------------

def leer_documento(ruta):
    with open(ruta, "r", encoding="utf-8", errors="replace") as fh:
        bruto = fh.read()
    meta = {}
    cabecera = FRONTMATTER.match(bruto)
    if cabecera:
        for linea in cabecera.group(1).splitlines():
            if ":" in linea:
                clave, valor = linea.split(":", 1)
                meta[clave.strip()] = valor.strip()
    return meta, bruto


def titulo_de(texto, url):
    """Primera linea con sustancia del cuerpo, como titulo del documento."""
    for linea in texto.splitlines():
        linea = linea.strip()
        if len(linea) > 3 and not linea.startswith(("|", "-", ">")):
            return linea[:160]
    return url.rsplit("/", 1)[-1]


def nombre_seguro(texto, maximo=90):
    texto = re.sub(r"[^\w\s-]", "", texto, flags=re.U).strip()
    texto = re.sub(r"[\s_]+", "-", texto).strip("-").lower()
    return texto[:maximo] or "documento"


def libro_de(url):
    """Libro/guia al que pertenece un capitulo, para agrupar capitulos
    consecutivos en el mismo fichero de salida."""
    ruta = re.sub(r"^https?://[^/]+", "", url)
    segmentos = [s for s in ruta.split("/") if s]
    return "/".join(segmentos[:-1]) if len(segmentos) > 1 else ruta


# ---------------------------------------------------------------------------
# Empaquetado
# ---------------------------------------------------------------------------

def encabezado(doc):
    lineas = [f"Producto: {ETIQUETAS.get(doc['producto'], doc['producto'])}"]
    if doc["version"]:
        lineas.append(f"Version: {doc['version']}")
    lineas.append(f"Documento: {doc['titulo']}")
    lineas.append(f"Fuente: {doc['url']}")
    if doc.get("retrieved_at"):
        lineas.append(f"Recuperado: {doc['retrieved_at'][:10]}")
    return "\n".join(lineas)


def partir_por_parrafos(texto, limite):
    """Parte un texto demasiado largo en trozos <= limite, cortando en lineas
    en blanco para no romper una frase por la mitad."""
    if len(texto) <= limite:
        return [texto]
    trozos, actual, tam = [], [], 0
    for parrafo in texto.split("\n\n"):
        if tam + len(parrafo) + 2 > limite and actual:
            trozos.append("\n\n".join(actual))
            actual, tam = [], 0
        while len(parrafo) > limite:  # parrafo unico mayor que el limite
            trozos.append(parrafo[:limite])
            parrafo = parrafo[limite:]
        actual.append(parrafo)
        tam += len(parrafo) + 2
    if actual:
        trozos.append("\n\n".join(actual))
    return trozos


def empaquetar(documentos, limite, mezclar_libros=False):
    """Agrupa capitulos consecutivos en ficheros de <= limite caracteres.

    Por defecto no mezcla libros: un fichero que salta de la guia de
    administracion a la de troubleshooting produce un chunk incoherente. Con
    `mezclar_libros` se relaja esa frontera, necesario en el perfil `chat`
    donde solo caben 20 ficheros por producto.
    """
    paquetes = []
    documentos.sort(key=lambda d: (d["libro"], d["url"]))
    if mezclar_libros:
        agrupado = [("todos", iter(documentos))]
    else:
        agrupado = itertools.groupby(documentos, key=lambda d: d["libro"])
    for libro, capitulos in agrupado:
        actual, tam = [], 0
        for capitulo in capitulos:
            bloque = encabezado(capitulo) + "\n\n" + capitulo["texto"]
            # El separador se cuenta tambien para un capitulo suelto: si no, un
            # capitulo que cabe por los pelos se pasa del limite al renderizar.
            if len(bloque) + COSTE_SEPARADOR > limite:
                if actual:
                    paquetes.append((libro, actual))
                    actual, tam = [], 0
                margen = len(encabezado(capitulo)) + COSTE_SEPARADOR + 32
                trozos = partir_por_parrafos(capitulo["texto"], limite - margen)
                for i, trozo in enumerate(trozos):
                    parte = dict(capitulo, texto=trozo)
                    if i:
                        parte["titulo"] = f"{capitulo['titulo']} (parte {i + 1})"
                    paquetes.append((libro, [parte]))
                continue
            if tam + len(bloque) + COSTE_SEPARADOR > limite and actual:
                paquetes.append((libro, actual))
                actual, tam = [], 0
            actual.append(capitulo)
            tam += len(bloque) + COSTE_SEPARADOR
        if actual:
            paquetes.append((libro, actual))
    return paquetes


def render_paquete(capitulos):
    partes = []
    for capitulo in capitulos:
        partes.extend([encabezado(capitulo), "", capitulo["texto"], "",
                       "-" * 60, ""])
    return "\n".join(partes).strip() + "\n"


# ---------------------------------------------------------------------------
# Pipeline
# ---------------------------------------------------------------------------

def recolectar(dir_entrada):
    documentos = []
    for raiz, _, ficheros in os.walk(dir_entrada):
        es_openapi = os.path.basename(raiz) == "openapi"
        for fichero in ficheros:
            if not fichero.endswith(".md"):
                continue
            ruta = os.path.join(raiz, fichero)
            meta, bruto = leer_documento(ruta)
            texto = a_texto_plano(bruto)
            if len(texto) < 200:  # tombstones y paginas vacias
                continue
            if es_openapi:
                api = meta.get("api", "Webex")
                documentos.append({
                    "ruta": ruta,
                    "url": meta.get("source", meta.get("doc_id", fichero)),
                    "producto": "webex-api",
                    "subgrupo": nombre_seguro(api, 40),
                    "familia": meta.get("doc_id", fichero),
                    "version": meta.get("api_version", ""),
                    "orden": (),
                    "libro": meta.get("tags", "") or nombre_seguro(api, 40),
                    "titulo": (f"{meta.get('method', '')} {meta.get('path', '')}".strip()
                               or meta.get("doc_id", fichero)),
                    "retrieved_at": meta.get("retrieved_at", ""),
                    "texto": texto,
                })
            elif meta.get("repo"):
                # Documento emitido por repos_ingest.py (SDKs, ejemplos de
                # integracion en GitHub). Se detecta por el campo `repo:` del
                # frontmatter, no por la ruta, para que la clasificacion no
                # dependa de en que directorio se le pase a recolectar().
                # Sin esta rama caian en clasificar_producto(), que no tiene
                # reglas para github.com y los mandaba a "misc", perdiendo la
                # etiqueta de producto y mezclandolos con paginas huerfanas.
                repo = meta["repo"]
                url = meta.get("source_url", "")
                documentos.append({
                    "ruta": ruta,
                    "url": url,
                    "producto": "webex-repos",
                    "subgrupo": nombre_seguro(repo.split("/")[-1], 40),
                    "familia": url,  # cada fichero de repo es unico, sin versiones que fusionar
                    "version": "",
                    "orden": (),
                    "libro": repo,
                    "titulo": titulo_de(texto, url),
                    "retrieved_at": meta.get("retrieved_at", ""),
                    "texto": texto,
                })
            else:
                url = meta.get("source_url", "")
                documentos.append({
                    "ruta": ruta,
                    "url": url,
                    "producto": clasificar_producto(url),
                    "subgrupo": "",
                    "familia": familia_documental(url),
                    "version": etiqueta_version(url),
                    "orden": clave_version(url),
                    "libro": libro_de(url),
                    "titulo": titulo_de(texto, url),
                    "retrieved_at": meta.get("retrieved_at", ""),
                    "texto": texto,
                })
    return documentos


DISTANCIA_DUPLICADO = 6  # bits de Hamming sobre un simhash de 64


def simhash(texto):
    """Huella de 64 bits sobre shingles de 4 palabras.

    Sirve para detectar que dos documentos son la misma guia en releases
    distintas aunque la URL no lo delate: Cisco renombra los slugs entre
    versiones (`...-handbook-1261` pasa a `...-guide-150`) y la comparacion
    por ruta se queda corta. El contenido, en cambio, apenas cambia.
    """
    palabras = re.findall(r"[a-z0-9]+", texto.lower())
    if len(palabras) < 8:
        return None
    pesos = [0] * 64
    for i in range(0, len(palabras) - 3, 3):
        shingle = " ".join(palabras[i:i + 4]).encode()
        h = int.from_bytes(hashlib.blake2b(shingle, digest_size=8).digest(), "big")
        for bit in range(64):
            pesos[bit] += 1 if (h >> bit) & 1 else -1
    huella = 0
    for bit in range(64):
        if pesos[bit] > 0:
            huella |= 1 << bit
    return huella


class _Union:
    """Union-find para fusionar los grupos que detectan la ruta y el contenido."""

    def __init__(self):
        self.padre = {}

    def raiz(self, x):
        self.padre.setdefault(x, x)
        while self.padre[x] != x:
            self.padre[x] = self.padre[self.padre[x]]
            x = self.padre[x]
        return x

    def unir(self, a, b):
        ra, rb = self.raiz(a), self.raiz(b)
        if ra != rb:
            self.padre[rb] = ra


def marcar_vigencia(documentos):
    """Marca cada documento como vigente o historico.

    Un documento es vigente si es la version mas alta de su familia. La familia
    se determina con dos senales que se fusionan: la ruta normalizada y la
    similitud de contenido dentro del mismo producto.
    """
    # webex-api: la spec OpenAPI ya trae una sola version por endpoint.
    # webex-repos: cada fichero de un repo es unico (README, guia de un SDK...),
    # no hay "releases" del mismo documento que fusionar por familia.
    SIN_VERSIONADO = {"webex-api", "webex-repos"}
    candidatos = [d for d in documentos if d["producto"] not in SIN_VERSIONADO]
    for doc in documentos:
        if doc["producto"] in SIN_VERSIONADO:
            doc["vigencia"] = "vigente"

    union = _Union()
    for i, doc in enumerate(candidatos):
        union.raiz(i)
        doc["_huella"] = simhash(doc["texto"])

    # Senal 1: misma familia de ruta.
    por_ruta = collections.defaultdict(list)
    for i, doc in enumerate(candidatos):
        por_ruta[doc["familia"]].append(i)
    for indices in por_ruta.values():
        for j in indices[1:]:
            union.unir(indices[0], j)

    # Senal 2: contenido casi identico dentro del mismo producto. La
    # comparacion se acota por producto para no hacerla contra el corpus
    # entero; dos releases de la misma guia nunca cambian de producto.
    por_producto = collections.defaultdict(list)
    for i, doc in enumerate(candidatos):
        if doc["_huella"] is not None:
            por_producto[doc["producto"]].append(i)
    for indices in por_producto.values():
        for pos, i in enumerate(indices):
            hi = candidatos[i]["_huella"]
            for j in indices[pos + 1:]:
                if bin(hi ^ candidatos[j]["_huella"]).count("1") <= DISTANCIA_DUPLICADO:
                    union.unir(i, j)

    grupos = collections.defaultdict(list)
    for i, doc in enumerate(candidatos):
        grupos[union.raiz(i)].append(doc)
    for grupo in grupos.values():
        grupo.sort(key=lambda d: (d["orden"], len(d["texto"])), reverse=True)
        for i, doc in enumerate(grupo):
            doc["vigencia"] = "vigente" if i == 0 else "historico"

    for doc in candidatos:
        doc.pop("_huella", None)
    return documentos


def escribir(documentos, dir_salida, perfil, dry_run=False):
    limite = perfil["limite"]
    grupos = collections.defaultdict(list)
    for doc in documentos:
        # En el perfil `chat` el tope de 20 ficheros es POR PRODUCTO, asi que
        # los subgrupos de webex-api no pueden ir a carpetas separadas: se
        # funden para que el reparto cuente sobre el producto entero.
        subgrupo = "" if perfil["mezclar_libros"] else doc["subgrupo"]
        grupos[(doc["producto"], doc["vigencia"], subgrupo)].append(doc)

    manifiesto = {}
    resumen = []
    avisos = []
    for (producto, vigencia, subgrupo), docs in sorted(grupos.items()):
        partes = [dir_salida, producto, vigencia]
        if subgrupo:
            partes.append(subgrupo)
        destino = os.path.join(*partes)
        paquetes = empaquetar(docs, limite, perfil["mezclar_libros"])
        tope = perfil["max_ficheros"]
        if tope and len(paquetes) > tope and vigencia == "vigente":
            avisos.append(f"{producto}/{vigencia}: {len(paquetes)} ficheros, "
                          f"por encima del tope de {tope} del perfil chat.")
        if not dry_run:
            os.makedirs(destino, exist_ok=True)
        usados = collections.Counter()
        entradas = []
        for _, capitulos in paquetes:
            base = nombre_seguro(capitulos[0]["titulo"])
            usados[base] += 1
            if usados[base] > 1:
                base = f"{base}-{usados[base]:02d}"
            contenido = render_paquete(capitulos)
            if not dry_run:
                with open(os.path.join(destino, base + ".txt"), "w",
                          encoding="utf-8") as fh:
                    fh.write(contenido)
            entradas.append({
                "fichero": base + ".txt",
                "chars": len(contenido),
                "capitulos": len(capitulos),
                "fuentes": [c["url"] for c in capitulos],
            })
        manifiesto[destino.replace("\\", "/")] = entradas
        resumen.append((producto, vigencia, subgrupo, len(docs),
                        sum(e["chars"] for e in entradas), len(entradas),
                        max((e["chars"] for e in entradas), default=0)))

    if not dry_run:
        os.makedirs(dir_salida, exist_ok=True)
        with open(os.path.join(dir_salida, "_manifiesto.json"), "w",
                  encoding="utf-8") as fh:
            json.dump(manifiesto, fh, indent=1, ensure_ascii=False)
    return resumen, avisos


# Dos guias distintas porque cada perfil se consume de una forma incompatible
# con la otra: "chat" es un chat normal de Copilot sin licencia de agentes
# (un ZIP, un enlace, arrastrar ficheros), "sharepoint" es un agente con
# carpeta propia (requiere licencia de Copilot con agentes). Mezclar las
# instrucciones en una sola guia le daria al lector pasos que no puede seguir.

GUIA_CABECERA_CHAT = """# Como usar este conocimiento en Microsoft 365 Copilot

Generado por `src/copilot_pack.py --perfil chat`. No editar a mano: se
reescribe en cada ejecucion.

## Que hay aqui

Un ZIP unico (`_zips/copilot-vigente-completo.zip`) con TODO el conocimiento
vigente, organizado en una carpeta por producto dentro del archivo. Pensado
para un chat normal de Copilot, **sin** licencia de agentes: no hace falta
crear nada en Agent Builder, solo compartir un enlace o arrastrar ficheros.

Los ficheros son `.txt` porque `.md` no esta entre los tipos que Copilot lee:
un `.md` se sube sin dar error y despues no responde nada. Ninguno pasa de
{limite} caracteres.

## Aviso importante: el ZIP es solo transporte

**Copilot no lee dentro de un archivo .zip.** Si compartes el enlace al .zip
tal cual, Copilot lo vera pero no podra usar su contenido. Hay que
descomprimirlo antes de que el chat lo use.

## Como montarlo

1. Descarga y descomprime `copilot-vigente-completo.zip`.
2. Sube la carpeta descomprimida (no el .zip) a tu OneDrive o SharePoint.
3. Comparte el enlace **a la carpeta**, con permiso de lectura para quien
   vaya a usar el chat.
4. En una conversacion de Microsoft 365 Copilot, pega ese enlace, o bien
   arrastra directamente hasta 20 de los `.txt` de la carpeta que necesites
   como adjuntos (limite de la version sin licencia de agentes: 3 ficheros
   por conversacion cada 24h, hasta 512 MB cada uno).
5. En el primer mensaje, indica el comportamiento esperado, por ejemplo:

> Eres un especialista en Cisco Unified Communications. Responde solo a
> partir de los ficheros adjuntos. Cita siempre la linea `Fuente:` del
> documento en el que te bases. Si la respuesta depende de la version,
> dilo de forma explicita. Si la documentacion no cubre la pregunta, dilo
> en lugar de deducir la respuesta.

## Inventario

"""

GUIA_CABECERA_SHAREPOINT = """# Despliegue de los agentes de M365 Copilot

Generado por `src/copilot_pack.py --perfil sharepoint`. No editar a mano: se
reescribe en cada ejecucion. **Requiere licencia de Copilot con agentes
(Agent Builder)**; sin ella, usa el perfil `chat` en su lugar.

## Que hay aqui

Una carpeta por producto. Cada carpeta es el conocimiento de **un agente
especialista**, no de un agente generalista: separar por producto es lo que
hace que el agente de CUCM no conteste con documentacion de UCCE.

Dentro de cada producto:

- `vigente/`   ultima version de cada guia. **Es lo que debe consumir el agente.**
- `historico/` versiones anteriores. No se sube salvo que alguien necesite un
  agente atado a una release concreta.

Los ficheros son `.txt` porque `.md` no esta entre los tipos sobre los que
Copilot razona: un `.md` se sube sin dar error y despues no responde nada.
Ninguno pasa de {limite} caracteres, el umbral que Microsoft documenta para
contenido referenciado por carpeta de SharePoint; por encima Copilot deja de
escanear el fichero entero.

## Como montarlo

1. En SharePoint, crea una biblioteca de documentos (por ejemplo
   `Documentacion Cisco UC`).
2. Sube una carpeta `vigente/` por cada producto que quieras cubrir,
   renombrandola con el nombre del producto.
3. Por cada agente, en Microsoft 365 Copilot: **Nuevo agente > Configurar**.
4. En **Conocimiento**, usa **Introducir URL** y pega la URL de la carpeta del
   producto. Una carpeta cuenta como 1 de las 100 fuentes permitidas y cubre
   todos sus subpaths.
5. Activa **Usar solo los origenes especificados** para que priorice la
   documentacion frente al conocimiento general del modelo.
6. Espera a que el estado de los ficheros pase de "Preparando" a listo. Con
   volumenes altos tarda del orden de minutos.

Sugerencia de instrucciones para cada agente:

> Eres un especialista en {{producto}}. Responde solo a partir de la
> documentacion oficial de Cisco que tienes como conocimiento. Cita siempre la
> linea `Fuente:` del documento en el que te bases. Si la respuesta depende de
> la version, dilo de forma explicita. Si la documentacion no cubre la
> pregunta, dilo en lugar de deducir la respuesta.

## Inventario

"""


def comprimir_todo(dir_salida, vigencia="vigente",
                   nombre="copilot-vigente-completo.zip"):
    """Empaqueta TODO el conocimiento vigente en un unico ZIP.

    Salida final del pipeline: un solo archivo, listo para subir a OneDrive y
    compartir un unico enlace. Conserva la carpeta de producto dentro del
    archivo, para que al descomprimir siga sabiendose a que tecnologia
    pertenece cada fichero.

    Aviso importante: Copilot NO lee dentro de un ZIP. El formato no aparece
    en ninguna lista de tipos soportados, ni como origen de conocimiento de
    un agente ni como adjunto de chat; se sube sin error y su contenido queda
    invisible. Este ZIP es transporte: hay que descomprimirlo en destino y
    compartir el enlace a la CARPETA resultante, no al .zip.
    """
    dir_zips = os.path.join(dir_salida, "_zips")
    os.makedirs(dir_zips, exist_ok=True)
    destino = os.path.join(dir_zips, nombre)
    total = 0
    with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for producto in sorted(os.listdir(dir_salida)):
            origen = os.path.join(dir_salida, producto, vigencia)
            if not os.path.isdir(origen):
                continue
            for raiz, _, ficheros in os.walk(origen):
                for fichero in sorted(ficheros):
                    ruta = os.path.join(raiz, fichero)
                    interno = os.path.join(producto,
                                           os.path.relpath(ruta, origen))
                    z.write(ruta, interno.replace("\\", "/"))
                    total += 1
    return destino, total, os.path.getsize(destino)


def _miles(n):
    """Separador de miles con punto, como se escribe en espanol."""
    return f"{n:,}".replace(",", ".")


def escribir_guia(dir_salida, resumen, limite, perfil="chat"):
    """Emite la guia de despliegue junto a la salida, con el inventario real."""
    cabecera = GUIA_CABECERA_SHAREPOINT if perfil == "sharepoint" else GUIA_CABECERA_CHAT
    lineas = [cabecera.format(limite=_miles(limite))]
    lineas.append("| Producto | Carpeta a subir | Ficheros | M caracteres |")
    lineas.append("|---|---|---:|---:|")
    vigentes = [r for r in resumen if r[1] == "vigente"]
    por_producto = collections.defaultdict(lambda: [0, 0])
    for producto, _, _, _, nchars, nfich, _ in vigentes:
        por_producto[producto][0] += nfich
        por_producto[producto][1] += nchars
    for producto in sorted(por_producto, key=lambda p: -por_producto[p][1]):
        nfich, nchars = por_producto[producto]
        lineas.append(f"| {ETIQUETAS.get(producto, producto)} | "
                      f"`{producto}/vigente/` | {_miles(nfich)} | {nchars / 1e6:.1f} |")

    historico = [r for r in resumen if r[1] == "historico"]
    if historico:
        total_f = sum(r[5] for r in historico)
        total_c = sum(r[4] for r in historico)
        lineas.append("")
        lineas.append(f"Ademas hay {_miles(total_f)} ficheros ({total_c / 1e6:.1f} M "
                      f"caracteres) en las carpetas `historico/`, con las "
                      f"versiones anteriores de cada guia.")

    ruta = os.path.join(dir_salida, "_DESPLIEGUE.md")
    with open(ruta, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lineas) + "\n")
    return ruta


# PERFIL_POR_DEFECTO en una constante propia (no solo un default= suelto en
# argparse) para que un test pueda fijar "el default es chat" importando este
# valor, en vez de re-parsear texto de ayuda o grepear el fuente.
PERFIL_POR_DEFECTO = "chat"


def construir_parser():
    """Parser de linea de comandos, en funcion propia para que los tests
    puedan verificar defaults y choices sin invocar main()."""
    ap = argparse.ArgumentParser(
        description="Reempaqueta docs/ en .txt para Microsoft 365 Copilot. "
                    "Por defecto (--perfil chat) produce un unico ZIP listo "
                    "para compartir por enlace, sin necesitar un agente.")
    ap.add_argument("--entrada", default=DIR_ENTRADA)
    ap.add_argument("--entrada-repos", default=DIR_ENTRADA_REPOS,
                    help="Documentacion de repos GitHub (repos_ingest.py). "
                         "Se omite si el directorio no existe.")
    ap.add_argument("--salida", default=DIR_SALIDA)
    ap.add_argument("--perfil", choices=sorted(PERFILES), default=PERFIL_POR_DEFECTO,
                    help="chat (por defecto): hasta 20 ficheros grandes por "
                         "producto, pensado para un unico ZIP que se sube a "
                         "OneDrive/SharePoint y se comparte por enlace, sin "
                         "necesitar un agente. sharepoint: muchos ficheros de "
                         "36.000 chars para referenciar una carpeta desde un "
                         "agente por producto (requiere licencia de Copilot "
                         "con agentes).")
    ap.add_argument("--limite", type=int, default=None,
                    help="Sobrescribe el limite de caracteres del perfil.")
    ap.add_argument("--zip", action="store_true",
                    help="Empaqueta todo el conocimiento vigente en UN UNICO "
                         "ZIP en _zips/. Es un contenedor de transporte: "
                         "Copilot NO lee dentro de un ZIP, hay que "
                         "descomprimirlo en destino y compartir el enlace a "
                         "la carpeta resultante.")
    ap.add_argument("--dry-run", action="store_true",
                    help="Calcula el reparto sin escribir nada.")
    return ap


def main(argv=None):
    args = construir_parser().parse_args(argv)

    perfil = dict(PERFILES[args.perfil])
    if args.limite:
        perfil["limite"] = args.limite

    print(f"Leyendo {args.entrada} ...", file=sys.stderr)
    documentos = recolectar(args.entrada)
    if os.path.isdir(args.entrada_repos):
        print(f"Leyendo {args.entrada_repos} ...", file=sys.stderr)
        documentos += recolectar(args.entrada_repos)
    print(f"  {len(documentos)} documentos, "
          f"{sum(len(d['texto']) for d in documentos) / 1e6:.1f} M chars tras limpieza",
          file=sys.stderr)

    marcar_vigencia(documentos)
    resumen, avisos = escribir(documentos, args.salida, perfil, args.dry_run)

    print(f"\n{'producto':12s} {'vigencia':10s} {'grupo':22s} "
          f"{'docs':>6s} {'M chars':>8s} {'ficheros':>9s} {'max':>7s}")
    print("-" * 84)
    for producto, vigencia, subgrupo, ndocs, nchars, nfich, mayor in resumen:
        print(f"{producto:12s} {vigencia:10s} {subgrupo:22s} "
              f"{ndocs:6d} {nchars / 1e6:7.1f}M {nfich:9d} {mayor:7d}")
    print("-" * 84)
    print(f"{'TOTAL':12s} {'':10s} {'':22s} {sum(r[3] for r in resumen):6d} "
          f"{sum(r[4] for r in resumen) / 1e6:7.1f}M "
          f"{sum(r[5] for r in resumen):9d}")

    for aviso in avisos:
        print(f"AVISO: {aviso}", file=sys.stderr)

    if not args.dry_run:
        ruta_guia = escribir_guia(args.salida, resumen, perfil["limite"], args.perfil)
        print(f"\nGuia de despliegue: {ruta_guia}")
        if args.zip:
            ruta, nficheros, tam = comprimir_todo(args.salida)
            print(f"\nZIP final (solo transporte; Copilot no lee dentro de un "
                  f"ZIP, descomprimir en destino):\n  {ruta}\n"
                  f"  {nficheros} ficheros, {tam / 1e6:.1f} MB")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
