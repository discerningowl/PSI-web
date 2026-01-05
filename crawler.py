#!/usr/bin/env python3
"""
Peach State Intertie Web Crawler
A configurable web crawler for scraping peachstateintertie.com
"""

import os
import json
import time
import logging
from urllib.parse import urljoin, urlparse
from datetime import datetime
from typing import Set, Dict, List
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('crawler.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class PeachStateCrawler:
    """Web crawler for Peach State Intertie website"""

    def __init__(self, base_url: str = None, max_depth: int = 3, delay: float = 1.0):
        """
        Initialize the crawler

        Args:
            base_url: Starting URL for crawling
            max_depth: Maximum depth to crawl
            delay: Delay between requests in seconds
        """
        self.base_url = base_url or os.getenv('BASE_URL', 'https://peachstateintertie.com')
        self.max_depth = max_depth or int(os.getenv('MAX_DEPTH', '3'))
        self.delay = delay or float(os.getenv('DELAY_BETWEEN_REQUESTS', '1.0'))
        self.output_dir = Path(os.getenv('OUTPUT_DIR', './output'))

        self.visited_urls: Set[str] = set()
        self.crawled_data: List[Dict] = []

        # Setup session with headers
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': os.getenv('USER_AGENT',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        })

        # Create output directory
        self.output_dir.mkdir(exist_ok=True)
        logger.info(f"Initialized crawler for {self.base_url}")

    def is_valid_url(self, url: str) -> bool:
        """Check if URL belongs to the target domain"""
        parsed = urlparse(url)
        base_parsed = urlparse(self.base_url)
        return parsed.netloc == base_parsed.netloc

    def normalize_url(self, url: str) -> str:
        """Normalize URL by removing fragments"""
        parsed = urlparse(url)
        return f"{parsed.scheme}://{parsed.netloc}{parsed.path}"

    def fetch_page(self, url: str) -> requests.Response:
        """
        Fetch a page with proper error handling

        Args:
            url: URL to fetch

        Returns:
            Response object or None if failed
        """
        try:
            logger.info(f"Fetching: {url}")
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            time.sleep(self.delay)  # Rate limiting
            return response
        except requests.RequestException as e:
            logger.error(f"Error fetching {url}: {e}")
            return None

    def extract_links(self, soup: BeautifulSoup, current_url: str) -> Set[str]:
        """
        Extract all links from the page

        Args:
            soup: BeautifulSoup object
            current_url: Current page URL

        Returns:
            Set of normalized URLs
        """
        links = set()
        for link in soup.find_all('a', href=True):
            href = link['href']
            absolute_url = urljoin(current_url, href)
            normalized_url = self.normalize_url(absolute_url)

            if self.is_valid_url(normalized_url):
                links.add(normalized_url)

        return links

    def extract_page_data(self, url: str, soup: BeautifulSoup) -> Dict:
        """
        Extract structured data from the page

        Args:
            url: Page URL
            soup: BeautifulSoup object

        Returns:
            Dictionary with extracted data
        """
        # Extract title
        title = soup.title.string if soup.title else "No title"

        # Extract meta description
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        description = meta_desc['content'] if meta_desc else ""

        # Extract all headings
        headings = {
            f'h{i}': [h.get_text(strip=True) for h in soup.find_all(f'h{i}')]
            for i in range(1, 7)
        }

        # Extract all paragraphs
        paragraphs = [p.get_text(strip=True) for p in soup.find_all('p') if p.get_text(strip=True)]

        # Extract all links
        links = [
            {'text': a.get_text(strip=True), 'href': a.get('href')}
            for a in soup.find_all('a', href=True)
        ]

        # Extract images
        images = [
            {'alt': img.get('alt', ''), 'src': img.get('src', '')}
            for img in soup.find_all('img')
        ]

        # Extract any structured data (JSON-LD)
        json_ld = []
        for script in soup.find_all('script', type='application/ld+json'):
            try:
                json_ld.append(json.loads(script.string))
            except:
                pass

        return {
            'url': url,
            'title': title,
            'description': description,
            'headings': headings,
            'paragraphs': paragraphs[:10],  # Limit to first 10 paragraphs
            'links': links,
            'images': images,
            'json_ld': json_ld,
            'crawled_at': datetime.now().isoformat()
        }

    def crawl(self, start_url: str = None, depth: int = 0):
        """
        Recursively crawl the website

        Args:
            start_url: Starting URL (defaults to base_url)
            depth: Current crawl depth
        """
        if start_url is None:
            start_url = self.base_url

        # Normalize URL
        start_url = self.normalize_url(start_url)

        # Check if already visited or max depth reached
        if start_url in self.visited_urls or depth > self.max_depth:
            return

        # Mark as visited
        self.visited_urls.add(start_url)

        # Fetch the page
        response = self.fetch_page(start_url)
        if not response:
            return

        # Parse the page
        soup = BeautifulSoup(response.content, 'lxml')

        # Extract data
        page_data = self.extract_page_data(start_url, soup)
        self.crawled_data.append(page_data)
        logger.info(f"Crawled: {start_url} (depth: {depth})")

        # Extract and crawl links
        if depth < self.max_depth:
            links = self.extract_links(soup, start_url)
            for link in links:
                if link not in self.visited_urls:
                    self.crawl(link, depth + 1)

    def save_results(self):
        """Save crawled data to files"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

        # Save as JSON
        json_file = self.output_dir / f'crawled_data_{timestamp}.json'
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump({
                'base_url': self.base_url,
                'crawled_at': datetime.now().isoformat(),
                'total_pages': len(self.crawled_data),
                'pages': self.crawled_data
            }, f, indent=2, ensure_ascii=False)
        logger.info(f"Saved JSON data to {json_file}")

        # Save as HTML report
        html_file = self.output_dir / f'crawl_report_{timestamp}.html'
        html_content = self.generate_html_report()
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        logger.info(f"Saved HTML report to {html_file}")

        # Save URL list
        url_file = self.output_dir / f'urls_{timestamp}.txt'
        with open(url_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(sorted(self.visited_urls)))
        logger.info(f"Saved URL list to {url_file}")

    def generate_html_report(self) -> str:
        """Generate an HTML report of the crawl"""
        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Crawl Report - {self.base_url}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        h1 {{
            color: #333;
            border-bottom: 3px solid #4CAF50;
            padding-bottom: 10px;
        }}
        .summary {{
            background: white;
            padding: 20px;
            border-radius: 5px;
            margin-bottom: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .page {{
            background: white;
            padding: 15px;
            margin-bottom: 15px;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .page h2 {{
            color: #4CAF50;
            margin-top: 0;
        }}
        .url {{
            color: #666;
            font-size: 14px;
            word-break: break-all;
        }}
        .content {{
            margin-top: 10px;
        }}
        .stat {{
            display: inline-block;
            margin-right: 20px;
            font-weight: bold;
        }}
    </style>
</head>
<body>
    <h1>Crawl Report: {self.base_url}</h1>

    <div class="summary">
        <h2>Summary</h2>
        <div class="stat">Total Pages: {len(self.crawled_data)}</div>
        <div class="stat">Crawl Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</div>
    </div>

    <h2>Crawled Pages</h2>
"""

        for page in self.crawled_data:
            html += f"""
    <div class="page">
        <h2>{page['title']}</h2>
        <div class="url">{page['url']}</div>
        <div class="content">
            <p><strong>Description:</strong> {page['description'] or 'No description'}</p>
            <p><strong>Links found:</strong> {len(page['links'])}</p>
            <p><strong>Images found:</strong> {len(page['images'])}</p>
        </div>
    </div>
"""

        html += """
</body>
</html>
"""
        return html

    def run(self):
        """Run the crawler"""
        logger.info(f"Starting crawl of {self.base_url}")
        logger.info(f"Max depth: {self.max_depth}, Delay: {self.delay}s")

        start_time = time.time()

        try:
            self.crawl()
        except KeyboardInterrupt:
            logger.info("Crawl interrupted by user")
        except Exception as e:
            logger.error(f"Crawl failed: {e}", exc_info=True)

        elapsed_time = time.time() - start_time
        logger.info(f"Crawl completed in {elapsed_time:.2f} seconds")
        logger.info(f"Total pages crawled: {len(self.crawled_data)}")

        # Save results
        self.save_results()


def main():
    """Main entry point"""
    import argparse

    parser = argparse.ArgumentParser(description='Crawl Peach State Intertie website')
    parser.add_argument('--url', help='Base URL to crawl',
                        default=os.getenv('BASE_URL', 'https://peachstateintertie.com'))
    parser.add_argument('--depth', type=int, help='Maximum crawl depth',
                        default=int(os.getenv('MAX_DEPTH', '3')))
    parser.add_argument('--delay', type=float, help='Delay between requests (seconds)',
                        default=float(os.getenv('DELAY_BETWEEN_REQUESTS', '1.0')))

    args = parser.parse_args()

    crawler = PeachStateCrawler(
        base_url=args.url,
        max_depth=args.depth,
        delay=args.delay
    )

    crawler.run()


if __name__ == '__main__':
    main()
