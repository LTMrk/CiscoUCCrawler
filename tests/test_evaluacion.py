"""Pruebas de tools/evaluar_corpus.py.

La que importa es `test_gana_la_pagina_corta_y_exacta`. El primer intento
de esta herramienta puntuaba con tf-idf a secas, sin normalizar por
longitud, y la pagina exacta de `docs/axl/authentication/` quedaba en el
puesto 307 por detras de apendices enormes que mencionan "authentication"
de pasada. La medida decia 4 aciertos de 12 cuando la realidad eran 11:
habria mandado a buscar un problema de cobertura inexistente. Una metrica
equivocada es peor que no tener metrica, porque se la cree uno.
"""
import os
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "tools"))

import evaluar_corpus as ev


def _corpus(directorio, documentos):
    """documentos: {nombre: (url, texto)}."""
    for nombre, (url, texto) in documentos.items():
        with open(os.path.join(directorio, nombre + ".md"), "w",
                  encoding="utf-8") as fh:
            fh.write(f"---\nsource_url: {url}\n---\n\n{texto}\n")


def test_tokenizar_parte_por_no_alfanumerico_y_descarta_lo_de_una_letra():
    # El "5" de "v12.5" se pierde por la regla de dos caracteres. Se acepta:
    # las versiones aparecen en los documentos como 12_5, 1251 o 12-5, no
    # como tokens sueltos, asi que recuperarlo no compraria nada.
    assert ev.tokenizar("AXL addPhone, v12.5") == ["axl", "addphone", "v12"]
    # Una sola letra nunca discrimina y ensucia el idf.
    assert ev.tokenizar("a b de 1") == ["de"]


def test_gana_la_pagina_corta_y_exacta():
    # El apendice repite los terminos MAS veces que la pagina exacta: es el
    # unico caso en que la normalizacion por longitud decide. Si se pone
    # B = 0, gana el apendice, que es justo la regresion que se busca.
    with tempfile.TemporaryDirectory() as d:
        # Hacen falta documentos de tamano corriente: BM25 normaliza contra
        # la longitud MEDIA, y con solo dos documentos el apendice arrastra
        # la media hacia si mismo y deja de estar penalizado. En el corpus
        # real la media son unas 4.350 palabras sobre 15.806 documentos.
        documentos = {f"normal{i}": (f"https://x/normal{i}/", "texto comun " * 100)
                      for i in range(18)}
        documentos["exacta"] = ("https://x/docs/axl/authentication/",
                                "AXL authentication basic credentials")
        documentos["apendice"] = ("https://x/guia/apendice/",
                                  "axl authentication " * 20
                                  + "relleno irrelevante " * 4000)
        _corpus(d, documentos)
        tf, df, urls, largos = ev.indexar(d, ["axl", "authentication"])
        ranking = ev.puntuar(["axl", "authentication"], tf, df, largos, len(urls))
        assert urls[ranking[0][1]].endswith("/docs/axl/authentication/"), \
            f"gana el documento largo: {urls[ranking[0][1]]}"


def test_un_termino_en_todos_los_documentos_no_decide():
    # "cisco" esta en los 15.806 documentos del corpus real y no distingue
    # nada; "finesse" esta en veinticinco y lo dice todo. Aqui a escala.
    #
    # El caso esta montado para que SOLO el idf pueda decidirlo. Los dos
    # candidatos miden lo mismo, asi que la normalizacion por longitud no
    # interviene; cada uno trae un unico termino de la consulta, asi que
    # tampoco decide el numero de terminos distintos; y el que trae el
    # comun lo repite diez veces, o sea que gana en frecuencia bruta. Si el
    # idf se vuelve constante, gana ese, que es la regresion buscada.
    #
    # Las URL no llevan los terminos: la cabecera del documento tambien se
    # tokeniza, y un "finesse" colado en la URL falsearia el recuento.
    with tempfile.TemporaryDirectory() as d:
        documentos = {f"relleno{i}": (f"https://x/r{i}/", "cisco " + "texto " * 60)
                      for i in range(18)}
        documentos["raro"] = ("https://x/a/", "finesse " + "texto " * 60)
        documentos["comun"] = ("https://x/b/", "cisco " * 10 + "texto " * 51)
        _corpus(d, documentos)
        tf, df, urls, largos = ev.indexar(d, ["cisco", "finesse"])
        assert df["cisco"] == 19 and df["finesse"] == 1, df
        ranking = ev.puntuar(["cisco", "finesse"], tf, df, largos, len(urls))
        assert urls[ranking[0][1]] == "https://x/a/", \
            f"decide el termino comun: {urls[ranking[0][1]]}"


def test_posicion_esperada_devuelve_el_primero_que_casa():
    urls = {"a": "https://x/uno/", "b": "https://x/dos/", "c": "https://x/tres/"}
    ranking = [(3.0, "a"), (2.0, "b"), (1.0, "c")]
    assert ev.posicion_esperada(ranking, urls, "dos") == 2
    assert ev.posicion_esperada(ranking, urls, "uno|tres") == 1


def test_posicion_esperada_sin_coincidencia_es_none():
    # No es 0 ni -1: None obliga al llamante a distinguir "no esta" de
    # "esta el primero", que es justo donde se cuelan los off-by-one.
    urls = {"a": "https://x/uno/"}
    assert ev.posicion_esperada([(1.0, "a")], urls, "nada") is None


def test_evaluar_de_punta_a_punta():
    with tempfile.TemporaryDirectory() as d:
        _corpus(d, {
            "buena": ("https://x/docs/axl/", "AXL addPhone creates a phone"),
            "otra": ("https://x/docs/webex/", "Webex meetings"),
        })
        preguntas = [
            {"pregunta": "AXL addPhone", "url_esperada": "docs/axl"},
            {"pregunta": "algo que no existe en ningun documento",
             "url_esperada": "docs/axl"},
        ]
        resultados, total = ev.evaluar(preguntas, dir_docs=d, top=1)
        assert total == 2
        assert resultados[0]["acierto"] is True
        assert resultados[0]["posicion"] == 1
        assert resultados[1]["acierto"] is False


def test_el_fichero_de_preguntas_del_repo_es_coherente():
    import json
    import re
    ruta = os.path.join(RAIZ, "evaluacion", "preguntas.json")
    with open(ruta, encoding="utf-8") as fh:
        preguntas = json.load(fh)["preguntas"]
    assert len(preguntas) >= 5, "menos de cinco preguntas no mide nada"
    for p in preguntas:
        assert p["pregunta"].strip(), p
        # Una regex mal escrita convertiria la pregunta en un fallo
        # permanente sin decir por que.
        re.compile(p["url_esperada"])
        assert ev.tokenizar(p["pregunta"]), f"pregunta sin terminos: {p}"


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
