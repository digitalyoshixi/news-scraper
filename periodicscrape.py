"""
This code is to be ran on the server as a thread
It will:
- Run the webscaper functions defined in webscraper.py
- Perform CRUD operations defined in dboperations.py to store the webscraped results into the postgres database
"""

import webscaper
import dboperations