from flask import Flask
from app.route import hello_world, index, login, logout, home_page

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret'
    app.add_url_rule('/', '/', hello_world)
    app.add_url_rule('/index', 'index', index)
    app.add_url_rule('/login', 'login', login, methods=["POST", "GET"])
    app.add_url_rule('/logout', 'logout', logout)
    app.add_url_rule('/home_page', 'home_page', home_page)
    return app
