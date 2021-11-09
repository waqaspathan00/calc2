""" this module contains the History class """

class History:
    """
    this class has no need to be instantiated as all of its attr and func are static
    this class should not be accessed directly and should only be used through the Calculator
    """
    history = []

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
    def remove_from_history(index):
        """ remove a calculation at specified index in history """
        History.history.pop(index)
