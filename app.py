from flask import Flask, render_template, request, url_for
import webscraper

app = Flask(__name__) # referencing this file

print(webscraper.returnpagedata())
@app.route('/', methods=['POST','GET'])
def index():
    # Authentication
    

    # GET data
    #if request.method == "GET":
        #print(request.args)
        #print(request.args["EEE"]) # this is a query parameter

    return render_template('index.html') 




app.run(host="0.0.0.0", port=5000) # run the app on localhost:80 running on all adddresses
