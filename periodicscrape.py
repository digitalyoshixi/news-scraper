"""
This code is to be ran on the server as a thread
It will:
- Run the webscaper functions defined in webscraper.py
- Perform CRUD operations defined in dboperations.py to store the webscraped results into the postgres database
"""

import webscraper
import dboperations

all_articles = {}
webscraper.the_verge(all_articles)
print(all_articles)
breakpoint()

for url in all_articles:
    dboperations.add_entry(url, all_articles[url][0], all_articles[url][2], all_articles[url][1])