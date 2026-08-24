"""
state_store.py — Persistencia de estado y transición BATCH -> INCREMENTAL.

MODELO
------
Un único manifiesto (logs/manifest.json) con una entrada por URL:

    {
      "doc_id":        id estable derivado de la URL (nombre de fichero)
      "content_sha":   hash del markdown YA SANITIZADO
      "etag":          cabecera ETag de la última respuesta
      "last_modified": cabecera Last-Modified de la última respuesta
      "first_seen":    ISO timestamp
      "last_seen":     ISO timestamp de la última visita (haya cambiado o no)
      "last_changed":  ISO timestamp del último cambio real de contenido
      "unchanged_runs": nº de ejecuciones consecutivas sin cambio
      "next_check":    ISO timestamp — antes de esta fecha no se revisita
      "status":        "active" | "gone" | "blocked" | "redirect"
      "redirect_to":   URL destino, solo si status == "redirect"
      "fail_count":    fallos consecutivos
    }

TRES CORRECCIONES SOBRE EL DISEÑO ANTERIOR
------------------------------------------
1. El código original comparaba contra un set GLOBAL de hashes (seen_hashes).
   Eso confunde "esta página no ha cambiado" con "otra página tiene el mismo
   contenido", y hace imposible detectar deltas de forma fiable. Aquí la
   comparación es POR URL contra su hash anterior.

2. El original escribía en modo append sobre un markdown consolidado. En un
   pipeline RAG eso duplica chunks en cada recrawl y deja contenido obsoleto
   en el índice para siempre. Aquí cada documento es un fichero propio con
   doc_id estable, que se REEMPLAZA al cambiar.

3. El original nunca escribía logs/more_work.flag, que es justo lo que
   etl.yml comprueba para encadenar lotes — la ejecución continua nunca se
   disparaba. Aquí se escribe explícitamente.

SALIDA PARA EL CONSUMIDOR RAG
-----------------------------
Cada ejecución emite logs/deltas.json con las listas added / modified /
removed en términos de doc_id, para que el paso de indexación haga upsert y
delete selectivos en lugar de reconstruir el índice completo.
"""

import hashlib
import json
import os
import re
from datetime import datetime, timedelta, timezone
from urllib.parse import urlparse

RUTA_MANIFIESTO = "logs/manifest.json"
RUTA_DELTAS = "logs/deltas.json"
RUTA_FRONTERA = "logs/frontier.json"
RUTA_FLAG_TRABAJO = "logs/more_work.flag"
DIR_DOCS = "docs/pages"


def ahora():
    return datetime.now(timezone.utc)


def iso(dt):
    return dt.isoformat()


def parse_iso(texto, por_defecto=None):
    try:
        return datetime.fromisoformat(texto)
    except (TypeError, ValueError):
        return por_defecto


def doc_id_para(url):
    """ID estable y legible. El sufijo de hash evita colisiones cuando dos
    rutas distintas se normalizan al mismo slug."""
    parsed = urlparse(url)
    slug = f"{parsed.netloc}{parsed.path}".lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug).strip("-")[:120]
    sufijo = hashlib.sha1(url.encode("utf-8")).hexdigest()[:10]
    return f"{slug}-{sufijo}"


def hash_contenido(texto):
    return hashlib.sha256(texto.encode("utf-8")).hexdigest()


class ManifestStore:
    MODO_BOOTSTRAP = "bootstrap"
    MODO_INCREMENTAL = "incremental"

    def __init__(self, ruta=RUTA_MANIFIESTO):
        self.ruta = ruta
        self.entradas = {}
        self.deltas = {"added": [], "modified": [], "unchanged": [],
                       "removed": [], "blocked": []}
        self._cargar()

    def _cargar(self):
        if os.path.exists(self.ruta):
            try:
                with open(self.ruta, "r", encoding="utf-8") as f:
                    datos = json.load(f)
                self.entradas = datos.get("entradas", {})
            except Exception:
                self.entradas = {}

    @property
    def modo(self):
        """Sin manifiesto poblado -> primera captura estática completa."""
        activos = [e for e in self.entradas.values() if e.get("status") == "active"]
        return self.MODO_BOOTSTRAP if len(activos) == 0 else self.MODO_INCREMENTAL

    # -- decisión de revisita ------------------------------------------------

    def debe_visitar(self, url):
        entrada = self.entradas.get(url)
        if entrada is None:
            return True
        if entrada.get("status") == "gone":
            return False
        if entrada.get("status") == "blocked":
            # No se reintenta automáticamente: requiere revisión manual.
            return False
        if (entrada.get("status") == "redirect"
                and entrada.get("http_status") in (301, 308)):
            # Redirección permanente: esta URL no volverá a servir contenido.
            # Las temporales (302/303/307) sí se revisan cuando toca su TTL.
            return False
        proxima = parse_iso(entrada.get("next_check", ""))
        if proxima is None:
            return True
        return ahora() >= proxima

    def cabeceras_condicionales(self, url):
        """Cabeceras para GET condicional. Un 304 ahorra ancho de banda al
        origen y reduce drásticamente la probabilidad de que el WAF nos
        clasifique como carga abusiva."""
        entrada = self.entradas.get(url) or {}
        cabeceras = {}
        if entrada.get("etag"):
            cabeceras["If-None-Match"] = entrada["etag"]
        if entrada.get("last_modified"):
            cabeceras["If-Modified-Since"] = entrada["last_modified"]
        return cabeceras

    # -- TTL adaptativo ------------------------------------------------------

    @staticmethod
    def _calcular_ttl(unchanged_runs):
        """Backoff de revisita: la documentación estable se consulta cada vez
        menos. Techo de 30 días para no dejar nada rancio indefinidamente."""
        dias = min(30, 2 ** min(unchanged_runs, 5))
        return timedelta(days=max(1, dias))

    # -- registro de resultados ---------------------------------------------

    def registrar_contenido(self, url, markdown):
        """Compara contra el hash previo DE ESTA URL y clasifica el delta.
        Devuelve (cambio: bool, doc_id: str)."""
        entrada = self.entradas.get(url)
        nuevo_hash = hash_contenido(markdown)
        t = ahora()
        did = entrada.get("doc_id") if entrada else doc_id_para(url)

        if entrada is None:
            self.entradas[url] = {
                "doc_id": did,
                "content_sha": nuevo_hash,
                "etag": None,
                "last_modified": None,
                "first_seen": iso(t),
                "last_seen": iso(t),
                "last_changed": iso(t),
                "unchanged_runs": 0,
                "next_check": iso(t + self._calcular_ttl(0)),
                "status": "active",
                "fail_count": 0,
            }
            self.deltas["added"].append(did)
            return True, did

        entrada["last_seen"] = iso(t)
        entrada["status"] = "active"
        entrada["fail_count"] = 0

        if entrada.get("content_sha") == nuevo_hash:
            entrada["unchanged_runs"] = entrada.get("unchanged_runs", 0) + 1
            entrada["next_check"] = iso(t + self._calcular_ttl(entrada["unchanged_runs"]))
            self.deltas["unchanged"].append(did)
            return False, did

        entrada["content_sha"] = nuevo_hash
        entrada["last_changed"] = iso(t)
        entrada["unchanged_runs"] = 0
        entrada["next_check"] = iso(t + self._calcular_ttl(0))
        self.deltas["modified"].append(did)
        return True, did

    def registrar_no_modificado(self, url):
        """Respuesta 304: el origen confirma que no hay cambio. Ni siquiera
        hace falta sanitizar."""
        entrada = self.entradas.get(url)
        if not entrada:
            return
        t = ahora()
        entrada["last_seen"] = iso(t)
        entrada["unchanged_runs"] = entrada.get("unchanged_runs", 0) + 1
        entrada["next_check"] = iso(t + self._calcular_ttl(entrada["unchanged_runs"]))
        entrada["fail_count"] = 0
        self.deltas["unchanged"].append(entrada["doc_id"])

    def registrar_cabeceras(self, url, etag=None, last_modified=None):
        entrada = self.entradas.get(url)
        if not entrada:
            return
        if etag:
            entrada["etag"] = etag
        if last_modified:
            entrada["last_modified"] = last_modified

    def registrar_desaparecido(self, url):
        """404/410: se emite tombstone para que el índice vectorial borre el
        documento. Sin esto, el agente RAG sigue citando páginas retiradas."""
        entrada = self.entradas.get(url)
        if not entrada:
            return
        entrada["status"] = "gone"
        entrada["last_seen"] = iso(ahora())
        self.deltas["removed"].append(entrada["doc_id"])

        ruta = os.path.join(DIR_DOCS, f"{entrada['doc_id']}.md")
        if os.path.exists(ruta):
            os.remove(ruta)

    def registrar_redireccion(self, url, destino, codigo=301):
        """3xx: el recurso existe, pero en otra URL.

        No es un fallo (no incrementa fail_count) ni un tombstone (no borra
        nada ni emite delta 'removed'): el documento se indexará bajo su URL
        canónica, que es la que se encola en su lugar. Confundir esto con un
        fallo era justo lo que aparcaba las URLs de developer.cisco.com.
        """
        entrada = self.entradas.setdefault(url, {
            "doc_id": doc_id_para(url), "content_sha": None,
            "first_seen": iso(ahora()), "unchanged_runs": 0, "fail_count": 0,
        })
        t = ahora()
        entrada["status"] = "redirect"
        entrada["redirect_to"] = destino
        entrada["http_status"] = codigo
        entrada["last_seen"] = iso(t)
        entrada["next_check"] = iso(t + self._calcular_ttl(
            entrada.get("unchanged_runs", 0)))
        # Limpia los intentos que la URL arrastrase de cuando un 3xx se
        # clasificaba como fallo.
        entrada["fail_count"] = 0

    def registrar_bloqueo(self, url, codigo):
        entrada = self.entradas.setdefault(url, {
            "doc_id": doc_id_para(url), "content_sha": None,
            "first_seen": iso(ahora()), "unchanged_runs": 0, "fail_count": 0,
        })
        entrada["status"] = "blocked"
        entrada["last_seen"] = iso(ahora())
        entrada["fail_count"] = entrada.get("fail_count", 0) + 1
        entrada["http_status"] = codigo
        self.deltas["blocked"].append(entrada["doc_id"])

    def registrar_fallo(self, url):
        entrada = self.entradas.get(url)
        if not entrada:
            return
        entrada["fail_count"] = entrada.get("fail_count", 0) + 1
        # Tras 5 fallos consecutivos se aparca; no se reintenta cada ejecución.
        if entrada["fail_count"] >= 5:
            entrada["next_check"] = iso(ahora() + timedelta(days=14))

    # -- escritura de documentos --------------------------------------------

    @staticmethod
    def escribir_documento(doc_id, url, markdown):
        """Un fichero por documento, sobrescrito en cada cambio. El front
        matter da al indexador metadatos de procedencia sin parsear el cuerpo."""
        os.makedirs(DIR_DOCS, exist_ok=True)
        ruta = os.path.join(DIR_DOCS, f"{doc_id}.md")
        cabecera = (
            "---\n"
            f"doc_id: {doc_id}\n"
            f"source_url: {url}\n"
            f"retrieved_at: {iso(ahora())}\n"
            "---\n\n"
        )
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(cabecera + markdown)
        return ruta

    # -- persistencia --------------------------------------------------------

    def guardar(self):
        os.makedirs(os.path.dirname(self.ruta), exist_ok=True)
        with open(self.ruta, "w", encoding="utf-8") as f:
            json.dump({
                "schema_version": 2,
                "updated_at": iso(ahora()),
                "entradas": self.entradas,
            }, f, indent=2, sort_keys=True)

    def guardar_deltas(self, ruta=RUTA_DELTAS):
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        resumen = {
            "run_at": iso(ahora()),
            "modo": self.modo,
            "added": sorted(set(self.deltas["added"])),
            "modified": sorted(set(self.deltas["modified"])),
            "removed": sorted(set(self.deltas["removed"])),
            "blocked": sorted(set(self.deltas["blocked"])),
            "unchanged_count": len(self.deltas["unchanged"]),
        }
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(resumen, f, indent=2)
        return resumen


# ---------------------------------------------------------------------------
# Frontera persistente entre ejecuciones de GitHub Actions
# ---------------------------------------------------------------------------

def guardar_frontera(pendientes, ruta=RUTA_FRONTERA):
    """pendientes: lista de (url, depth)."""
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    if pendientes:
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump([{"url": u, "depth": d} for u, d in pendientes], f, indent=2)
        # Señal que etl.yml consulta para encadenar el siguiente lote.
        with open(RUTA_FLAG_TRABAJO, "w", encoding="utf-8") as f:
            f.write(str(len(pendientes)))
    else:
        for p in (ruta, RUTA_FLAG_TRABAJO):
            if os.path.exists(p):
                os.remove(p)


def cargar_frontera(ruta=RUTA_FRONTERA):
    if not os.path.exists(ruta):
        return []
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            return [(item["url"], item["depth"]) for item in json.load(f)]
    except Exception:
        return []
                    
