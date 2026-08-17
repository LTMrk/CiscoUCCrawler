"""
openapi_render.py — Conversión de una operación OpenAPI a documento RAG.

QUÉ SE EXTRAE Y POR QUÉ
-----------------------
El extractor anterior solo leía `content[mime].example` (singular). Auditando
los specs contra lo que define OpenAPI 3, faltaba:

  examples (plural)   Mapa de ejemplos con nombre: {nombre: {value, summary}}.
                      Es la forma que usa OpenAPI 3; la singular es legado.
                      Perder esto es perder los payloads reales.

  ejemplos de respuesta   Solo se extraía el ESQUEMA de la respuesta, nunca un
                      payload. "¿Qué me devuelve este endpoint?" es una de las
                      preguntas más frecuentes y no se podía responder.

  scopes de OAuth     security: [{oauth2: ["spark:people_read"]}] — se listaba
                      el nombre del esquema y se DESCARTABA la lista de scopes.
                      En Webex el scope es justo lo que el desarrollador
                      necesita saber para que la llamada no devuelva 403.

  deprecated: true    Sin esto el agente recomienda endpoints retirados con
                      total confianza. Va también al front matter para poder
                      filtrarlo antes de la búsqueda vectorial.

  respuestas 4xx/5xx  Solo se aplanaba el esquema de las 2xx. Para consultas de
                      troubleshooting (un objetivo declarado del proyecto) la
                      forma del error y sus códigos son lo relevante.

  enum/default/format en parámetros   Se capturaba enum en el cuerpo pero no en
                      los parámetros de query o path.

  readOnly            Una propiedad readOnly no puede enviarse en la petición.
                      Es fuente habitual de errores 400.

  curl sintetizado    No está en el spec, pero es derivable de método + ruta +
                      parámetros + cuerpo. Para un agente técnico un ejemplo
                      ejecutable vale más que la descripción del esquema.
"""

import json

MAX_LINEAS_SCHEMA = 60
MAX_CHARS_EJEMPLO = 1500


def resolver_ref(spec, ref, profundidad=0):
    """Resuelve un $ref local (#/components/...). Corta a profundidad 6 para
    no colgarse en esquemas recursivos, comunes en definiciones grandes."""
    if profundidad > 6 or not isinstance(ref, str) or not ref.startswith("#/"):
        return {}
    nodo = spec
    for parte in ref[2:].split("/"):
        if not isinstance(nodo, dict) or parte not in nodo:
            return {}
        nodo = nodo[parte]
    return nodo


def _deref(spec, nodo):
    if isinstance(nodo, dict) and "$ref" in nodo:
        return resolver_ref(spec, nodo["$ref"])
    return nodo if isinstance(nodo, dict) else {}


def describir_schema(spec, schema, profundidad=0, visitados=None):
    """Aplana un esquema a líneas legibles. El objetivo no es reconstruir el
    JSON Schema sino producir texto que se embeba bien."""
    if visitados is None:
        visitados = set()
    if not isinstance(schema, dict) or profundidad > 4:
        return []

    if "$ref" in schema:
        ref = schema["$ref"]
        if ref in visitados:
            return [f"{'  ' * profundidad}- (referencia circular a {ref.split('/')[-1]})"]
        visitados = visitados | {ref}
        schema = resolver_ref(spec, ref)

    # Composición: allOf / oneOf / anyOf
    for clave, etiqueta in (("allOf", "todos de"), ("oneOf", "uno de"), ("anyOf", "cualquiera de")):
        if clave in schema:
            lineas = [f"{'  ' * profundidad}- ({etiqueta}:)"]
            for sub in schema[clave][:5]:
                lineas += describir_schema(spec, sub, profundidad + 1, visitados)
            return lineas

    if schema.get("type") == "array" and "items" in schema:
        lineas = [f"{'  ' * profundidad}- (array de:)"]
        return lineas + describir_schema(spec, schema["items"], profundidad + 1, visitados)

    obligatorios = set(schema.get("required", []))
    lineas = []
    for nombre, prop in (schema.get("properties") or {}).items():
        p = _deref(spec, prop)
        tipo = p.get("type", "object")
        fmt = p.get("format")
        if fmt:
            tipo = f"{tipo}/{fmt}"

        marcas = []
        if nombre in obligatorios:
            marcas.append("**requerido**")
        if p.get("readOnly"):
            # No puede enviarse en la peticion: causa comun de HTTP 400.
            marcas.append("solo lectura")
        if p.get("writeOnly"):
            marcas.append("solo escritura")
        if p.get("deprecated"):
            marcas.append("DEPRECADO")
        sufijo = f" ({', '.join(marcas)})" if marcas else ""

        desc = (p.get("description") or "").strip().replace("\n", " ")
        extras = []
        if p.get("enum"):
            extras.append(f"Valores: {', '.join(map(str, p['enum'][:15]))}.")
        if p.get("default") is not None:
            extras.append(f"Por defecto: {p['default']}.")
        if p.get("maxLength"):
            extras.append(f"Long. max: {p['maxLength']}.")
        extra = (" " + " ".join(extras)) if extras else ""

        lineas.append(
            f"{'  ' * profundidad}- `{nombre}` ({tipo}){sufijo}: {desc}{extra}".rstrip())

        if p.get("type") == "object" or "properties" in p:
            lineas += describir_schema(spec, p, profundidad + 1, visitados)
        elif p.get("type") == "array" and "items" in p:
            lineas += describir_schema(spec, p["items"], profundidad + 1, visitados)

    return lineas


def extraer_ejemplos(spec, definicion_contenido):
    """Recoge ejemplos tanto de `example` (legado) como de `examples` (mapa
    con nombre, la forma de OpenAPI 3). Devuelve [(etiqueta, payload)]."""
    salida = []
    if not isinstance(definicion_contenido, dict):
        return salida

    if definicion_contenido.get("example") is not None:
        salida.append(("Ejemplo", definicion_contenido["example"]))

    for nombre, ej in (definicion_contenido.get("examples") or {}).items():
        ej = _deref(spec, ej)
        valor = ej.get("value")
        if valor is None:
            continue
        etiqueta = ej.get("summary") or nombre
        salida.append((etiqueta, valor))

    # Algunos specs ponen el ejemplo dentro del propio esquema.
    esquema = _deref(spec, definicion_contenido.get("schema") or {})
    if not salida and esquema.get("example") is not None:
        salida.append(("Ejemplo", esquema["example"]))

    return salida


def _bloque_json(valor):
    try:
        texto = json.dumps(valor, indent=2, ensure_ascii=False)
    except (TypeError, ValueError):
        texto = str(valor)
    if len(texto) > MAX_CHARS_EJEMPLO:
        texto = texto[:MAX_CHARS_EJEMPLO] + "\n  ... (truncado)"
    return f"```json\n{texto}\n```"


def extraer_scopes(spec, operacion):
    """Devuelve (esquemas, scopes). Los scopes de OAuth son lo que determina
    si la llamada devuelve 200 o 403; el extractor anterior los descartaba."""
    seguridad = operacion.get("security")
    if seguridad is None:
        seguridad = spec.get("security") or []
    esquemas, scopes = [], []
    for bloque in seguridad:
        if not isinstance(bloque, dict):
            continue
        for nombre, lista in bloque.items():
            esquemas.append(nombre)
            if isinstance(lista, list):
                scopes.extend(lista)
    return sorted(set(esquemas)), sorted(set(scopes))


def sintetizar_curl(base, ruta, metodo, parametros, esquema_cuerpo, spec):
    """Genera una invocación ejecutable. No está en el spec, pero es derivable
    y para un agente técnico vale más que la descripción del esquema."""
    ruta_final = ruta
    query = []
    for p in parametros:
        sitio = p.get("in")
        nombre = p.get("name", "")
        if sitio == "path":
            ruta_final = ruta_final.replace("{" + nombre + "}", f"<{nombre}>")
        elif sitio == "query" and p.get("required"):
            query.append(f"{nombre}=<{nombre}>")

    url = f"{base}{ruta_final}"
    if query:
        url += "?" + "&".join(query)

    lineas = [f"curl -X {metodo.upper()} '{url}' \\",
              "  -H 'Authorization: Bearer <TOKEN>' \\"]

    if esquema_cuerpo:
        esquema = _deref(spec, esquema_cuerpo)
        obligatorios = esquema.get("required", [])
        cuerpo = {}
        for nombre in obligatorios[:6]:
            prop = _deref(spec, (esquema.get("properties") or {}).get(nombre, {}))
            tipo = prop.get("type", "string")
            cuerpo[nombre] = {
                "string": f"<{nombre}>", "integer": 0, "number": 0,
                "boolean": True, "array": [], "object": {},
            }.get(tipo, f"<{nombre}>")
        lineas.append("  -H 'Content-Type: application/json' \\")
        lineas.append(f"  -d '{json.dumps(cuerpo, ensure_ascii=False)}'")
    else:
        lineas[-1] = lineas[-1].rstrip(" \\")

    return "```bash\n" + "\n".join(lineas) + "\n```"


def operacion_a_markdown(spec, nombre_api, ruta, metodo, operacion):
    """Documento autocontenido para una operación."""
    info = spec.get("info") or {}
    servidores = spec.get("servers") or []
    base = servidores[0].get("url", "") if servidores else ""
    deprecado = bool(operacion.get("deprecated"))
    esquemas_sec, scopes = extraer_scopes(spec, operacion)

    partes = [f"# {metodo.upper()} {ruta}", ""]

    if deprecado:
        # Primera linea del cuerpo a proposito: si el chunker corta, esto
        # sobrevive. Un agente que recomienda endpoints retirados es peor
        # que uno que no responde.
        partes += ["> **ENDPOINT DEPRECADO.** No usar en integraciones nuevas.", ""]

    partes.append(f"**API:** {nombre_api}")
    if operacion.get("tags"):
        partes.append(f"**Área:** {', '.join(operacion['tags'])}")
    if operacion.get("operationId"):
        partes.append(f"**operationId:** `{operacion['operationId']}`")
    if base:
        partes.append(f"**URL base:** `{base}`")
    if scopes:
        partes.append(f"**Scopes requeridos:** {', '.join(f'`{s}`' for s in scopes)}")
    elif esquemas_sec:
        partes.append(f"**Autenticación:** {', '.join(esquemas_sec)}")

    if operacion.get("summary"):
        partes += ["", "## Resumen", operacion["summary"]]
    if operacion.get("description"):
        partes += ["", "## Descripción", operacion["description"].strip()]

    # Parámetros
    parametros = [_deref(spec, p) for p in (operacion.get("parameters") or [])]
    if parametros:
        partes += ["", "## Parámetros"]
        for p in parametros:
            esquema_p = _deref(spec, p.get("schema") or {})
            tipo = esquema_p.get("type", "")
            if esquema_p.get("format"):
                tipo = f"{tipo}/{esquema_p['format']}"
            marcas = []
            if p.get("required"):
                marcas.append("**requerido**")
            if p.get("deprecated"):
                marcas.append("DEPRECADO")
            sufijo = f" ({', '.join(marcas)})" if marcas else ""
            desc = (p.get("description") or "").strip().replace("\n", " ")
            extras = []
            if esquema_p.get("enum"):
                extras.append(f"Valores: {', '.join(map(str, esquema_p['enum'][:15]))}.")
            if esquema_p.get("default") is not None:
                extras.append(f"Por defecto: {esquema_p['default']}.")
            extra = (" " + " ".join(extras)) if extras else ""
            partes.append(
                f"- `{p.get('name','?')}` [{p.get('in','?')}] ({tipo}){sufijo}: {desc}{extra}".rstrip())

    # Cuerpo de la petición
    esquema_cuerpo = None
    body = _deref(spec, operacion.get("requestBody") or {})
    for tipo_mime, definicion in (body.get("content") or {}).items():
        esquema = definicion.get("schema") or {}
        esquema_cuerpo = esquema_cuerpo or esquema
        lineas = describir_schema(spec, esquema)
        if lineas:
            partes += ["", f"## Cuerpo de la petición ({tipo_mime})"]
            partes += lineas[:MAX_LINEAS_SCHEMA]
        for etiqueta, valor in extraer_ejemplos(spec, definicion):
            partes += ["", f"### {etiqueta} — petición", _bloque_json(valor)]

    # Ejemplo ejecutable
    partes += ["", "## Ejemplo de invocación",
               sintetizar_curl(base, ruta, metodo, parametros, esquema_cuerpo, spec)]

    # Respuestas: exito y error por separado. El extractor anterior solo
    # aplanaba las 2xx, justo al reves de lo que necesita troubleshooting.
    respuestas = operacion.get("responses") or {}
    exitosas = {k: v for k, v in respuestas.items() if str(k).startswith("2")}
    errores = {k: v for k, v in respuestas.items() if not str(k).startswith("2")}

    if exitosas:
        partes += ["", "## Respuestas correctas"]
        for codigo, definicion in sorted(exitosas.items(), key=lambda kv: str(kv[0])):
            d = _deref(spec, definicion)
            partes.append(f"**{codigo}**: {(d.get('description') or '').strip()}")
            for _mime, cont in (d.get("content") or {}).items():
                lineas = describir_schema(spec, cont.get("schema") or {})
                partes += lineas[:MAX_LINEAS_SCHEMA]
                for etiqueta, valor in extraer_ejemplos(spec, cont):
                    partes += ["", f"### {etiqueta} — respuesta {codigo}", _bloque_json(valor)]
            for nombre_h, h in (d.get("headers") or {}).items():
                hd = _deref(spec, h)
                partes.append(f"- Cabecera `{nombre_h}`: "
                              f"{(hd.get('description') or '').strip()}")

    if errores:
        partes += ["", "## Respuestas de error"]
        for codigo, definicion in sorted(errores.items(), key=lambda kv: str(kv[0])):
            d = _deref(spec, definicion)
            partes.append(f"- **{codigo}**: {(d.get('description') or '').strip()}")
            for _mime, cont in (d.get("content") or {}).items():
                for etiqueta, valor in extraer_ejemplos(spec, cont)[:1]:
                    partes += [f"  {etiqueta}:", _bloque_json(valor)]

    if operacion.get("externalDocs", {}).get("url"):
        partes += ["", f"**Documentación adicional:** "
                       f"{operacion['externalDocs']['url']}"]

    contexto_api = (info.get("description") or "").strip()
    if contexto_api:
        partes += ["", "## Contexto de la API",
                   contexto_api[:600] + ("..." if len(contexto_api) > 600 else "")]

    partes += ["", "---",
               "> Fuente: webex/webex-openapi-specs (Cisco), licencia CC BY 4.0.\n"
               "> https://github.com/webex/webex-openapi-specs"]

    return "\n".join(partes), {"deprecated": deprecado, "scopes": scopes}
