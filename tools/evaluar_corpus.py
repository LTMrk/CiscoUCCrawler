#!/usr/bin/env python3
"""Mide si el corpus contiene una respuesta y si se encuentra por palabras.

QUÉ MIDE Y QUÉ NO. No predice lo que hará Microsoft 365 Copilot: su
recuperación es semántica y no se puede reproducir aquí. Lo que mide es la
parte que sí controlamos, que es si el documento adecuado está en el corpus
y si sale a flote con las palabras de la pregunta. Un fallo aquí es un
fallo seguro; un acierto es condición necesaria, no suficiente.

El corpus está en inglés. Una pregunta en español puntuará bajo aunque el
documento esté: eso no es un fallo del corpus, es el límite de una búsqueda
léxica, y por eso las preguntas del fichero llevan las palabras clave en
inglés. Si el equipo pregunta a Copilot en español, esa distancia la salva
Copilot, no esta herramienta.

Sin dependencias y sin red: recorre docs/ tal cual está commiteado. Unos 33
segundos sobre 15.800 documentos.

    python3 tools/evaluar_corpus.py
    python3 tools/evaluar_corpus.py --top 10 --preguntas otras.json
"""
import argparse
import json
import math
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR_DOCS = os.path.join(RAIZ, "docs")
PREGUNTAS = os.path.join(RAIZ, "evaluacion", "preguntas.json")

_PALABRA = re.compile(r"[a-z0-9]{2,}")
_URL = re.compile(r"^source_url:\s*(\S+)", re.MULTILINE)


def tokenizar(texto):
    return _PALABRA.findall(texto.lower())


# Parámetros de BM25, los habituales. k1 satura la frecuencia de término
# (la vigésima aparición de "axl" no vale como la segunda) y b controla
# cuánto penaliza la longitud.
K1 = 1.5
B = 0.75


def indexar(dir_docs, terminos):
    """Un solo recorrido del corpus. Devuelve (tf, df, urls, longitudes).

    Solo se guarda la frecuencia de los términos que alguna pregunta usa:
    un índice completo de 68 millones de tokens no cabe en memoria y no
    hace falta para esto. La longitud total sí se cuenta entera, porque es
    lo que BM25 usa para normalizar.
    """
    terminos = set(terminos)
    tf, df, urls, longitudes = {}, {}, {}, {}
    for carpeta, _, ficheros in os.walk(dir_docs):
        for fichero in ficheros:
            if not fichero.endswith(".md"):
                continue
            ruta = os.path.join(carpeta, fichero)
            with open(ruta, encoding="utf-8", errors="replace") as fh:
                texto = fh.read()
            m = _URL.search(texto[:500])
            urls[ruta] = m.group(1) if m else ruta
            palabras = tokenizar(texto)
            longitudes[ruta] = len(palabras)
            propias = {}
            for palabra in palabras:
                if palabra in terminos:
                    propias[palabra] = propias.get(palabra, 0) + 1
            if propias:
                tf[ruta] = propias
                for palabra in propias:
                    df[palabra] = df.get(palabra, 0) + 1
    return tf, df, urls, longitudes


def puntuar(terminos, tf, df, longitudes, total_docs):
    """BM25, ordenado de mayor a menor.

    El primer intento fue tf-idf a secas y daba una medida enganosa: sin
    normalizar por longitud gana el documento mas largo, y la pagina exacta
    de `docs/axl/authentication/` quedaba en el puesto 307 por detras de
    apendices de cientos de miles de palabras que mencionan "authentication"
    de pasada. Una metrica asi habria mandado a buscar un problema de
    cobertura que no existe.
    """
    media = (sum(longitudes.values()) / len(longitudes)) if longitudes else 1
    idf = {t: math.log(1 + (total_docs - df.get(t, 0) + 0.5)
                       / (df.get(t, 0) + 0.5)) for t in terminos}
    puntuadas = []
    for ruta, propias in tf.items():
        norma = K1 * (1 - B + B * longitudes.get(ruta, 0) / media)
        s = 0.0
        for t in terminos:
            f = propias.get(t, 0)
            if f:
                s += idf[t] * f * (K1 + 1) / (f + norma)
        if s > 0:
            puntuadas.append((s, ruta))
    puntuadas.sort(key=lambda par: (-par[0], par[1]))
    return puntuadas


def posicion_esperada(ranking, urls, patron):
    """Posición (empezando en 1) del primer documento cuya URL casa.

    None si ninguno casa: el corpus no tiene el documento, o la búsqueda
    léxica no lo saca por ningún sitio. Las dos cosas son un fallo.
    """
    regex = re.compile(patron, re.I)
    for i, (_, ruta) in enumerate(ranking, start=1):
        if regex.search(urls.get(ruta, "")):
            return i
    return None


def evaluar(preguntas, dir_docs=DIR_DOCS, top=5):
    todos = [t for p in preguntas for t in tokenizar(p["pregunta"])]
    tf, df, urls, longitudes = indexar(dir_docs, todos)
    total = max(len(urls), 1)

    resultados = []
    for p in preguntas:
        ranking = puntuar(tokenizar(p["pregunta"]), tf, df, longitudes, total)
        pos = posicion_esperada(ranking, urls, p["url_esperada"])
        resultados.append({
            "pregunta": p["pregunta"],
            "url_esperada": p["url_esperada"],
            "posicion": pos,
            "acierto": pos is not None and pos <= top,
            "primero": urls.get(ranking[0][1], "") if ranking else "",
        })
    return resultados, total


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--preguntas", default=PREGUNTAS)
    ap.add_argument("--top", type=int, default=5,
                    help="posicion maxima que cuenta como acierto")
    args = ap.parse_args()

    with open(args.preguntas, encoding="utf-8") as fh:
        preguntas = json.load(fh)["preguntas"]

    resultados, total = evaluar(preguntas, top=args.top)
    aciertos = sum(1 for r in resultados if r["acierto"])

    print(f"Corpus: {total} documentos · {len(resultados)} preguntas "
          f"· acierto en top {args.top}\n")
    for r in resultados:
        pos = r["posicion"]
        marca = "OK  " if r["acierto"] else ("#%-3d" % pos if pos else "--  ")
        print(f"{marca} {r['pregunta']}")
        if not r["acierto"]:
            print(f"       esperaba: {r['url_esperada']}")
            print(f"       primero:  {r['primero']}")

    print(f"\nAciertos: {aciertos}/{len(resultados)} "
          f"({100 * aciertos // max(len(resultados), 1)}%)")
    # Sin codigo de salida distinto de cero: esto es una medida, no una
    # puerta. Convertirlo en fallo de CI obligaria a fijar un umbral antes
    # de saber cual es el valor normal.
    return 0


if __name__ == "__main__":
    sys.exit(main())
