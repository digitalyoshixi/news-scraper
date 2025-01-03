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

def sanitizestring(inpstr : str) -> str:
    """
    For any strings that have ' as a substring within the main string, replace that with the character 

    """
    liststr = list(inpstr)
    for i in range(len(liststr)):
        if liststr[i] == "\'":
            liststr[i]  = "’"
    return ''.join(liststr)
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
                    paragraph.append([sanitizestring(oktext),""])
                    toadd = atags.pop(0)
                    toadd[0] = sanitizestring(toadd[0])
                    toadd[1] = sanitizestring(toadd[1])
                    paragraph.append(toadd)
                paragraph.append([sanitizestring(temptag[lastindex:]),''])
                #paragraph.append(['Hi im hay',''])
                totalbody.append(paragraph)
                #breakpoint()
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
                for i in getarticlebody(ptags):
                    totalbody.extend(i)
            article_tags = []
            #breakpoint()
            article_authors = soup.findAll('a', class_="text-orange-400 hover:text-orange-500")
            authors = []
            for article_author in article_authors:
                authors.append(article_author.text.strip())
            article_title = sanitizestring(soup.find('h1', class_="mb-3").text.strip())
            article_subtitle = sanitizestring(soup.find('p', class_="text-gray-550").text.strip())
            imageurl = soup.find('img', class_="intro-image")['src']
            # update dictionary
            articledict[article_link] = [authors, article_tags, article_title, article_subtitle, totalbody, imageurl]

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
                for i in getarticlebody(ptags, "https://www.theverge.com"):
                    totalbody.extend(i)
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
            # image url
            imageurl = soup.find('img', attrs={
                'style' : "position:absolute;top:0;left:0;bottom:0;right:0;box-sizing:border-box;padding:0;border:none;margin:auto;display:block;width:0;height:0;min-width:100%;max-width:100%;min-height:100%;max-height:100%;object-fit:cover"
            })['src']
            article_bodies = soup.findAll('div', class_="post-content post-content-double")
            # update dictionary
            articledict[article_link] = [authors, article_tags, article_title, article_subtitle, totalbody, imageurl]

# make a python dictionary
#allarticles = {}
#arstechnica(allarticles)
#the_verge(allarticles)
#print(allarticles)