""" This is the Calculator object which can do basic calculator functions: +-*/ """
from calculator.helpers.history import History
from calculator.helpers.csv_reader import Reader

class Calculator:
    """ This is the Calculator class"""

    @staticmethod
    def calculate_file(filename):
        """
        read a file and perform required math calculation using filename
        return a 2d list with following format for each item - [expected_result, calculated_result]
            - expected_result, value we expect from calculation gotten from each line in the file
            - calculated_result, the value we calculate from the numbers in the file
        """

        reader = Reader(filename)
        operation = reader.operation
        results = []

        for row in reader.rows:
            expected_result = row[0]
            vals = row[1:]
            calculated_result = Calculator.calculate_numbers(operation, *vals)

            results.append([expected_result, calculated_result])

        return results

    @staticmethod
    def calculate_numbers(operation, *vals):
        if operation == "addition":
            return Calculator.add_number(*vals)
        elif operation == "subtraction":
            return Calculator.subtract_number(*vals)
        elif operation == "multiplication":
            return Calculator.multiply_number(*vals)
        elif operation == "division":
            return Calculator.divide_number(*vals)

    @staticmethod
    def add_number(*vals):
        """ performs addition and returns resulting value """
        History.add_addition_calculation(*vals)
        return Calculator.get_last_result()

    @staticmethod
    def subtract_number(*vals):
        """ performs subtraction and returns resulting value """
        History.add_subtraction_calculation(*vals)
        return Calculator.get_last_result()

    @staticmethod
    def multiply_number(*vals):
        """ performs addition and returns resulting value """
        History.add_multiplication_calculation(*vals)
        return Calculator.get_last_result()

    @staticmethod
    def divide_number(*vals):
        """ performs addition and returns resulting value """
        History.add_division_calculation(*vals)
        return Calculator.get_last_result()

    @staticmethod
    def get_last_result():
        """ return the result of the last calculation """
        calculation = History.get_last_calculation()
        return calculation.get_result()
