import os
import asyncio
import re
from urllib.parse import urlparse, urljoin
from crawl4ai import AsyncWebCrawler, CacheMode

def sanitize_filename(url):
    clean = re.sub(r'https?://', '', url)
    clean = re.sub(r'[^a-zA-Z0-9]', '_', clean)
    return clean[:100] + ".md"

def normalize_url(url):
    # HECHO TÉCNICO: Elimina fragmentos y parámetros para evitar procesar duplicados
    return url.split('#')[0].split('?')[0].rstrip('/')

def is_strict_en_us(url):
    url_lower = url.lower()
    
    # HECHO TÉCNICO: Regex para detectar patrones ISO de localización (ej. /es/, /de-de/, /zh_cn/)
    locale_pattern = re.compile(r'/([a-z]{2})([-_][a-z]{2})?/')
    matches = locale_pattern.findall(url_lower)
    
    for match in matches:
        lang_code = match[0]
        # Si encuentra un código de idioma de 2 letras que no sea 'en' o 'us', lo rechaza
        if lang_code not in ['en', 'us', 'c']: 
            return False

    parsed = urlparse(url_lower)
    path = parsed.path
    
    if 'cisco.com' in parsed.netloc and '/c/' in path:
        if '/c/en/us/' not in path:
            return False
            
    if 'webex.com' in parsed.netloc:
        if bool(re.search(r'/[a-z]{2}-[a-z]{2}/', path)) and '/en-us/' not in path:
            return False

    return True

def is_allowed_domain(url):
    # HECHO TÉCNICO: Evita fugas del crawler hacia internet abierto
    allowed = ['cisco.com', 'webex.com', 'webexconnect.io', 'webexengage.io']
    return any(domain in url for domain in allowed)

async def deep_crawl():
    output_dir = "docs"
    os.makedirs(output_dir, exist_ok=True)
    
    if not os.path.exists("urls.txt"):
        print("El archivo urls.txt no existe.")
        return

    with open("urls.txt", "r") as f:
        seeds = [normalize_url(line.strip()) for line in f if line.strip() and not line.startswith("#")]

    visited = set()
    queue = asyncio.Queue()
    max_depth = 2
    
    for seed in seeds:
        if is_strict_en_us(seed) and is_allowed_domain(seed):
            await queue.put((seed, 0))

    async with AsyncWebCrawler(verbose=True) as crawler:
        while not queue.empty():
            url, depth = await queue.get()
            
            if url in visited:
                continue
            visited.add(url)
            
            print(f"[Profundidad {depth}] Procesando: {url}")
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
                    css_selector="#fw-content, main, article, .content, .cisco-content"
                )
                
                if result.success and result.markdown:
                    filename = os.path.join(output_dir, sanitize_filename(url))
                    with open(filename, "w", encoding="utf-8") as md_file:
                        md_file.write(result.markdown)
                    print(f"Guardado exitosamente: {filename}")
                
                # HECHO TÉCNICO: Extracción profunda con resolución absoluta de rutas
                if depth < max_depth and hasattr(result, 'links'):
                    internal_links = result.links.get("internal", [])
                    for link_obj in internal_links:
                        raw_next_url = link_obj.get("href")
                        if raw_next_url:
                            next_url = normalize_url(urljoin(url, raw_next_url))
                            if next_url.startswith("http") and next_url not in visited:
                                if is_strict_en_us(next_url) and is_allowed_domain(next_url):
                                    await queue.put((next_url, depth + 1))
                                
                await asyncio.sleep(1)
            except Exception as e:
                print(f"Excepción crítica en {url}: {str(e)}")

if __name__ == "__main__":
    asyncio.run(deep_crawl())
