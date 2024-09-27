from flask import Flask, render_template, request
import webscraper

app = Flask(__name__) # referencing this file

print(webscraper.returnpagedata())
@app.route('/', methods=['POST','GET'])
def index():
    myreq = request
    breakpoint()
    print(request)
    return render_template('index.html') 




app.run(host="0.0.0.0", port=5000) # run the app on localhost:80 running on all adddresses
