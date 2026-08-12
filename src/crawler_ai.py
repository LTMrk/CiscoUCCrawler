import os
import asyncio
import re
import subprocess
from urllib.parse import urlparse, urljoin
from crawl4ai import AsyncWebCrawler, CacheMode

def sanitize_filename(url):
    clean = re.sub(r'https?://', '', url)
    clean = re.sub(r'[^a-zA-Z0-9]', '_', clean)
    return clean[:100] + ".md"

def normalize_url(url):
    return url.split('#')[0].split('?')[0].rstrip('/')

def load_blocked_patterns():
    blocked_file = "blocked_urls.txt"
    if not os.path.exists(blocked_file):
        return []
    with open(blocked_file, "r", encoding="utf-8") as f:
        return [line.strip().lower() for line in f if line.strip() and not line.startswith("#")]

BLOCKED_PATTERNS = load_blocked_patterns()

def is_blocked_by_user(url):
    url_lower = url.lower()
    for pattern in BLOCKED_PATTERNS:
        if pattern in url_lower:
            return True
    return False

def is_strict_en_us(url):
    url_lower = url.lower()
    parsed = urlparse(url_lower)
    netloc = parsed.netloc
    path = parsed.path

    if 'careers.cisco.com' in netloc or 'jobs.cisco.com' in netloc:
        return False

    locale_pattern = re.compile(r'/([a-z]{2})([-_][a-z]{2})?/')
    matches = locale_pattern.findall(url_lower)
    
    for match in matches:
        lang_code = match[0]
        if lang_code not in ['en', 'us', 'c']: 
            return False

    if 'cisco.com' in netloc and '/c/' in path:
        if '/c/en/us/' not in path:
            return False
            
    if 'webex.com' in netloc:
        if bool(re.search(r'/[a-z]{2}-[a-z]{2}/', path)) and '/en-us/' not in path:
            return False

    return True

def is_allowed_domain(url):
    allowed = ['cisco.com', 'webex.com', 'webexconnect.io', 'webexengage.io']
    return any(domain in url for domain in allowed)

def git_commit_and_push(filename):
    try:
        subprocess.run(["git", "config", "--global", "user.name", "github-actions[bot]"], check=True)
        subprocess.run(["git", "config", "--global", "user.email", "github-actions[bot]@users.noreply.github.com"], check=True)
        subprocess.run(["git", "add", filename], check=True)
        
        diff_check = subprocess.run(["git", "diff", "--staged", "--quiet"])
        if diff_check.returncode != 0:
            commit_msg = f"docs: add {os.path.basename(filename)}"
            subprocess.run(["git", "commit", "-m", commit_msg], check=True)
            subprocess.run(["git", "pull", "--rebase", "origin", "main"], check=False)
            subprocess.run(["git", "push"], check=True)
            print(f"Sincronizado remotamente: {filename}")
    except Exception as e:
        print(f"Error en sincronizacion Git para {filename}: {e}")

async def deep_crawl():
    output_dir = "docs"
    os.makedirs(output_dir, exist_ok=True)
    
    if not os.path.exists("urls.txt"):
        print("El archivo urls.txt no existe.")
        return

    with open("urls.txt", "r", encoding="utf-8") as f:
        seeds = [normalize_url(line.strip()) for line in f if line.strip() and not line.startswith("#")]

    visited = set()
    queue = asyncio.Queue()
    max_depth = 2
    
    for seed in seeds:
        if is_strict_en_us(seed) and is_allowed_domain(seed) and not is_blocked_by_user(seed):
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
                    print(f"Guardado localmente: {filename}")
                    
                    git_commit_and_push(filename)
                
                if depth < max_depth and hasattr(result, 'links'):
                    internal_links = result.links.get("internal", [])
                    for link_obj in internal_links:
                        raw_next_url = link_obj.get("href")
                        if raw_next_url:
                            next_url = normalize_url(urljoin(url, raw_next_url))
                            if next_url.startswith("http") and next_url not in visited:
                                if is_strict_en_us(next_url) and is_allowed_domain(next_url) and not is_blocked_by_user(next_url):
                                    await queue.put((next_url, depth + 1))
                                
                await asyncio.sleep(1)
            except Exception as e:
                print(f"Excepcion critica en {url}: {str(e)}")

if __name__ == "__main__":
    asyncio.run(deep_crawl())
    
