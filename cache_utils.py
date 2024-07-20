import os
import json
import requests

CACHE_FILE = 'api_cache.json'

if os.path.exists(CACHE_FILE):
    with open(CACHE_FILE, 'r', encoding='utf8') as f:
        cache = json.load(f)
else:
    cache = {}

def save_cache():
    with open(CACHE_FILE, 'w', encoding='utf8') as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)

def cached_api_request(url):
    if url in cache:
        print(f"Cache hit for URL: {url}")
        return cache[url]
    else:
        print(f"Cache miss for URL: {url}")
        response = requests.get(url)
        cache[url] = response.json()
        save_cache()
        return cache[url]
