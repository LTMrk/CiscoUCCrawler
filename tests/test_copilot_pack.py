"""Prueba el reempaquetado de docs/ para agentes de M365 Copilot."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))), "src"))

from copilot_pack import (
    LIMITE_CHARS,
    PERFILES,
    a_texto_plano,
    clasificar_producto,
    clave_version,
    PERFIL_POR_DEFECTO,
    comprimir_todo,
    construir_parser,
    empaquetar,
    encabezado,
    escribir_guia,
    etiqueta_version,
    familia_documental,
    marcar_vigencia,
    render_paquete,
)


# ---------------------------------------------------------------------------
# Clasificacion por producto
# ---------------------------------------------------------------------------

def test_clasificacion_por_producto():
    casos = [
        ("https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/15/x.html", "cucm"),
        ("https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/y.html", "cuc"),
        ("https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/z.html", "expressway"),
        ("https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/vcr4/a.html", "cube"),
        ("https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/"
         "contact_center/crs/express_15_0/b.html", "uccx"),
        ("https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/"
         "contact_center/icm_enterprise/icm_enterprise_15_0_1/c.html", "ucce"),
    ]
    for url, esperado in casos:
        assert clasificar_producto(url) == esperado, url


def test_clasificacion_devnet():
    """Los doc-sets de developer.cisco.com se integran en el producto al que
    pertenecen, no en un bucket aparte: la referencia de API de AXL va con la
    documentacion de CUCM porque es lo que el agente necesita a la vez.

    Sin DOCSETS_DEVNET la mayoria caeria en "misc", porque las regex de
    PRODUCTOS estan escritas sobre rutas de www.cisco.com.
    """
    casos = [
        # Los que NO casaban con ninguna regex previa.
        ("https://developer.cisco.com/docs/axl/axl-developer-guide/", "cucm"),
        ("https://developer.cisco.com/docs/contact-center-express/"
         "cti-protocol-overview/", "uccx"),
        ("https://developer.cisco.com/docs/ios-xe-voip/", "cube"),
        ("https://developer.cisco.com/docs/cer-config/", "cuc"),
        ("https://developer.cisco.com/site/roomdevices/", "endpoints"),
        ("https://developer.cisco.com/site/webdialer/", "cucm"),
        ("https://developer.cisco.com/site/tapi/", "cucm"),
        # Los que ya casaban: el mapeo nuevo no debe desviarlos.
        ("https://developer.cisco.com/docs/finesse/rest-api-dev-guide/", "cvp"),
        ("https://developer.cisco.com/docs/customer-voice-portal/", "cvp"),
        ("https://developer.cisco.com/docs/packaged-contact-center/"
         "api-dev-guide/", "ucce"),
        ("https://developer.cisco.com/docs/enterprise-chat-and-email/", "ucce"),
        ("https://developer.cisco.com/docs/jabber-bots/", "impresence"),
        ("https://developer.cisco.com/site/unity-connection/documentation/",
         "cuc"),
    ]
    for url, esperado in casos:
        assert clasificar_producto(url) == esperado, \
            f"{url} -> {clasificar_producto(url)}, esperado {esperado}"


def test_devnet_no_altera_cisco_com():
    """El gancho de DevNet se activa solo para developer.cisco.com. Si tocara
    el resto, reclasificaria los 12.000 documentos ya empaquetados."""
    casos = [
        ("https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/15/x.html",
         "cucm"),
        ("https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/"
         "contact_center/finesse/finesse_1251/y.html", "cvp"),
        ("https://help.webex.com/en-us/article/abc/z", "webexcloud"),
    ]
    for url, esperado in casos:
        assert clasificar_producto(url) == esperado, url


def test_impresence_gana_a_cucm():
    """im_presence vive bajo /cucm/ pero es un producto distinto: su regex debe
    evaluarse antes o todo IM&P acabaria en el agente de CUCM."""
    url = ("https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/"
           "im_presence/configAdminGuide/12_5_1_su4/guia.html")
    assert clasificar_producto(url) == "impresence"


# ---------------------------------------------------------------------------
# Familias documentales y versiones
# ---------------------------------------------------------------------------

def test_familia_ignora_la_version():
    base = "https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/"
    a = familia_documental(base + "12_5_1SU4/systemConfig/cucm_b_system-config-1251su4.html")
    b = familia_documental(base + "15/systemConfig/cucm_b_system-config-15.html")
    assert a == b


def test_familia_ignora_el_separador():
    """Cisco alterna guion bajo y guion medio entre releases del mismo libro."""
    raiz = ("https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/"
            "contact_center/icm_enterprise/")
    a = familia_documental(raiz + "icm_enterprise_12_6_1/reference/guide/"
                                  "ucce_b_database-schema-guide.html")
    b = familia_documental(raiz + "icm_enterprise_15_0_1/reference/guide/"
                                  "ucce-b-database-schema-guide.html")
    assert a == b


def test_orden_de_version_pone_la_mas_alta_primero():
    v15 = clave_version("https://x/td/docs/voice_ip_comm/cucm/admin/15/g.html")
    v1251 = clave_version("https://x/td/docs/voice_ip_comm/cucm/admin/12_5_1SU4/g.html")
    assert v15 > v1251


def test_etiqueta_de_version_legible():
    assert etiqueta_version("https://x/cucm/admin/12_5_1/g.html") == "12.5.1"
    assert etiqueta_version("https://x/expressway/admin_guide/X15-5/g.html") == "X15-5"
    assert etiqueta_version("https://x/cucm/admin/14SU2/adminGd/g.html") == "14SU2"


def test_version_embebida_en_el_nombre_del_arbol():
    """Contact Center no usa un segmento propio para la version: la pega al
    nombre del arbol. Sin cubrirlo, esos capitulos salen sin version."""
    casos = [
        ("https://x/cust_contact/contact_center/icm_enterprise/"
         "icm_enterprise_15_0_1/g.html", "15.0.1"),
        ("https://x/cust_contact/contact_center/crs/express_12_5_1_su1/g.html",
         "12.5.1SU1"),
        ("https://x/cust_contact/contact_center/finesse/finesse_1501/g.html", "1501"),
    ]
    for url, esperado in casos:
        assert etiqueta_version(url) == esperado, url


def test_modelos_de_telefono_no_se_confunden_con_version():
    """`7821_7841_7861` son modelos, no una release: la version real es /10_1/."""
    url = "https://x/voice_ip_comm/cuipph/7821_7841_7861/10_1/english/g.html"
    assert etiqueta_version(url) == "10.1"


def test_modelo_suelto_de_cuatro_digitos_no_es_version():
    """Los arboles de telefonos usan /7832/, /8832/, /6800/ como segmento. Sin
    prefijo alfabetico no puede tomarse por una release: el inventario acababa
    listando 7832 y 8832 como si fueran versiones de producto."""
    for modelo in ("7832", "8832", "6800", "8845", "191"):
        url = f"https://x/voice_ip_comm/cuipph/{modelo}/english/g.html"
        assert etiqueta_version(url) == "", modelo


def test_version_condensada_solo_con_prefijo():
    """`finesse_1501` si es una release; el prefijo lo garantiza."""
    assert etiqueta_version("https://x/contact_center/finesse/finesse_1501/g.html") == "1501"


def test_guiones_y_guiones_bajos_dan_la_misma_version():
    """Sin normalizar, `15-0-1` y `15_0_1` figuraban como dos versiones
    distintas en el inventario del RAG."""
    a = etiqueta_version("https://x/contact_center/customer_voice_portal/15-0-1/g.html")
    b = etiqueta_version("https://x/contact_center/customer_voice_portal/15_0_1/g.html")
    assert a == b == "15.0.1"


def test_expressway_conserva_su_notacion_con_guion():
    """Expressway se nombra oficialmente X15-5, no X15.5."""
    assert etiqueta_version("https://x/expressway/admin_guide/X15-5/g.html") == "X15-5"


def test_documento_sin_version_no_inventa_una():
    url = ("https://www.cisco.com/c/en/us/support/docs/collaboration-endpoints/"
           "ip-phone-7800-series/200850-Troubleshoot-Cisco-Phone.html")
    assert etiqueta_version(url) == ""


def test_marcar_vigencia_deja_una_sola_vigente_por_familia():
    def doc(url, texto):
        return {"producto": "cucm", "familia": familia_documental(url),
                "orden": clave_version(url), "texto": texto, "url": url}

    base = "https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/"
    cuerpo = ("Configure the dial plan on the cluster. " * 40)
    docs = [
        doc(base + "12_5_1/systemConfig/g.html", cuerpo),
        doc(base + "14/systemConfig/g.html", cuerpo),
        doc(base + "15/systemConfig/g.html", cuerpo),
    ]
    marcar_vigencia(docs)
    vigentes = [d for d in docs if d["vigencia"] == "vigente"]
    assert len(vigentes) == 1
    assert "/15/" in vigentes[0]["url"]


def test_vigencia_detecta_duplicado_aunque_cambie_el_slug():
    """El renombrado de slug entre releases se caza por contenido, no por ruta."""
    def doc(url, texto):
        return {"producto": "ucce", "familia": familia_documental(url),
                "orden": clave_version(url), "texto": texto, "url": url}

    cuerpo = ("The database schema stores call detail records for each agent. " * 60)
    docs = [
        doc("https://x/td/docs/voice_ip_comm/cust_contact/contact_center/"
            "icm_enterprise/icm_enterprise_12_6_1/reference/guide/"
            "ucce_b_database-schema-handbook.html", cuerpo),
        doc("https://x/td/docs/voice_ip_comm/cust_contact/contact_center/"
            "icm_enterprise/icm_enterprise_15_0_1/reference/guide/"
            "ucce-b-database-schema-guide-150.html", cuerpo),
    ]
    marcar_vigencia(docs)
    assert [d["vigencia"] for d in docs].count("vigente") == 1


# ---------------------------------------------------------------------------
# Conversion a texto plano
# ---------------------------------------------------------------------------

def test_frontmatter_fuera():
    md = "---\ndoc_id: x\nsource_url: https://y\n---\n\nTexto util del documento."
    assert "doc_id" not in a_texto_plano(md)
    assert "Texto util" in a_texto_plano(md)


def test_tabla_se_linealiza():
    """Copilot no parsea tablas: en pipes el contenido se pierde."""
    md = ("| Parametro | Valor |\n"
          "|---|---|\n"
          "| Puerto SIP | 5060 |\n"
          "| Transporte | TCP |\n")
    texto = a_texto_plano(md)
    assert "|" not in texto
    assert "Parametro: Puerto SIP; Valor: 5060" in texto
    assert "Parametro: Transporte; Valor: TCP" in texto


def test_tabla_con_celda_multilinea_se_linealiza():
    """Si la ultima celda lleva salto de linea, la fila no cierra con pipe.
    Sin reensamblarla, la fila entera se cuela sin aplanar."""
    md = "\n".join([
        "| Version | Fecha | Cambio |",
        "|---|---|---|",
        "| 2.0 | 26-Feb-2026 | Cambio la informacion",
        "de contexto del documento. |",
    ])
    texto = a_texto_plano(md)
    assert "|" not in texto
    assert "Cambio: Cambio la informacion de contexto del documento." in texto


def test_parrafo_partido_se_reconstruye():
    """El HTML de Cisco mete saltos y tabuladores dentro de las frases."""
    md = "Cisco\n\t\trecommends performing\n           regular backups."
    assert a_texto_plano(md) == "Cisco recommends performing regular backups."


def test_encabezados_pierden_almohadillas_y_no_se_duplican():
    md = "Back Up the System\n\n# Back Up the System\n\nContenido del capitulo."
    texto = a_texto_plano(md)
    assert "#" not in texto
    assert texto.count("Back Up the System") == 1


def test_vinetas_se_conservan_en_lineas_propias():
    md = "- Primera opcion\n- Segunda opcion\n"
    texto = a_texto_plano(md)
    assert texto.splitlines() == ["- Primera opcion", "- Segunda opcion"]


def test_bloque_de_codigo_conserva_el_contenido_sin_valla():
    md = "Ejecute:\n\n```\nutils dbreplication status\n```\n"
    texto = a_texto_plano(md)
    assert "utils dbreplication status" in texto
    assert "```" not in texto


def test_enlaces_e_imagenes_dejan_solo_el_texto():
    md = "Consulte la [guia oficial](https://cisco.com/g) y ![diagrama](x.png)."
    texto = a_texto_plano(md)
    assert "https://cisco.com/g" not in texto
    assert "guia oficial" in texto and "diagrama" in texto


# ---------------------------------------------------------------------------
# Empaquetado
# ---------------------------------------------------------------------------

def _capitulo(libro, indice, chars):
    return {"producto": "cucm", "version": "15", "url": f"https://x/{libro}/{indice:03d}",
            "libro": libro, "titulo": f"Capitulo {indice}",
            "retrieved_at": "2026-08-17T00:00:00+00:00", "texto": "a" * chars}


def test_ningun_paquete_supera_el_limite():
    capitulos = [_capitulo("libro", i, 9_000) for i in range(40)]
    for _, grupo in empaquetar(capitulos, LIMITE_CHARS):
        assert len(render_paquete(grupo)) <= LIMITE_CHARS


def test_capitulo_gigante_se_parte_y_cada_trozo_cabe():
    capitulos = [_capitulo("libro", 0, 200_000)]
    paquetes = empaquetar(capitulos, LIMITE_CHARS)
    assert len(paquetes) > 1
    for _, grupo in paquetes:
        assert len(render_paquete(grupo)) <= LIMITE_CHARS


def test_capitulos_pequenos_se_agrupan():
    """El objetivo es reducir el numero de ficheros, no producir uno por pagina."""
    capitulos = [_capitulo("libro", i, 2_000) for i in range(10)]
    assert len(empaquetar(capitulos, LIMITE_CHARS)) == 1


def test_no_se_mezclan_libros_distintos():
    capitulos = [_capitulo("libro-a", 0, 500), _capitulo("libro-b", 1, 500)]
    assert len(empaquetar(capitulos, LIMITE_CHARS)) == 2


def test_perfil_chat_cabe_en_20_ficheros():
    """En adjuntos de chat el tope es 20 ficheros por conversacion. El perfil
    `chat` debe mezclar libros para no desbordarlo."""
    perfil = PERFILES["chat"]
    # 300 capitulos de 30.000 chars = 9 M, el tamano de cucm/vigente.
    capitulos = [_capitulo(f"libro-{i // 10}", i, 30_000) for i in range(300)]
    paquetes = empaquetar(capitulos, perfil["limite"], perfil["mezclar_libros"])
    assert len(paquetes) <= perfil["max_ficheros"], len(paquetes)
    for _, grupo in paquetes:
        assert len(render_paquete(grupo)) <= perfil["limite"]


def test_perfil_sharepoint_no_mezcla_libros():
    perfil = PERFILES["sharepoint"]
    capitulos = [_capitulo("libro-a", 0, 500), _capitulo("libro-b", 1, 500)]
    paquetes = empaquetar(capitulos, perfil["limite"], perfil["mezclar_libros"])
    assert len(paquetes) == 2


def test_los_dos_perfiles_declaran_lo_que_usa_escribir():
    for nombre, perfil in PERFILES.items():
        assert set(perfil) == {"limite", "max_ficheros", "mezclar_libros"}, nombre
        assert perfil["limite"] > 0


def test_zip_unico_agrupa_todos_los_productos_conservando_la_carpeta():
    """El ZIP final debe ser UNO SOLO (no uno por producto) y mantener el
    producto como carpeta dentro del archivo: si se pierde, al descomprimir no
    hay forma de saber a que tecnologia pertenece cada .txt. Tambien fija que
    el contenido llega intacto (Copilot no lee dentro de un ZIP; esto es
    transporte, y un byte alterado en el transporte se cuela en silencio)."""
    import tempfile, zipfile, shutil
    tmp = tempfile.mkdtemp()
    try:
        for producto in ("cucm", "ucce"):
            destino = os.path.join(tmp, producto, "vigente")
            os.makedirs(destino)
            # newline="" para que el fichero en disco tenga exactamente los
            # bytes escritos: en Windows, "w" sin esto traduce \n a \r\n y la
            # comparacion byte-a-byte de mas abajo fallaria por plataforma,
            # no por un bug real de comprimir_todo().
            with open(os.path.join(destino, "guia.txt"), "w", encoding="utf-8",
                      newline="") as fh:
                fh.write(f"Producto: {producto}\nContenido de {producto}.\n")
        # Lo historico no debe entrar.
        historico = os.path.join(tmp, "cucm", "historico")
        os.makedirs(historico)
        with open(os.path.join(historico, "vieja.txt"), "w", encoding="utf-8",
                  newline="") as fh:
            fh.write("version antigua\n")

        ruta, total, tam = comprimir_todo(tmp)
        assert total == 2 and tam > 0
        # Es EL UNICO zip: no debe haber generado ningun otro fichero en _zips/.
        dir_zips = os.path.join(tmp, "_zips")
        assert os.listdir(dir_zips) == [os.path.basename(ruta)]
        with zipfile.ZipFile(ruta) as z:
            assert sorted(z.namelist()) == ["cucm/guia.txt", "ucce/guia.txt"]
            assert z.read("cucm/guia.txt") == b"Producto: cucm\nContenido de cucm.\n"
            assert b"version antigua" not in b"".join(
                z.read(n) for n in z.namelist())
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def test_perfil_por_defecto_es_chat():
    """Sin licencia de agentes, sharepoint no es una opcion viable: el default
    debe ser lo unico que el usuario puede usar de verdad. Se parsean los
    argumentos reales del parser de main() (sin invocar main, que leeria
    docs/pages del repo), no una copia que pueda divergir."""
    args = construir_parser().parse_args([])
    assert args.perfil == "chat" == PERFIL_POR_DEFECTO


def test_guia_de_chat_no_menciona_agentes():
    """La guia del perfil chat es para quien NO tiene licencia de agentes: no
    debe darle pasos de Agent Builder que no puede seguir."""
    import tempfile, shutil
    tmp = tempfile.mkdtemp()
    try:
        resumen = [("cucm", "vigente", "", 1, 1000, 1, 500)]
        ruta = escribir_guia(tmp, resumen, LIMITE_CHARS, perfil="chat")
        texto = open(ruta, encoding="utf-8").read()
        # Puede citar "Agent Builder" para aclarar que no hace falta, pero no
        # debe darle pasos de configuracion que no puede seguir sin licencia.
        assert "Nuevo agente" not in texto
        assert "Configurar" not in texto
        assert "OneDrive" in texto
        assert "no lee dentro de un" in texto.lower()
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def test_guia_de_sharepoint_menciona_licencia_de_agentes():
    """Al reves: quien use el perfil sharepoint SI tiene licencia de agentes,
    y debe saber que ese perfil la requiere si alguien mas lo reutiliza."""
    import tempfile, shutil
    tmp = tempfile.mkdtemp()
    try:
        resumen = [("cucm", "vigente", "", 1, 1000, 1, 500)]
        ruta = escribir_guia(tmp, resumen, LIMITE_CHARS, perfil="sharepoint")
        texto = open(ruta, encoding="utf-8").read()
        assert "licencia" in texto.lower() and "agentes" in texto.lower()
        assert "Agent Builder" in texto
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def test_encabezado_lleva_producto_version_y_fuente():
    texto = encabezado(_capitulo("libro", 1, 10))
    assert "Producto: Cisco Unified Communications Manager (CUCM)" in texto
    assert "Version: 15" in texto
    assert "Fuente: https://x/libro/001" in texto


if __name__ == "__main__":
    pruebas = [v for k, v in sorted(globals().items())
               if k.startswith("test_") and callable(v)]
    for prueba in pruebas:
        prueba()
        print(f"  OK {prueba.__name__}")
    print(f"\n{len(pruebas)} PRUEBAS PASARON")
