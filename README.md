# Faceit Data Scraper

A Python-based tool for scraping and analyzing Faceit player statistics and match history data.

## Features

- Fetch player information by nickname
- Retrieve player lifetime statistics
- Get detailed match history
- Collect match-specific statistics
- Save data in JSON format for further analysis

## Prerequisites

- Python 3.x
- Virtual environment (recommended)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ElinArtem/faceit-scraper.git
cd faceit-scraper
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Open `run.py` and set your target player nickname:
```python
nickname = "YOUR_PLAYER_NICKNAME"
```

2. Run the script:
```bash
python run.py
```

The script will:
- Fetch player information
- Collect lifetime statistics
- Get match history
- Save detailed match statistics to a JSON file

## Project Structure

```
├── src/
│   ├── config.py     # Configuration of project (api keys, URLs, etc.)
│   ├── scraper.py    # Core scraping functionality
│   ├── history.py    # Match history handling
│   ├── utils         # Utility functions
│   └── storage       # Data storage operations
├── data/             # Directory for saved data
├── run.py            # Main execution script
```

## Data Output

The script generates JSON files containing:
- Player statistics
- Match history
- Detailed match statistics
- Timestamps and game information

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This tool is for educational purposes only. Please respect Faceit's terms of service and rate limits when using this scraper.
