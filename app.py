import pymongo 
from flask import Flask,render_template,redirect,url_for,flash,request,session,g
import mongo_setup 
import datetime
app = Flask(__name__)
app.secret_key = "dBCBAJBJCBHJBHBHJE*&^CHSAVCSACBADABCHJBJAH"
import services as sc
@app.route("/") #Runs the landing page which is still under construction
def index():
    return render_template("login.html")
@app.before_request  #The before_request decorator allows us to create a function that will run before each request.
def before_request():
    g.username = None
    if 'username' in session:
        g.username = session["username"] 

@app.route("/login",methods = ["POST","GET"])  #Every owner can be a user and a host. SO this ensures the login of that owner
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if sc.find_account_by_username_password(username,password):
            session["username"] = username 
             # use this session data for your account
            print("Logged in")
            return redirect(url_for("dashboard"))
        else:
            return redirect(url_for("register"))
    return   render_template("login.html")
@app.route("/signout") #Helps you end the session i.e logs you out
def signout():
    session.pop("username",None)
    return redirect(url_for("index"))
@app.route("/dashboard")  #This is the dashboard for your account (Owner)
def dashboard():
    if g.username:
        return render_template("dashboard.html",user = session["username"])
    return redirect(url_for("login"))
@app.route("/signin",methods=["POST","GET"]) #If you don't have an account this route helps you sign up into dog-bnb
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

@app.route("/register_doghouse",methods=["POST","GET"]) #Any owner can register his doghouse here
def register_doghouse():
    if request.method == "POST":
        inputData = dict(request.form)
        print(inputData)
        dh = sc.create_doghouse(inputData)
        a = sc.save_doghouse_user(str(session["username"]),dh)
        print(a.doghouse_ids)
        print(sc.find_doghouses_for_user(a))
        print("Dog house created!")
        return "Thanks for registering your doghouse! We will soon make sure that you get your bookings"
    return render_template("register_doghouse.html")
@app.route("/book_your_doghouse_as_host",methods=["POST","GET"]) #You can give your dog house for rent using this route
def book_your_doghouse_as_host():
    if request.method == "POST":
        inputData = dict(request.form)
        date_in = inputData["start_date"] # replace this string with whatever method or function collects your data
        date_processing = date_in.replace('T', '-').replace(':', '-').split('-')
        date_processing = [int(v) for v in date_processing]
        date_time_obj = datetime.datetime(*date_processing)
        print(date_time_obj) 
        a = sc.find_account_by_username(session["username"])
        all_doghouses = sc.find_doghouses_for_user(a)
        dh = sc.add_available_date(all_doghouses[int(inputData["doghouse_number"])-1],date_time_obj,inputData["days"])
    try:
        if(session["username"]):
            return render_template("book_your_doghouse_as_host.html")
    except:
        return "Please Login to continue"

# @app.route("/available_doghouses")
# def available_doghouses():
#     doghouses = sc.find_doghouses_for_user_session(session["username"])



if __name__=="__main__":
    mongo_setup.global_init() 
    app.run(debug=True)