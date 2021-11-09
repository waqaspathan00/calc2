class History:
    history = []

    @staticmethod
    def get_first_calculation():
        """ return the first calculation in Calculator history """
        return History.history[0]

    @staticmethod
    def get_last_calculation():
        """ return the last calculation in Calculator history """
        return History.history[-1]

    @staticmethod
    def get_num_of_calculations():
        """ return the number of calculations in Calculator history """
        return len(History.history)

    @staticmethod
    def clear_history():
        """ remove all calculations in Calculator history """
        History.history = []

    @staticmethod
    def remove_from_history(index):
        """ remove a calculation at specified index in Calculator history """
        History.history.pop(index)
