import os
import asyncio
import re
from crawl4ai import AsyncWebCrawler, CacheMode

def sanitize_filename(url):
    clean = re.sub(r'https?://', '', url)
    clean = re.sub(r'[^a-zA-Z0-9]', '_', clean)
    return clean[:100] + ".md"

async def crawl_urls():
    output_dir = "docs"
    os.makedirs(output_dir, exist_ok=True)
    
    if not os.path.exists("urls.txt"):
        print("El archivo urls.txt no existe.")
        return

    with open("urls.txt", "r") as f:
        urls = [line.strip() for line in f if line.strip() and not line.startswith("#")]

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
                    magic=True
                )
                if result.success:
                    filename = os.path.join(output_dir, sanitize_filename(url))
                    with open(filename, "w", encoding="utf-8") as md_file:
                        md_file.write(result.markdown)
                    print(f"Guardado exitosamente: {filename}")
                else:
                    print(f"Error al rastrear {url}: {result.error_message}")
            except Exception as e:
                print(f"Excepción crítica en {url}: {str(e)}")

if __name__ == "__main__":
    asyncio.run(crawl_urls())
  
