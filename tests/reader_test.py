from calculator.helpers.csv_reader import Reader
from calculator.main import Calculator

def test_get_operation_name():
    # ARRANGE
    reader = Reader("tests/test_data/addition.csv")

    # ACT
    operation_name = reader.get_operation_name()

    # ASSERT
    assert operation_name == "addition"

def test_calculate_using_file():
    reader = Reader("tests/test_data/addition.csv")
    operation = reader.operation

    for row in reader.rows:
        expected_result = row[0]
        vals = row[1:]
        calculated_result = Calculator.calculate_numbers(operation, *vals)

        assert expected_result == calculated_result

"""
make a fixture to load the csv file and perform calculations
one file with 4 results for each op and set of numbers to be calculated
"""
