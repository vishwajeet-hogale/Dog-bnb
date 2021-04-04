import pymongo 
from flask import Flask,render_template,redirect,url_for,flash,request,session,g
import mongo_setup 
app = Flask(__name__)
app.secret_key = "dBCBAJBJCBHJBHBHJE*&^CHSAVCSACBADABCHJBJAH"
import services as sc
@app.route("/")
def index():
    return render_template("login.html")


@app.before_request
def before_request():
    g.username = None
    if 'username' in session:
        g.username = session["username"] 
@app.route("/login",methods = ["POST","GET"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if sc.find_account_by_username_password(username,password):
            session["username"] = username  # use this session data for your account
            print("Logged in")
            return redirect(url_for("dashboard"))
        else:
            return redirect(url_for("register"))
    return   render_template("login.html")
@app.route("/signout")
def signout():
    session.pop("username",None)
    return render_template("login.html")
@app.route("/dashboard")
def dashboard():
    if g.username:
        return render_template("dashboard.html",user = session["username"])
    return redirect(url_for("login"))
@app.route("/signin",methods=["POST","GET"])
def register():
    if request.method == "POST":
        name = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]
        old_accnt = sc.find_account_by_email(email)
        if old_accnt:
            print(f"Account with email {email} already exists!")
        else:
            sc.create_account(name,email,password)
            print("Account createdddd")
        print("Account Created!!!!")
        return redirect(url_for("login"))
    return render_template("signin.html")
if __name__=="__main__":
    mongo_setup.global_init() 
    app.run(debug=True)