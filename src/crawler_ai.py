import os
import asyncio
import re
import xml.etree.ElementTree as ET
import requests
from crawl4ai import AsyncWebCrawler, CacheMode

def sanitize_filename(url):
    clean = re.sub(r'https?://', '', url)
    clean = re.sub(r'[^a-zA-Z0-9]', '_', clean)
    return clean[:100] + ".md"

def expand_sitemap(url):
    if not url.endswith(".xml"):
        return [url]
    try:
        print(f"Expandiendo sitemap: {url}")
        resp = requests.get(url, timeout=15)
        if resp.status_code == 200:
            root = ET.fromstring(resp.content)
            namespaces = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
            locs = [loc.text for loc in root.findall('.//ns:loc', namespaces)]
            if not locs:
                locs = [loc.text for loc in root.findall('.//{*}loc')]
            print(f"Encontradas {len(locs)} URLs en el sitemap.")
            return locs[:30] # Límite de seguridad por ejecución
    except Exception as e:
        print(f"Error procesando sitemap {url}: {e}")
    return [url]

async def crawl_urls():
    output_dir = "docs"
    os.makedirs(output_dir, exist_ok=True)
    
    if not os.path.exists("urls.txt"):
        print("El archivo urls.txt no existe.")
        return

    with open("urls.txt", "r") as f:
        raw_inputs = [line.strip() for line in f if line.strip() and not line.startswith("#")]

    urls = []
    for item in raw_inputs:
        urls.extend(expand_sitemap(item))

    async with AsyncWebCrawler(verbose=True) as crawler:
        for url in urls:
            print(f"Procesando: {url}")
            try:
                result = await crawler.arun(
                    url=url,
                    word_count_threshold=15,
                    exclude_external_links=True,
                    remove_overlay_elements=True,
                    process_iframes=True,
                    cache_mode=CacheMode.BYPASS,
                    magic=True,
                    css_selector="main, article, .content, #main-content"
                )
                if result.success and result.markdown:
                    filename = os.path.join(output_dir, sanitize_filename(url))
                    with open(filename, "w", encoding="utf-8") as md_file:
                        md_file.write(result.markdown)
                    print(f"Guardado exitosamente: {filename}")
                else:
                    print(f"Error o contenido vacío en {url}")
            except Exception as e:
                print(f"Excepción crítica en {url}: {str(e)}")

if __name__ == "__main__":
    asyncio.run(crawl_urls())
    
