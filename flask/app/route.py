from flask import render_template

def hello_world():
    return "hello, mvc"

def index():
    return render_template('index.html')