# Quick Start Guide

Get started with the Peach State Intertie Web Crawler in 3 simple steps!

## Step 1: Setup

Run the automated setup script:

```bash
chmod +x setup.sh
./setup.sh
```

Or manually:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Step 2: Run the Crawler

Activate the virtual environment (if not already active):

```bash
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Run the crawler:

```bash
python crawler.py
```

## Step 3: View Results

The crawler will create an `output/` directory with three files:

1. **JSON data**: `crawled_data_YYYYMMDD_HHMMSS.json`
2. **HTML report**: `crawl_report_YYYYMMDD_HHMMSS.html` (open in browser)
3. **URL list**: `urls_YYYYMMDD_HHMMSS.txt`

## Customization

### Quick Options

```bash
# Crawl deeper (more pages)
python crawler.py --depth 5

# Slower crawling (more polite)
python crawler.py --delay 2.0

# Different starting URL
python crawler.py --url https://example.com
```

### Configuration File

Edit `.env` for persistent settings:

```bash
cp .env.example .env
nano .env  # or use your favorite editor
```

## Example Session

```bash
# Setup
./setup.sh
source venv/bin/activate

# Run crawler
python crawler.py --depth 2 --delay 1.5

# View results
ls -lh output/
open output/crawl_report_*.html  # macOS
xdg-open output/crawl_report_*.html  # Linux
```

## Troubleshooting

### Problem: 403 Forbidden errors

**Solution**: Increase delay between requests
```bash
python crawler.py --delay 2.0
```

### Problem: Too many pages

**Solution**: Reduce crawl depth
```bash
python crawler.py --depth 2
```

### Problem: Package installation fails

**Solution**: Upgrade pip first
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Customize `crawler.py` for specific data extraction needs
- Check `crawler.log` for detailed activity logs

## Need Help?

- Check the log file: `tail -f crawler.log`
- Review the README.md for advanced usage
- Ensure you have Python 3.7 or higher: `python3 --version`
