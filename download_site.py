#!/usr/bin/env python3
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time

visited = set()
base_url = "https://peachstateintertie.com"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

def download_page(url, depth=0, max_depth=2):
    if depth > max_depth or url in visited:
        return

    visited.add(url)

    try:
        print(f"Fetching: {url}")
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()

        # Parse URL
        parsed = urlparse(url)
        path = parsed.path.strip('/')

        if not path:
            path = 'index.html'
        elif not path.endswith('.html'):
            path += '.html'

        # Create directory structure
        filepath = os.path.join('site', path)
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        # Save HTML
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(response.text)

        print(f"Saved: {filepath}")

        # Parse and find links
        soup = BeautifulSoup(response.text, 'html.parser')
        for link in soup.find_all('a', href=True):
            href = link['href']
            absolute_url = urljoin(url, href)

            if absolute_url.startswith(base_url):
                time.sleep(1)
                download_page(absolute_url, depth + 1, max_depth)

    except Exception as e:
        print(f"Error: {e}")

os.makedirs('site', exist_ok=True)
download_page(base_url)
print(f"\nDownloaded {len(visited)} pages")
