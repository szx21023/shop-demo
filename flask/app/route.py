from flask import render_template, request, session, redirect, url_for
from .model import Users

def hello_world():
    return "hello, mvc"

def index():
    return render_template("index.html")

def login():
    if request.method == "POST":
        user = request.form["nm"]
        session["username"] = user
        return redirect(url_for("home_page"))
    
    else:
        if "username" in session:
            return redirect(url_for("home_page"))

        return render_template("login.html")

def logout():
    session.pop('username')
    return redirect(url_for("index"))

def shopping_cart():
    if "username" in session:
        return f"hello mr.{session['username']}"

    else:
        return redirect(url_for("login"))

def home_page():
    if 'username' in session:
        return f"this is {session['username']} page!"

    else:
        return "none one page!"

def users():
    result = Users.query.all()
    for data in result:
        print(data.username, data.password, data.phone, data.email, data.create_time)
    return 'ok'