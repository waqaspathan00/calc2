""" This is the Calculator object which can do basic calculator functions: +-*/ """
from calculator.helpers.history import History

class Calculator:
    """ This is the Calculator class"""

    @staticmethod
    def add_number(*vals):
        """ performs addition and returns resulting value """
        History.add_addition_calculation(*vals)
        return Calculator.get_last_result()

    @staticmethod
    def subtract_number(*vals):
        """ performs subtraction and returns resulting value """
        History.add_subtraction_calculation(*vals)
        return Calculator.get_last_result()

    @staticmethod
    def multiply_number(*vals):
        """ performs addition and returns resulting value """
        History.add_multiplication_calculation(*vals)
        return Calculator.get_last_result()

    @staticmethod
    def divide_number(*vals):
        """ performs addition and returns resulting value """
        History.add_division_calculation(*vals)
        return Calculator.get_last_result()

    @staticmethod
    def get_last_result():
        """ return the result of the last calculation """
        calculation = History.get_last_calculation()
        return calculation.get_result()
