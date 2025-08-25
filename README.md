# create project folder
mkdir olx_scraper && cd olx_scraper

# create virtual environment
python3 -m venv venv
source venv/bin/activate   # (Linux/Mac)
# venv\Scripts\activate    # (Windows)

# create requirements.txt (see above) and install
pip install -r requirements.txt

# run script
python scraper.py
