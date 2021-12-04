""" this file contains the math operation classes built on Calculation class """
from calculator.calculations.calculation import Calculation

class Addition(Calculation):  # pylint: disable=too-few-public-methods
    """ calculate sum of numbers in self.vals """

    def get_result(self):
        """ calculate the sum of the vals in self.vals """
        total = 0
        for val in self.vals:
            total += int(val)
        return total

class Subtraction(Calculation):  # pylint: disable=too-few-public-methods
    """
    save the first number in self.vals
    from this number subtract every subsequent number to calculate result
    """

    def get_result(self):
        """ calculate the sum of the vals in self.vals """
        total = int(self.vals[0])

        for val in self.vals[1:]:
            total -= int(val)

        return total

class Multiplication(Calculation):  # pylint: disable=too-few-public-methods
    """
    save the first number in self.vals
    then multiply this number by every subsequent number to get result
    """

    def get_result(self):
        """ calculate the sum of the vals in self.vals """
        total = int(self.vals[0])

        for val in self.vals[1:]:
            total *= int(val)

        return total

class Division(Calculation):  # pylint: disable=too-few-public-methods
    """
    save the first number in self.vals
    then divide this number by every subsequent number to get result
    """

    def get_result(self):
        """ calculate the sum of the vals in self.vals """
        total = int(self.vals[0])

        for val in self.vals[1:]:
            if int(val == 0):
                raise ZeroDivisionError("Divide by zero error")
            total /= int(val)

        return int(total)
