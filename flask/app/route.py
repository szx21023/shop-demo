from flask import render_template, request, session, redirect, url_for

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

def home_page():
    if 'username' in session:
        return f"this is {session['username']} page!"

    else:
        return "none one page!"
