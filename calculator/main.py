""" This is the Calculator object which can do basic calculator functions: +-*/ """
from calculator.calculations.operations import Addition, Subtraction, Multiplication, Division

class Calculator:
    """ This is the Calculator class"""

    history = []

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

        Calculator.history.append(total)

        return total.get_result()

    @staticmethod
    def subtract_number(*vals):
        """ subtract val from result """
        total = Subtraction(*vals)

        Calculator.history.append(total)

        return total.get_result()

    @staticmethod
    def multiply_number(*vals):
        """ multiply result by number """
        total = Multiplication(*vals)

        Calculator.history.append(total)

        return total.get_result()

    @staticmethod
    def divide_number(*vals):
        """ divide result by number """
        total = Division(*vals)

        Calculator.history.append(total)

        return total.get_result()

    @staticmethod
    def get_first_calculation():
        """ return the first calculation in Calculator history """
        return Calculator.history[0]

    @staticmethod
    def get_last_calculation():
        """ return the last calculation in Calculator history """
        return Calculator.history[-1]

    @staticmethod
    def get_num_of_calculations():
        """ return the number of calculations in Calculator history """
        return len(Calculator.history)

    @staticmethod
    def clear_history():
        """ remove all calculations in Calculator history """
        Calculator.history = []

    @staticmethod
    def remove_from_history(index):
        """ remove a calculation at specified index in Calculator history """
        Calculator.history.pop(index)
