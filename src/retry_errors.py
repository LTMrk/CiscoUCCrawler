import os
import asyncio
import re
from crawl4ai import AsyncWebCrawler, CacheMode

def extract_failed_urls(log_path):
    failed_urls = set()
    if not os.path.exists(log_path):
        print("No se encontro el archivo de log.")
        return failed_urls

    with open(log_path, "r", encoding="utf-8") as f:
        for line in f:
            # Ignorar las entradas que son duplicados exitosos
            if "CONTENIDO DUPLICADO EXACTO" in line or "GIT_PUSH" in line:
                continue
            
            # Extraer la URL al final de la linea
            match = re.search(r'\| URL: (https?://[^\s]+)', line)
            if match:
                failed_urls.add(match.group(1))
    
    return list(failed_urls)

async def retry_failed_urls():
    urls_to_retry = extract_failed_urls("logs/error.log")
    print(f"URLs a reintentar: {len(urls_to_retry)}")
    
    output_dir = "docs"
    os.makedirs(output_dir, exist_ok=True)
    
    # Cadencia alta para evadir Akamai WAF
    DELAY_SECONDS = 30 

    async with AsyncWebCrawler(verbose=True) as crawler:
        for url in urls_to_retry:
            print(f"Reintentando con cadencia alta: {url}")
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
                    filename = os.path.join(output_dir, "reintentos_exitosos.md")
                    with open(filename, "a", encoding="utf-8") as md_file:
                        md_file.write(f"\n\n---\n# ORIGEN: {url}\n\n")
                        md_file.write(result.markdown)
                    print("Guardado en reintentos_exitosos.md")
                else:
                    print(f"Fallo definitivo en reintento: {result.error_message}")
                
                print(f"Esperando {DELAY_SECONDS} segundos para evadir el WAF...")
                await asyncio.sleep(DELAY_SECONDS)
                
            except Exception as e:
                print(f"Excepcion en reintento {url}: {str(e)}")

if __name__ == "__main__":
    asyncio.run(retry_failed_urls())
  
