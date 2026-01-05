#!/bin/bash
# Setup script for Peach State Intertie Web Crawler

echo "Setting up Peach State Intertie Web Crawler..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed. Please install Python 3.7 or higher."
    exit 1
fi

echo "Python version: $(python3 --version)"

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "Creating .env file from template..."
    cp .env.example .env
    echo "Please edit .env file to customize settings"
fi

# Create output directory
echo "Creating output directory..."
mkdir -p output

# Make crawler executable
echo "Making crawler executable..."
chmod +x crawler.py

echo ""
echo "Setup complete!"
echo ""
echo "To activate the virtual environment, run:"
echo "  source venv/bin/activate"
echo ""
echo "To run the crawler, use:"
echo "  python crawler.py"
echo ""
echo "For more options, see README.md"
