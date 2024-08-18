from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    """Returns a message that says 'welcome' when the /welcome route is hit"""
    return 'welcome'

@app.route('/welcome/home')
def welcome_home():
    """Returns a message that says 'welcome home' when the /welcome/home route is hit"""
    return 'welcome home'

@app.route('/welcome/back')
def welcome_back():
    """Returns a message that says 'welcome back' when the /welcome/back route is hit"""
    return 'welcome back'

