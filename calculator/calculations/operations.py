""" this file contains the math operation classes built on Calculation class """
from calculator.calculations.calculation import Calculation

class Addition(Calculation):
    """ calculate sum of numbers in self.vals """

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
    """
    save the first number in self.vals
    from this number subtract every subsequent number to calculate result
    """

    def get_result(self):
        """ calculate the sum of the vals in self.vals """
        total = self.vals[0]
        for val in self.vals[1:]:
            total -= val

        return total

class Multiplication(Calculation):
    """
    save the first number in self.vals
    then multiply this number by every subsequent number to get result
    """

    def get_result(self):
        """ calculate the sum of the vals in self.vals """
        total = self.vals[0]

        for val in self.vals[1:]:
            total *= val

        return total

class Division(Calculation):
    """
    save the first number in self.vals
    then divide this number by every subsequent number to get result
    """

    def get_result(self):
        """ calculate the sum of the vals in self.vals """
        total = self.vals[0]

        for val in self.vals[1:]:
            total /= val

        return total
