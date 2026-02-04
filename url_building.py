from flask import url_for
from flask import Flask

app = Flask(__name__)#initializing the app

@app.route("/")
def hello():
    return "Hello Nato"
@app.route("/login")
def login():
    return "Login"
@app.route("/user/<username>")#for user input <>
def profile(username):
    return f"(username)/'s profile"

with app.test_request_context():
    print(url_for('hello'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
