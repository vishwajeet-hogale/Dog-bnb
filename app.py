import pymongo 
from Flask import Flask,request,render_template,flash

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello"

if __name__=="__main__":
    app.run(debug=True)