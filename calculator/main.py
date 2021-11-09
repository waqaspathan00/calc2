""" This is the Calculator object which can do basic calculator functions: +-*/ """
from calculator.calculations.operations import Addition, Subtraction, Multiplication, Division
from calculator.calculations.history import History

class Calculator:
    """ This is the Calculator class"""

    # IGNORE - CURRENTLY DEPRECATED
    # def __init__(self):
    #     self.result = 0
    #
    # def get_result(self):
    #     """ Get Result of Calculation"""
    #     return self.result

    @staticmethod
    def add_number(*vals):
        """ adds values to result """
        total = Addition(*vals)

        History.history.append(total)

        return total.get_result()

    @staticmethod
    def subtract_number(*vals):
        """ subtract val from result """
        total = Subtraction(*vals)

        History.history.append(total)

        return total.get_result()

    @staticmethod
    def multiply_number(*vals):
        """ multiply result by number """
        total = Multiplication(*vals)

        History.history.append(total)

        return total.get_result()

    @staticmethod
    def divide_number(*vals):
        """ divide result by number """
        total = Division(*vals)

        History.history.append(total)

        return total.get_result()
