from flask import render_template, request, session, redirect, url_for

def hello_world():
    return "hello, mvc"

def index():
    return render_template("index.html")

def login():
    username = request.args.get('username')
    password = request.args.get('password')
    session['username'] = username
    return f"successful login!"

def logout():
    session.pop('username')
    return redirect(url_for("index"))

def home_page():
    if 'username' in session:
        return f"this is {session['username']} page!"

    else:
        return "none one page!"
