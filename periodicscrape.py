"""
This code is to be ran on the server as a thread
It will:
- Run the webscaper functions defined in webscraper.py
- Perform CRUD operations defined in dboperations.py to store the webscraped results into the postgres database
"""

import webscraper
import dboperations
import geminimodel

all_articles = {}
webscraper.arstechnica(all_articles)
webscraper.the_verge(all_articles)
#print(all_articles)

for url in all_articles:
    # Check if url is in the postgresdb
    if not dboperations.url_exists(url):
        # articledict[article_link] = (authors, article_tags, article_title, article_subtitle, totalbody):
        title = all_articles[url][2]
        subtitle = all_articles[url][3]
        authors = all_articles[url][0]
        content = all_articles[url][4]
        tags = all_articles[url][1] + webscraper.sanitizestring(geminimodel.get_tags(content).strip()).split(", ")
        aisummary = webscraper.sanitizestring(geminimodel.get_summary(content))
        imageurl = ""
        print(title)
        dboperations.add_entry(url, title , subtitle , authors, content, tags, imageurl, aisummary)
    else:
        print(f"{url} already in db")