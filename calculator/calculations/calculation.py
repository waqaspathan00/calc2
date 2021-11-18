""" this module contains the calculation class """

# pylint: disable=too-few-public-methods
class Calculation:
    """
    this is an interface class for math operations to be built on top of
    when instantiated, it will take the numbers in a math calculation as parameters
    """

    def __init__(self, *vals):
        """ initialize Calculation object with vals """
        self.vals = vals

    @classmethod
    def create(cls, *vals):
        """ create Calculation object factory method """
        return cls(*vals)
