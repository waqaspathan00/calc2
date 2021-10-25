""" This is the Calculator object which can do basic calculator functions: +-*/ """

class Calculator:
    """ This is the Calculator class"""

    def __init__(self, starting_result=0):
        self.result = starting_result

    def get_result(self):
        """ Get Result of Calculation"""
        return self.result

    def add_number(self, *vals):
        """ adds val to result"""
        for val in vals:
            self.result += val

        return self.result

    def subtract_number(self, *vals):
        """ subtract val from result """
        for val in vals:
            self.result -= val

        return self.result

    def multiply_number(self, *vals):
        """ multiply result by number """
        for val in vals:
            self.result *= val

        return self.result

    def divide_number(self, *vals):
        """ divide result by number """
        for val in vals:
            self.result /= val

        return self.result
