from app.controllers.controller import ControllerBase
from flask import render_template, request

class IndexController(ControllerBase):

    @staticmethod
    def post():
        nums = [int(num) for num in request.form["nums"].split()]


        return render_template("index.html")

    @staticmethod
    def get():
        return render_template('index.html')
