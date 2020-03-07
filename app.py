from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    
    # to get the current date
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day == 1

    return render_template("index.html", new_year=new_year)

@app.route("/<string:name>")
def para(name):
    return f"hello {name}!!"