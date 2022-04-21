from flask_sqlalchemy import SQLAlchemy
from flask import Flask

# for docker-compose
DB_USER = 'root'
DB_PASS = 'test1234'
DB_HOST = 'mysql'
DB_PORT = '3306'
DB_NAME = 'test'
# for develop
# DB_HOST = 'localhost'
# DB_PORT = '33060'
db = SQLAlchemy()

def create_app():
    from app.route import hello_world, index, login, logout, shopping_carts, shopping, home_page, users, products
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret'
    app.add_url_rule('/', '/', hello_world)
    app.add_url_rule('/index', 'index', index)
    app.add_url_rule('/login', 'login', login, methods=["POST", "GET"])
    app.add_url_rule('/logout', 'logout', logout)
    app.add_url_rule('/shopping_carts', 'shopping_carts', shopping_carts)
    app.add_url_rule('/shopping', 'shopping', shopping)
    app.add_url_rule('/home_page', 'home_page', home_page)
    app.add_url_rule('/users', 'users', users)
    app.add_url_rule('/products', 'products', products)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    db.init_app(app)
    return app
