import os
import asyncio
import re
import gzip
import xml.etree.ElementTree as ET
import requests
from crawl4ai import AsyncWebCrawler, CacheMode

def sanitize_filename(url):
    clean = re.sub(r'https?://', '', url)
    clean = re.sub(r'[^a-zA-Z0-9]', '_', clean)
    return clean[:100] + ".md"

def expand_sitemap(url):
    if not url.endswith((".xml", ".gz")):
        return [url]
    try:
        print(f"Descargando sitemap: {url}")
        resp = requests.get(url, timeout=20)
        if resp.status_code != 200:
            return []
        
        content = resp.content
        if url.endswith(".gz") or content.startswith(b'\x1f\x8b'):
            content = gzip.decompress(content)
            
        root = ET.fromstring(content)
        
        if root.tag.endswith('sitemapindex'):
            locs = []
            for sitemap in root.findall('.//{*}sitemap/{*}loc'):
                if sitemap.text:
                    locs.extend(expand_sitemap(sitemap.text))
            return locs

        locs = [loc.text for loc in root.findall('.//{*}loc') if loc.text]
        print(f"Encontradas {len(locs)} URLs en el sitemap.")
        return locs[:15] # Lote reducido para evitar timeouts en GitHub Actions
    except Exception as e:
        print(f"Error procesando sitemap {url}: {e}")
    return []

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

    valid_urls = [u for u in urls if not u.endswith((".xml", ".gz", ".zip"))]

    async with AsyncWebCrawler(verbose=True) as crawler:
        for url in valid_urls:
            print(f"Procesando: {url}")
            try:
                result = await crawler.arun(
                    url=url,
                    word_count_threshold=20,
                    exclude_external_links=True,
                    remove_overlay_elements=True,
                    process_iframes=True,
                    cache_mode=CacheMode.BYPASS,
                    magic=True,
                    excluded_tags=["nav", "footer", "header", "aside", "script", "style"],
                    css_selector="#fw-content, main, article, .cisco-content"
                )
                if result.success and result.markdown:
                    filename = os.path.join(output_dir, sanitize_filename(url))
                    with open(filename, "w", encoding="utf-8") as md_file:
                        md_file.write(result.markdown)
                    print(f"Guardado: {filename}")
                else:
                    print(f"Contenido vacío o fallo en {url}")
                await asyncio.sleep(1)
            except Exception as e:
                print(f"Excepción crítica en {url}: {str(e)}")

if __name__ == "__main__":
    asyncio.run(crawl_urls())
    
