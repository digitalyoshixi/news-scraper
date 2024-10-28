from bs4 import BeautifulSoup 
import requests
import json

def returnpagedata():
    return "Fun"


def scrapewebsite(url : str) -> str:
    """
    return the required contents of a given url
    required contents include:
    1. Article name
    2. Author name
    3. Article body
    """

def arstechnica(articledict):
    """
    ars technica URL: https://arstechnica.com/gadgets/
    """
    # visit the page
    url = "https://arstechnica.com/gadgets/"
    home_html = requests.get(url)
    soup = BeautifulSoup(home_html.content, 'html.parser')

    individual_articles = soup.findAll('a', class_="relative block aspect-square h-auto w-16 overflow-hidden rounded-sm md:w-24")
    for individual_article in individual_articles:
        article_link = individual_article['href']

        individual_article_html = requests.get(article_link).content
        soup = BeautifulSoup(individual_article_html, 'html.parser')
        article_bodies = soup.findAll('div', class_="post-content post-content-double text-xl lg:pl-[72px]")
        totalbody = []
        for article_body in article_bodies:
            ptags = article_body.findAll('p')
            for tag in ptags:
                atags = []
                for a in tag.findAll('a'):
                    atags.append((a.text,a['href']))
                    #a.decompose()
                temptag = tag.text
                lastindex = 0
                while len(atags) > 0:
                    nextatag = atags[0][0]
                    lastindex = temptag.find(nextatag)
                    print(nextatag, lastindex)
                    oktext = temptag[:lastindex]
                    print(oktext)
                    totalbody.append((oktext,))
                    totalbody.append(atags.pop(0))
                totalbody.append((temptag[lastindex:],))
                print(totalbody)
                #totalbody.append(str(tag).strip('<p>').strip('</p>'))
                breakpoint()
        article_author = soup.find('a', class_="text-orange-400 hover:text-orange-500").text.strip()
        article_title = soup.find('h1', class_="mb-3 font-serif text-4xl font-bold text-gray-100 md:text-6xl md:leading-[1.05]").text.strip()
        # update dictionary
        articledict[article_link] = (article_author, article_title, totalbody)
# make a python dictionary
allarticles = {}

arstechnica(allarticles)

with open('articles.json', 'w') as f:
    json.dump(allarticles, f)

