from flask import Flask, render_template, request, url_for
from flask_cors import CORS, cross_origin
from llamamodel import getresp

#import webscraper

app = Flask(__name__) # referencing this file
cors = CORS(app)
app.config['CORS-HEADERS'] = 'Content-Type'

@app.route('/', methods=['GET'])
def index():
    articles = [
            ["Title 1", "News Outlet 1", "/static/images/someimage.png", "Some description here"],
            ["Title 2", "Some News Outlet", "/static/images/someimage.png", "Some description here"],
            ]
    return render_template('index.html', articles=articles) 

@app.route('/scrape', methods=['POST'])
@cross_origin()
def scrape():
    # GET data
    if request.method == "POST":
        print(request.form)
    return request.form

app.run(host="0.0.0.0", port=5500,debug=True) # run the app on localhost:80 running on all adddresses
