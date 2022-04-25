from flask import render_template, request, session, redirect, url_for
from .model import Users, Products

def hello_world():
    return "hello, mvc"

def index():
    products = Products.query.all()
    return render_template("index.html", products=products)

def login():
    if request.method == "POST":
        result = Users.query.filter(
            Users.username == request.form["nm"]).first()
        if result:
            if result.password == request.form["pw"]:
                session["username"] = request.form["nm"]
                return redirect(url_for("home_page"))

            else:
                return "password is incorrect!!!", 400

        else:
            return "the name doesnt exist!!!", 400
    
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

def products(pid=None):
    message = '''<tr><td>id</td>
                     <td>name</td>
                     <td>stars</td>
                     <td>price</td>
                     <td>create_time</td></tr>'''
    if pid:
        data = Products.query.filter_by(id=pid).first()
        message += f'<tr><td>{data.id}</td><td>{data.name}</td><td>{data.stars}</td><td>{data.price}</td><td>{data.create_time}</td></tr>'

    else:
        result = Products.query.all()
        for data in result:
            message += f'<tr><td>{data.id}</td><td>{data.name}</td><td>{data.stars}</td><td>{data.price}</td><td>{data.create_time}</td></tr>'
    return f'<table>' + message + '</table>'