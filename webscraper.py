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

def getarticlebody(ptags, headerurl=""):
    """
    from a list of all paragraph tags (which is supposed to represent the article body), return a formatted version that returns a list
    that looks like:
    [
        # paragraph 1
        [
        [normaltext, ""],
        [specialtext, url],
        [normaltext, ""],
        ...
        ],
        # paragrahph2
        [
        [normaltext, ""],
        [specialtext, url],
        [normaltext, ""],
        ...
        ],
    ]
    """

    totalbody = []
    for tag in ptags:
                paragraph = []
                atags = []
                for a in tag.findAll('a'):
                    actualurl = a['href']
                    if not 'http' in actualurl[:5]:
                        actualurl = headerurl+actualurl
                    atags.append([a.text,actualurl])
                    #a.decompose()
                temptag = tag.text
                lastindex = 0
                while len(atags) > 0:
                    nextatag = atags[0][0]
                    aindex = temptag.find(nextatag)
                    oktext = temptag[lastindex:aindex]
                    lastindex = aindex+len(atags[0][0])
                    paragraph.append([oktext,""])
                    paragraph.append(atags.pop(0))
                paragraph.append([temptag[lastindex:],""])
                totalbody.append(paragraph)
    return totalbody

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
        if not article_link in articledict.keys():
            individual_article_html = requests.get(article_link).content
            soup = BeautifulSoup(individual_article_html, 'html.parser')
            article_bodies = soup.findAll('div', class_="post-content post-content-double")
            totalbody = []
            for article_body in article_bodies:
                ptags = article_body.findAll('p')
                totalbody.extend(getarticlebody(ptags))
            article_tags = []
            #breakpoint()
            article_authors = soup.findAll('a', class_="text-orange-400 hover:text-orange-500")
            authors = []
            for article_author in article_authors:
                authors.append(article_author.attrs.get('content'))
            article_title = soup.find('h1', class_="mb-3").text.strip()
            article_subtitle = soup.find('p', class_="text-gray-550").text.strip()
            # update dictionary
            articledict[article_link] = [authors, article_tags, article_title, article_subtitle, totalbody]

def the_verge(articledict):
    '''(the verge doesn't have links to each article?)
    url = 'https://www.theverge.com/tech/'
    home_html = requests.get(url)
    soup = BeautifulSoup(home_html, 'html_parser')
    
    individual_articles = soup.findAll('a', class_=)
    '''
    
    url = "https://www.theverge.com/tech/"
    home_html = requests.get(url)
    soup = BeautifulSoup(home_html.content, 'html.parser')

    individual_articles = soup.findAll('a', class_="block h-full w-full")
    for individual_article in individual_articles:  
        article_link = "https://www.theverge.com" + individual_article['href']
        if not article_link in articledict.keys():
            individual_article_html = requests.get(article_link).content
            soup = BeautifulSoup(individual_article_html, 'html.parser')
            # get article body
            article_bodies = soup.findAll('div', class_ = 'duet--article--article-body-component')
            totalbody = []
            for article_body in article_bodies:
                ptags = article_body.findAll('p', class_='duet--article--dangerously-set-cms-markup duet--article--standard-paragraph mb-20 font-fkroman text-18 leading-160 -tracking-1 selection:bg-franklin-20 dark:text-white dark:selection:bg-blurple [&_a:hover]:shadow-highlight-franklin dark:[&_a:hover]:shadow-highlight-blurple [&_a]:shadow-underline-black dark:[&_a]:shadow-underline-white')
                
                for tag in ptags:
                    totalbody.extend(getarticlebody(ptags,"https://www.theverge.com"))
            #print(article_link)
            #print("------------------")
            #print(article_author)
            #get article tag
            article_tags = []
#            article_tags_list = soup.findAll('li', class_='inline font-polysans-mono text-12 font-medium uppercase tracking-12 text-blurple')
#            for li in article_tags_list:
#                tagelems = li.findAll('a')
#                for tagelem in tagelems:
#                    article_tags.append(tagelem.text)
#            print(article_tags)
            meta_article_tags = soup.find('meta', {'name':'parsely-tags'})
            article_tags = meta_article_tags.attrs.get('content').split(",")
            #print(article_tags) 

            # get article author(s)
            article_authors = soup.findAll('meta', {'name':'parsely-author'})
            authors = []
            for article_author in article_authors:
                authors.append(article_author.attrs.get('content'))
            #print(authors) 
            # article titles
            article_title = soup.find('h1').text
            article_subtitle = soup.find('h2').text
            # update dictionary
            articledict[article_link] = [authors, article_tags, article_title, article_subtitle, totalbody]

# make a python dictionary
#allarticles = {}
#arstechnica(allarticles)
#the_verge(allarticles)
#print(allarticles)