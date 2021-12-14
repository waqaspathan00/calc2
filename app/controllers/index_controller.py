""" handle POST and GET requests for the Calculator """

from flask import render_template, request, flash
from app.controllers.controller import ControllerBase
from calculator.main import Calculator

class IndexController(ControllerBase):
    """
        user can enter values and perform a math calculation on them
        values are entered in a textbox seperated by a space
        operation is chosen between 4 radio buttons
    """

    @staticmethod
    def post():
        """
            get the numbers entered from the form
            then perform calculation specified by user
        """
        # get the numbers entered in the textbox and turn it into a list of numbers
        nums = [int(num) for num in request.form["nums"].split()]

        if len(nums) < 2:
            flash('You need to calculate atleast 2 numbers', category="danger")
        else:
            flash('Successfully calculated', category="success")

            operation = request.form['operation']

            Calculator.calculate_numbers(operation, *nums)
            result = str(Calculator.get_last_result())

            return render_template('result.html', operation=operation, nums=nums, result=result)
        return render_template("index.html")

    @staticmethod
    def get():
        """ get the calculator page """
        return render_template('index.html')
