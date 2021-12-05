from app.controllers.controller import ControllerBase
from flask import render_template, request
from calculator.main import Calculator

class IndexController(ControllerBase):

    @staticmethod
    def post():
        """
        get the numbers entered from the form
        then perform calculation specified by user
        """
        nums = [int(num) for num in request.form["nums"].split()]
        operation = request.form['operation']

        Calculator.calculate_numbers(operation, *nums)
        result = str(Calculator.get_last_result())

        return render_template('result.html', operation=operation, nums=nums, result=result)

    @staticmethod
    def get():
        return render_template('index.html')
