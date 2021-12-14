""" flask calculator web app """

from flask import Flask
from app.controllers.index_controller import IndexController
from app.controllers.history_controller import HistoryController

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/", methods=['GET'])
def index_get():
    """ GET the homepage """
    return IndexController.get()

@app.route("/", methods=['POST'])
def index_post():
    """
    when POST request made:
        if valid, reroute to result.html
        else remain on page and show errors
    """
    return IndexController.post()

@app.route("/history", methods=['GET'])
def history_get():
    """ GET the calculation history """
    return HistoryController.get()

@app.route("/history", methods=['POST'])
def history_post():
    """ handle history POST request """
    return HistoryController.post()

