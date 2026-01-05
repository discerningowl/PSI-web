"""
Configuration module for the Peach State Intertie web crawler
"""

import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Crawler configuration settings"""

    # Base URL to crawl
    BASE_URL = os.getenv('BASE_URL', 'https://peachstateintertie.com')

    # Output directory for crawled data
    OUTPUT_DIR = os.getenv('OUTPUT_DIR', './output')

    # Maximum crawl depth
    MAX_DEPTH = int(os.getenv('MAX_DEPTH', '3'))

    # Delay between requests (in seconds)
    DELAY_BETWEEN_REQUESTS = float(os.getenv('DELAY_BETWEEN_REQUESTS', '1.0'))

    # User agent string
    USER_AGENT = os.getenv(
        'USER_AGENT',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    )

    # Request timeout
    REQUEST_TIMEOUT = int(os.getenv('REQUEST_TIMEOUT', '30'))

    # Enable/disable robots.txt checking
    RESPECT_ROBOTS_TXT = os.getenv('RESPECT_ROBOTS_TXT', 'true').lower() == 'true'
