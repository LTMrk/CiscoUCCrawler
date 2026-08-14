import os
import asyncio
import re
import subprocess
import json
import hashlib
from datetime import datetime
from urllib.parse import urlparse, urljoin
from crawl4ai import AsyncWebCrawler, CacheMode

def load_config():
    config_path = "config.json"
    default_config = {
        "global_settings": {
            "default_max_depth": 1,
            "request_delay_seconds": 1,
            "word_count_threshold": 20,
            "default_css_selector": "main, article"
        },
        "domain_depths": {},
        "seeds": [],
        "blocked_patterns": [],
        "custom_behaviors": []
    }
    if os.path.exists(config_path):
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return default_config

CONFIG = load_config()
BLOCKED_PATTERNS = CONFIG.get("blocked_patterns", [])

def get_max_depth_for_url(url):
    netloc = urlparse(url.lower()).netloc
    for domain, depth in CONFIG.get("domain_depths", {}).items():
        if domain in netloc:
            return depth
    return CONFIG.get("global_settings", {}).get("default_max_depth", 1)

def get_custom_behavior(url):
    url_lower = url.lower()
    for behavior in CONFIG.get("custom_behaviors", []):
        if behavior.get("pattern", "").lower() in url_lower:
            return behavior.get("css_selector"), behavior.get("js_code")
    return CONFIG.get("global_settings", {}).get("default_css_selector"), None

def get_group_filename(url):
    url_lower = url.lower()
    if "developer.webex.com" in url_lower:
        return "webex_api_reference_consolidated.md"
    netloc = urlparse(url).netloc
    return f"misc_{netloc.replace('.', '_').replace('-', '_')}.md"

def normalize_url(url):
    return url.split('#')[0].split('?')[0].rstrip('/')

def is_blocked_by_user(url):
    return any(pattern in url.lower() for pattern in BLOCKED_PATTERNS)

def is_strict_en_us(url):
    url_lower = url.lower()
    parsed = urlparse(url_lower)
    if 'cisco.com' in parsed.netloc and '/c/' in parsed.path and '/c/en/us/' not in parsed.path:
        return False
    if 'webex.com' in parsed.netloc and bool(re.search(r'/[a-z]{2}-[a-z]{2}/', parsed.path)) and '/en-us/' not in parsed.path:
        return False
    return True

def is_allowed_domain(url):
    return any(domain in url for domain in ['cisco.com', 'webex.com', 'webexconnect.io', 'webexengage.io'])

def log_error(url, reason):
    os.makedirs("logs", exist_ok=True)
    timestamp = datetime.now().isoformat()
    with open("logs/error.log", "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] ERROR - {reason} | URL: {url}\n")

def load_state():
    state_file = "logs/crawl_state.json"
    if os.path.exists(state_file):
        with open(state_file, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_state(state):
    os.makedirs("logs", exist_ok=True)
    with open("logs/crawl_state.json", "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)

def get_content_hash(content):
    return hashlib.sha256(content.encode('utf-8')).hexdigest()

def git_commit_and_push():
    try:
        os.makedirs("docs", exist_ok=True)
        os.makedirs("logs", exist_ok=True)
        subprocess.run(["git", "config", "--global", "user.name", "github-actions[bot]"], check=True)
        subprocess.run(["git", "config", "--global", "user.email", "github-actions[bot]@users.noreply.github.com"], check=True)
        status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
        if not status.stdout.strip():
            return
        subprocess.run(["git", "add", "docs/", "logs/", "config.json"], check=True)
        subprocess.run(["git", "commit", "-m", "docs: optimizacion de extraccion y purga de redundancias"], check=True)
        subprocess.run(["git", "pull", "--rebase", "origin", "main"], check=False)
        subprocess.run(["git", "push"], check=True)
    except Exception as e:
        log_error("GIT_PUSH", str(e))

async def deep_crawl():
    output_dir = "docs"
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs("logs", exist_ok=True)
    
    MAX_URLS_PER_RUN = 20
    processed_count = 0
    
    state = load_state()
    seen_hashes = {data.get("hash") for data in state.values() if isinstance(data, dict)}
    visited = set(state.keys())
    
    frontier_file = "logs/frontier.json"
    queue = asyncio.Queue()
    
    if os.path.exists(frontier_file):
        with open(frontier_file, "r", encoding="utf-8") as f:
            for item in json.load(f):
                await queue.put((item["url"], item["depth"]))
    else:
        for seed in [normalize_url(u.strip()) for u in CONFIG.get("seeds", []) if u.strip()]:
            if seed not in visited and is_strict_en_us(seed) and is_allowed_domain(seed) and not is_blocked_by_user(seed):
                await queue.put((seed, 0))

    delay = CONFIG.get("global_settings", {}).get("request_delay_seconds", 1)

    async with AsyncWebCrawler(verbose=True) as crawler:
        while not queue.empty():
            if processed_count >= MAX_URLS_PER_RUN:
                break
                
            url, depth = await queue.get()
            if url in visited:
                continue
            visited.add(url)
            processed_count += 1
            
            target_css, js_injection = get_custom_behavior(url)
            
            try:
                result = await crawler.arun(
                    url=url,
                    word_count_threshold=5,
                    exclude_external_links=True,
                    remove_overlay_elements=True,
                    process_iframes=False,
                    cache_mode=CacheMode.BYPASS,
                    magic=False,
                    css_selector=target_css,
                    js_code=js_injection if js_injection else "await new Promise(r => setTimeout(r, 3000));"
                )
                
                if not result.success or not result.html:
                    log_error(url, f"Fallo HTTP o DOM vacio: {getattr(result, 'error_message', 'Desconocido')}")
                    continue

                # EXTRACCIÓN OPTIMIZADA PARA WEBEX: Captura nativa del JSON empaquetado sin expandir basura DOM
                extracted_markdown = ""
                if "developer.webex.com" in url.lower():
                    match = re.search(r'window\.__INITIAL_STATE__\s*=\s*(\{.*?\});\s*<\/script>', result.html, re.DOTALL)
                    if match:
                        try:
                            state_json = json.loads(match.group(1))
                            api_entries = state_json.get("apiReference", {}).get("entry", {}).get("entries", [])
                            md_lines = [f"# Webex API Reference - Consolidado desde {url}\n"]
                            for entry in api_entries:
                                title = entry.get("title", "Endpoint")
                                md_lines.append(f"## {title}\n")
                                for version in entry.get("versions", []):
                                    spec_str = version.get("spec", "{}")
                                    md_lines.append(```json\n{spec_str}\n```\n)
                            extracted_markdown = "\n".join(md_lines)
                        except Exception:
                            pass
                
                # Fallback estándar si no es un portal con estado hidratado de Webex
                if not extracted_markdown:
                    extracted_markdown = result.markdown

                if extracted_markdown:
                    content_hash = get_content_hash(extracted_markdown)
                    if content_hash not in seen_hashes:
                        filename = os.path.join(output_dir, get_group_filename(url))
                        with open(filename, "w", encoding="utf-8") as md_file:
                            md_file.write(extracted_markdown)
                        
                        state[url] = {"hash": content_hash, "timestamp": datetime.now().isoformat()}
                        seen_hashes.add(content_hash)
                        save_state(state)
                        git_commit_and_push()

                if depth < get_max_depth_for_url(url) and hasattr(result, 'links'):
                    for link_obj in result.links.get("internal", []):
                        raw_next = link_obj.get("href")
                        if raw_next:
                            next_url = normalize_url(urljoin(url, raw_next))
                            if next_url.startswith("http") and next_url not in visited:
                                if is_strict_en_us(next_url) and is_allowed_domain(next_url) and not is_blocked_by_user(next_url):
                                    await queue.put((next_url, depth + 1))
                                    
                await asyncio.sleep(delay)
            except Exception as e:
                log_error(url, str(e))

    remaining = []
    while not queue.empty():
        u, d = queue.get_nowait()
        remaining.append({"url": u, "depth": d})
        
    if remaining:
        with open(frontier_file, "w", encoding="utf-8") as f:
            json.dump(remaining, f, indent=2)
    elif os.path.exists(frontier_file):
        os.remove(frontier_file)
        
    git_commit_and_push()

if __name__ == "__main__":
    asyncio.run(deep_crawl())
    
