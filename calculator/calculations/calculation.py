""" this is an interface class for math operations to be built on top of """

class Calculation:  # pylint: disable=too-few-public-methods
    """when instantiated, it will take the numbers in a math calculation as parameters"""

    def __init__(self, *vals):
        self.vals = vals
