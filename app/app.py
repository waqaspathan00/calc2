"""A simple flask web app"""
from flask import Flask
from app.controllers.index_controller import IndexController
from app.controllers.history_controller import HistoryController

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/", methods=['GET'])
def index_get():
    return IndexController.get()

@app.route("/", methods=['POST'])
def index_post():
    return IndexController.post()

@app.route("/history")
def history():
    return HistoryController.get()

# @app.route("/calculator", methods=['GET'])
# def calculator_get():
#     return CalculatorController.get()
#
# @app.route("/calculator", methods=['POST'])
# def calculator_post():
#     return CalculatorController.post()
