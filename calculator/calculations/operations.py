""" Addition Class """
from calculator.calculations.calculation import Calculation

class Addition(Calculation):

    # CONSTRUCTOR CALLING SUPER use this if you want to take more parameters
    # def __init__(self, *vals):
    #     super().__init__(*vals)

    def get_result(self):
        """ calculate the sum of the vals in self.vals """
        total = 0
        for val in self.vals:
            total += val
        return total

class Subtraction(Calculation):

    def get_result(self):
        """ calculate the sum of the vals in self.vals """
        total = 0
        for val in self.vals:
            total -= val

        return total

# class Multiplication(Calculation):
#
#     def getResult(self):
#         """ calculate the sum of the vals in self.vals """
#         total = 1
#         for val in self.vals:
#             total *= val
#
#         return total
#
# class Division(Calculation):
#
#     def getResult(self):
#         """ calculate the sum of the vals in self.vals """
#         total = 1
#         for val in self.vals:
#             total += val
#         return total
