"""
Utility functions for the web crawler
"""

import re
from urllib.parse import urlparse
from typing import List, Dict


def clean_text(text: str) -> str:
    """
    Clean and normalize text

    Args:
        text: Raw text string

    Returns:
        Cleaned text
    """
    if not text:
        return ""

    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)

    # Strip leading/trailing whitespace
    text = text.strip()

    return text


def is_valid_email(email: str) -> bool:
    """
    Validate email address

    Args:
        email: Email address string

    Returns:
        True if valid, False otherwise
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def is_valid_phone(phone: str) -> bool:
    """
    Validate phone number

    Args:
        phone: Phone number string

    Returns:
        True if valid, False otherwise
    """
    # Remove common formatting characters
    cleaned = re.sub(r'[\s\-\(\)\.]+', '', phone)

    # Check if it's a valid US phone number
    pattern = r'^\+?1?\d{10,11}$'
    return bool(re.match(pattern, cleaned))


def extract_emails(text: str) -> List[str]:
    """
    Extract email addresses from text

    Args:
        text: Text to search

    Returns:
        List of email addresses
    """
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return list(set(re.findall(pattern, text)))


def extract_phones(text: str) -> List[str]:
    """
    Extract phone numbers from text

    Args:
        text: Text to search

    Returns:
        List of phone numbers
    """
    # Pattern for US phone numbers
    patterns = [
        r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b',
        r'\(\d{3}\)\s*\d{3}[-.]?\d{4}\b',
        r'\b1[-.]?\d{3}[-.]?\d{3}[-.]?\d{4}\b'
    ]

    phones = []
    for pattern in patterns:
        phones.extend(re.findall(pattern, text))

    return list(set(phones))


def get_domain(url: str) -> str:
    """
    Extract domain from URL

    Args:
        url: URL string

    Returns:
        Domain name
    """
    parsed = urlparse(url)
    return parsed.netloc


def summarize_page_data(pages: List[Dict]) -> Dict:
    """
    Generate summary statistics from crawled pages

    Args:
        pages: List of page data dictionaries

    Returns:
        Summary statistics
    """
    if not pages:
        return {}

    total_links = sum(len(page.get('links', [])) for page in pages)
    total_images = sum(len(page.get('images', [])) for page in pages)
    total_paragraphs = sum(len(page.get('paragraphs', [])) for page in pages)

    # Extract all emails and phones
    all_text = ' '.join(
        ' '.join(page.get('paragraphs', []))
        for page in pages
    )
    emails = extract_emails(all_text)
    phones = extract_phones(all_text)

    return {
        'total_pages': len(pages),
        'total_links': total_links,
        'total_images': total_images,
        'total_paragraphs': total_paragraphs,
        'unique_emails': emails,
        'unique_phones': phones,
        'avg_links_per_page': total_links / len(pages) if pages else 0,
        'avg_images_per_page': total_images / len(pages) if pages else 0,
    }
