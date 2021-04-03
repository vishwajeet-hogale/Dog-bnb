import pymongo 
from flask import Flask,render_template,redirect,url_for,flash,request
import mongo_setup 
app = Flask(__name__)
app.secret_key = "dBCBAJBJCBHJBHBHJE*&^CHSAVCSACBADABCHJBJAH"
@app.route("/")
def index():
    return render_template("index.html")

if __name__=="__main__":
    mongo_setup.global_init() 
    app.run(debug=True)