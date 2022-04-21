from flask import render_template, request, session, redirect, url_for
from .model import Users, Products, Shopping_carts
from . import db

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

def products():
    result = Products.query.all()
    for data in result:
        print(data.name, data.stars, data.price, data.create_time)
    return 'ok'

def shopping_carts():
    result = Shopping_carts.query.all()
    for data in result:
        print(f'id: {data.id}, user: {data.user_id}, product: {data.product_id}, create_time: {data.create_time}')
    return 'ok'

def shopping():
    cart_1 = Shopping_carts(1, 1)
    cart_2 = Shopping_carts(100, 100)
    db.session.add_all([cart_1, cart_2])
    db.session.commit()
    query = Shopping_carts.query.first()
    print(query.products.id, query.products.price)
    return 'ok'