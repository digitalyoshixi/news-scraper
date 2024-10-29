from flask import Flask, render_template, request, url_for
from flask_cors import CORS, cross_origin
#import webscraper

app = Flask(__name__) # referencing this file
cors = CORS(app)
app.config['CORS-HEADERS'] = 'Content-Type'

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html') 

@app.route('/scrape', methods=['POST'])
@cross_origin()
def scrape():
    # GET data
    if request.method == "POST":
        print(request.form)
    return request.form

app.run(host="0.0.0.0", port=5500,debug=True) # run the app on localhost:80 running on all adddresses
