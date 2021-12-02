""" this module contains the History class """
from calculator.calculations.operations import Addition, Subtraction, Multiplication, Division

class History:
    """
    this class has no need to be instantiated as all of its attr and func are static
    this class should not be accessed directly and should only be used through the Calculator
    """
    history = []

    @staticmethod
    def add_addition_calculation(*vals):
        """ add Addition object with vals to history """
        History.history.append(Addition.create(*vals))

    @staticmethod
    def add_subtraction_calculation(*vals):
        """ add Subtraction object with vals to history """
        History.history.append(Subtraction.create(*vals))

    @staticmethod
    def add_multiplication_calculation(*vals):
        """ add Multiplication object with vals to history """
        History.history.append(Multiplication.create(*vals))

    @staticmethod
    def add_division_calculation(*vals):
        """ add Division object with vals to history """
        History.history.append(Division.create(*vals))

    @staticmethod
    def get_first_calculation():
        """ return the first calculation in history """
        return History.history[0]

    @staticmethod
    def get_last_calculation():
        """ return the last calculation in history """
        return History.history[-1]

    @staticmethod
    def get_num_of_calculations():
        """ return the number of calculations in history """
        return len(History.history)

    @staticmethod
    def clear_history():
        """ remove all calculations in history """
        History.history = []

    @staticmethod
    def remove_from_history(index: int):
        """ remove a calculation at specified index in history """
        History.history.pop(index)
