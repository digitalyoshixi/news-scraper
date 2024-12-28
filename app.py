from flask import Flask, render_template, request, url_for
from flask_cors import CORS, cross_origin
from llamamodel import getresp
from dboperations import get_recent_articles
#import webscraper

app = Flask(__name__) # referencing this file
cors = CORS(app)
app.config['CORS-HEADERS'] = 'Content-Type'

@app.route('/', methods=['GET'])
def index():
    articles = get_recent_articles()
    # an article has:
    """
    0 : id int
    1 : date-time object
    2 : url string
    3 : authors list
    4 : content double matrix
    5 : tags list
    6 : title string
    7 : subtitle string
    """
    return render_template('index.html', articles=articles) 

@app.route('/scrape', methods=['POST'])
@cross_origin()
def scrape():
    # GET data
    if request.method == "POST":
        print(request.form)
    return request.form

app.run(host="0.0.0.0", port=5500,debug=False) # run the app on localhost:5500 running on all adddresses (AUTORELOADER IS DISABLED)
