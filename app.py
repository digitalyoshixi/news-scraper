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
        print(request.form)
        urltoscrape = request.form['url']

app.run(host="0.0.0.0", port=5500,debug=True) # run the app on localhost:80 running on all adddresses
