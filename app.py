from flask import Flask, render_template, request, url_for
import webscraper

app = Flask(__name__) # referencing this file

print(webscraper.returnpagedata())
@app.route('/', methods=['GET'])
def index():


    return render_template('index.html') 


@app.route('/scrape', methods=['POST'])
def scrape():
    # GET data
    if request.method == "POST":
        urltoscrape = request.form['url']
    return render_template('index.html') # return homepage



app.run(host="0.0.0.0", port=5000) # run the app on localhost:80 running on all adddresses
