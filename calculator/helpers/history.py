""" this module contains the History class """
from calculator.calculations.operations import Addition, Subtraction, Multiplication, Division
from calculator.helpers.csv_handler import Writer

class History:
    """
    this class has no need to be instantiated as all of its attr and func are static
    this class should not be accessed directly and should only be used through the Calculator
    """
    history = []

    @staticmethod
    def add_addition_calculation(*vals):
        """ add Addition object with vals to history """
        new_calculation = Addition.create(*vals)
        History.write_calculation(new_calculation)

    @staticmethod
    def add_subtraction_calculation(*vals):
        """ add Subtraction object with vals to history """
        new_calculation = Subtraction.create(*vals)
        History.write_calculation(new_calculation)

    @staticmethod
    def add_multiplication_calculation(*vals):
        """ add Multiplication object with vals to history """
        new_calculation = Multiplication.create(*vals)
        History.write_calculation(new_calculation)

    @staticmethod
    def add_division_calculation(*vals):
        """ add Division object with vals to history """
        new_calculation = Division.create(*vals)
        History.write_calculation(new_calculation)

    @staticmethod
    def write_calculation(new_calculation):
        History.history.append(new_calculation)

        operation = History.operation_names[type(new_calculation)]
        result = new_calculation.get_result()
        vals = new_calculation.vals

        row = [operation, result, vals]

        Writer.write_line("app/data.csv", row)

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
        filename = "app/data.csv"
        # opening the file with w+ mode truncates the file
        f = open(filename, "w+")
        f.write("operation, result, numbers\n")
        f.close()

    @staticmethod
    def remove_from_history(index: int):
        """ remove a calculation at specified index in history """
        History.history.pop(index)


History.operation_names = {
    Addition: "addition",
    Subtraction: "subtraction",
    Multiplication: "multiplication",
    Division: "division",
}
