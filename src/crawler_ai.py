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
            "word_count_threshold": 20
        },
        "domain_depths": {}
    }
    if os.path.exists(config_path):
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            log_error("CONFIG_LOAD", str(e))
    return default_config

CONFIG = load_config()

def get_max_depth_for_url(url):
    netloc = urlparse(url.lower()).netloc
    domain_map = CONFIG.get("domain_depths", {})
    for domain, depth in domain_map.items():
        if domain in netloc:
            return depth
    return CONFIG.get("global_settings", {}).get("default_max_depth", 1)

def get_group_filename(url):
    url_lower = url.lower()
    
    if any(x in url_lower for x in ["cucm", "unified-communications-manager", "callmanager"]):
        return "cisco_cucm.md"
    if any(x in url_lower for x in ["unity", "unity-connection", "cuc"]):
        return "cisco_unity.md"
    if any(x in url_lower for x in ["expressway", "vcs", "video-communication-server"]):
        return "cisco_expressway.md"
    if any(x in url_lower for x in ["cube", "border-element", "vg-series", "catalyst-8000", "isr"]):
        return "cisco_gateways_routers.md"
    if any(x in url_lower for x in ["meeting-server", "cms"]):
        return "cisco_cms.md"

    if any(x in url_lower for x in ["uccx", "contact-center-express"]):
        return "cisco_uccx.md"
    if any(x in url_lower for x in ["ucce", "contact-center-enterprise", "cvp", "finesse"]):
        return "cisco_ucce.md"

    if any(x in url_lower for x in ["webex-contact-center", "wxcc"]):
        return "webex_contact_center.md"
    if any(x in url_lower for x in ["webexconnect", "webex-connect", "imimobile"]):
        return "webex_connect.md"
    if any(x in url_lower for x in ["webexengage", "webex-engage"]):
        return "webex_engage.md"

    if any(x in url_lower for x in ["webex-calling", "cloud-calling"]):
        return "webex_calling.md"
    if any(x in url_lower for x in ["meetings", "webinars", "training"]):
        return "webex_meetings.md"
    if any(x in url_lower for x in ["webex-app", "webex-teams", "messaging"]):
        return "webex_app.md"

    if any(x in url_lower for x in ["hardware.webex.com", "collaboration-endpoints", "ip-phone", "8800-series", "room-series", "desk-series", "board-series", "headsets", "cameras"]):
        return "cisco_devices_hardware.md"

    netloc = urlparse(url).netloc
    safe_netloc = netloc.replace(".", "_").replace("-", "_")
    return f"misc_{safe_netloc}.md"

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

def log_error(url, reason):
    os.makedirs("logs", exist_ok=True)
    timestamp = datetime.now().isoformat()
    with open("logs/error.log", "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] ERROR - {reason} | URL: {url}\n")
    print(f"REGISTRADO ERROR: {reason} en {url}")

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
            
        subprocess.run(["git", "add", "docs/", "logs/"], check=True)
        subprocess.run(["git", "commit", "-m", "docs: actualizacion incremental de estado, logs y agrupaciones"], check=True)
        subprocess.run(["git", "pull", "--rebase", "origin", "main"], check=False)
        subprocess.run(["git", "push"], check=True)
    except Exception as e:
        log_error("GIT_PUSH", str(e))

async def deep_crawl():
    output_dir = "docs"
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs("logs", exist_ok=True)
    
    MAX_URLS_PER_RUN = 50
    processed_count = 0
    
    state = load_state()
    seen_hashes = {data.get("hash") for data in state.values() if isinstance(data, dict)}
    visited = set(state.keys())
    
    # 1. CARGA DE LA COLA DE RASTREO (FRONTIER)
    frontier_file = "logs/frontier.json"
    queue = asyncio.Queue()
    
    if os.path.exists(frontier_file):
        with open(frontier_file, "r", encoding="utf-8") as f:
            saved_frontier = json.load(f)
            for item in saved_frontier:
                await queue.put((item["url"], item["depth"]))
    else:
        if not os.path.exists("urls.txt"):
            print("El archivo urls.txt no existe.")
            return
        with open("urls.txt", "r", encoding="utf-8") as f:
            seeds = [normalize_url(line.strip()) for line in f if line.strip() and not line.startswith("#")]
        for seed in seeds:
            if seed not in visited and is_strict_en_us(seed) and is_allowed_domain(seed) and not is_blocked_by_user(seed):
                await queue.put((seed, 0))

    delay = CONFIG.get("global_settings", {}).get("request_delay_seconds", 1)
    word_threshold = CONFIG.get("global_settings", {}).get("word_count_threshold", 20)

    async with AsyncWebCrawler(verbose=True) as crawler:
        while not queue.empty():
            # 2. CONTROL DE LÍMITE DE LOTE
            if processed_count >= MAX_URLS_PER_RUN:
                print("LIMITE DE LOTE ALCANZADO. Preparando volcado de estado.")
                break
                
            url, depth = await queue.get()
            
            if url in visited:
                continue
            visited.add(url)
            processed_count += 1
            
            max_depth_allowed = get_max_depth_for_url(url)
            print(f"[Profundidad {depth}/{max_depth_allowed}] Procesando: {url}")
            
            js_injection = "await new Promise(r => setTimeout(r, 5000));" if "developer.webex.com" in url.lower() else None
            
            try:
                result = await crawler.arun(
                    url=url,
                    word_count_threshold=word_threshold,
                    exclude_external_links=True,
                    remove_overlay_elements=True,
                    process_iframes=True,
                    cache_mode=CacheMode.BYPASS,
                    magic=True,
                    excluded_tags=["nav", "footer", "header", "aside", "script", "style"],
                    css_selector="#fw-content, main, article, .content, .cisco-content",
                    js_code=js_injection
                )
                
                if not result.success:
                    log_error(url, f"Fallo HTTP o Crawler: {result.error_message}")
                elif not result.markdown:
                    log_error(url, "Contenido vacio tras filtrado DOM")
                else:
                    content_hash = get_content_hash(result.markdown)
                    if content_hash in seen_hashes:
                        log_error(url, "CONTENIDO DUPLICADO EXACTO")
                    else:
                        filename = os.path.join(output_dir, get_group_filename(url))
                        with open(filename, "a", encoding="utf-8") as md_file:
                            md_file.write(f"\n\n---\n# ORIGEN: {url}\n\n")
                            md_file.write(result.markdown)
                        
                        state[url] = {
                            "hash": content_hash,
                            "timestamp": datetime.now().isoformat()
                        }
                        seen_hashes.add(content_hash)
                        save_state(state)
                        git_commit_and_push()
                
                if depth < max_depth_allowed and hasattr(result, 'links'):
                    internal_links = result.links.get("internal", [])
                    for link_obj in internal_links:
                        raw_next_url = link_obj.get("href")
                        if raw_next_url:
                            next_url = normalize_url(urljoin(url, raw_next_url))
                            if next_url.startswith("http") and next_url not in visited:
                                if is_strict_en_us(next_url) and is_allowed_domain(next_url) and not is_blocked_by_user(next_url):
                                    await queue.put((next_url, depth + 1))
                                
                await asyncio.sleep(delay)
            except Exception as e:
                log_error(url, f"Excepcion critica: {str(e)}")

    # 3. SERIALIZACIÓN DE LA COLA RESTANTE
    remaining_frontier = []
    while not queue.empty():
        u, d = queue.get_nowait()
        remaining_frontier.append({"url": u, "depth": d})
        
    if remaining_frontier:
        with open(frontier_file, "w", encoding="utf-8") as f:
            json.dump(remaining_frontier, f, indent=2)
        with open("logs/more_work.flag", "w") as f:
            f.write("PENDING")
        print(f"Quedan {len(remaining_frontier)} URLs en la cola. Archivo flag generado.")
    else:
        if os.path.exists(frontier_file):
            os.remove(frontier_file)
        if os.path.exists("logs/more_work.flag"):
            os.remove("logs/more_work.flag")
        print("Rastreo completado. Cola vacía.")
        
    git_commit_and_push()

if __name__ == "__main__":
    asyncio.run(deep_crawl())
