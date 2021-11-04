""" Addition Class """
from calculator.calculations.calculation import Calculation

class Addition(Calculation):

    def getResult(self):
        """ calculate the sum of the vals in self.vals """
        total = 0
        for val in self.vals:
            total += val
        return total
