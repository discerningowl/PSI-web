# Peach State Intertie Web Crawler

A Python-based web crawler designed to scrape and analyze content from the Peach State Intertie website (https://peachstateintertie.com).

## Features

- **Recursive Crawling**: Automatically discovers and crawls linked pages up to a configurable depth
- **Rate Limiting**: Respects server resources with configurable delays between requests
- **Data Extraction**: Extracts structured data including:
  - Page titles and meta descriptions
  - Headings (h1-h6)
  - Paragraphs and text content
  - Links and images
  - JSON-LD structured data
  - Contact information (emails, phone numbers)
- **Multiple Output Formats**:
  - JSON (structured data for programmatic access)
  - HTML (human-readable report)
  - TXT (list of crawled URLs)
- **Proper Headers**: Uses realistic browser headers to avoid blocking
- **Error Handling**: Robust error handling and logging

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Setup

1. Clone this repository:
```bash
git clone <repository-url>
cd PSI-web
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure the crawler (optional):
```bash
cp .env.example .env
# Edit .env with your preferred settings
```

## Usage

### Basic Usage

Run the crawler with default settings:

```bash
python crawler.py
```

### Command Line Options

```bash
python crawler.py --url https://peachstateintertie.com --depth 3 --delay 1.0
```

**Options:**
- `--url`: Base URL to crawl (default: from .env or https://peachstateintertie.com)
- `--depth`: Maximum crawl depth (default: 3)
- `--delay`: Delay between requests in seconds (default: 1.0)

### Configuration

Edit the `.env` file to customize crawler behavior:

```env
BASE_URL=https://peachstateintertie.com
OUTPUT_DIR=./output
MAX_DEPTH=3
DELAY_BETWEEN_REQUESTS=1
USER_AGENT=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36
```

## Output

The crawler generates three types of output files in the `output/` directory:

1. **JSON Data** (`crawled_data_YYYYMMDD_HHMMSS.json`):
   - Complete structured data from all crawled pages
   - Includes metadata, content, links, and images

2. **HTML Report** (`crawl_report_YYYYMMDD_HHMMSS.html`):
   - Human-readable summary of the crawl
   - Can be opened in any web browser

3. **URL List** (`urls_YYYYMMDD_HHMMSS.txt`):
   - Simple list of all crawled URLs
   - One URL per line

## Project Structure

```
PSI-web/
├── crawler.py          # Main crawler script
├── config.py           # Configuration settings
├── utils.py            # Utility functions
├── requirements.txt    # Python dependencies
├── .env.example        # Example environment configuration
├── .gitignore          # Git ignore rules
├── README.md           # This file
├── output/             # Output directory (created on first run)
└── crawler.log         # Log file (created on first run)
```

## How It Works

1. **Initialization**: The crawler starts at the base URL with configurable settings
2. **Fetching**: Pages are fetched using proper HTTP headers to avoid blocking
3. **Parsing**: HTML content is parsed using BeautifulSoup
4. **Extraction**: Structured data is extracted from each page
5. **Discovery**: Links are discovered and added to the crawl queue
6. **Recursion**: The process repeats for discovered links up to max depth
7. **Output**: Results are saved in multiple formats

## Rate Limiting and Ethics

This crawler includes several features to be respectful of the target server:

- Configurable delay between requests (default: 1 second)
- Proper User-Agent headers
- Request timeout handling
- Maximum depth limiting

**Please use responsibly:**
- Don't set delay below 0.5 seconds
- Monitor the crawler.log for errors
- Respect robots.txt directives
- Use during off-peak hours for large crawls

## Troubleshooting

### 403 Forbidden Errors

If you receive 403 errors, the website may be blocking automated requests:
- Try increasing the delay between requests
- Check if the website has a robots.txt file
- Ensure you're using a realistic User-Agent

### Installation Issues

If you have trouble installing dependencies:
```bash
pip install --upgrade pip
pip install -r requirements.txt --no-cache-dir
```

### Permission Errors

If you get permission errors creating the output directory:
```bash
mkdir output
chmod 755 output
```

## Advanced Usage

### Programmatic Usage

You can also use the crawler in your own Python scripts:

```python
from crawler import PeachStateCrawler

# Create crawler instance
crawler = PeachStateCrawler(
    base_url='https://peachstateintertie.com',
    max_depth=2,
    delay=1.5
)

# Run the crawl
crawler.run()

# Access the data
print(f"Crawled {len(crawler.crawled_data)} pages")
```

### Custom Data Extraction

Modify the `extract_page_data` method in `crawler.py` to extract additional data specific to your needs.

## Logging

All crawler activity is logged to:
- Console (INFO level and above)
- `crawler.log` file (all levels)

View the log file to troubleshoot issues:
```bash
tail -f crawler.log
```

## License

This project is provided as-is for educational and research purposes.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## Disclaimer

This tool is designed for legitimate web scraping purposes. Always:
- Respect website terms of service
- Follow robots.txt directives
- Use reasonable rate limiting
- Obtain permission when necessary

The authors are not responsible for misuse of this tool.
