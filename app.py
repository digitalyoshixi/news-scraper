from flask import Flask, render_template

app = Flask(__name__) # referencing this file

@app.route('/')
def index():
    return render_template('index.html') 

app.run(host="0.0.0.0", port=5000) # run the app on localhost:80 running on all adddresses
print("Abinash Commit")
