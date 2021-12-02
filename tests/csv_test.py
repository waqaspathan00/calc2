""" run Calculation tests using CSV data files """

import pytest
from calculator.helpers.csv_handler import Reader, Writer
from calculator.main import Calculator

def test_get_operation_name():
    """ check for operation type being properly extracted from filepath """
    # ARRANGE
    filepath = "tests/input_data/addition.csv"

    # ACT
    operation_name = Reader.get_operation_name(filepath)

    # ASSERT
    assert operation_name == "addition"

def operation_test_loop(rows, operation):
    """
    loop through rows of data
    assert correctness of expected vs calculated results
    """
    # ARRANGE by looping through the test data and extracting vars
    for row in rows:
        expected_result = row[0]
        vals = row[1:]

        # ACT on the data by performing calculation
        calculated_result = Calculator.calculate_numbers(operation, *vals)

        # ASSERT that the expected and calculated are same result
        assert expected_result == calculated_result


@pytest.mark.parametrize("filename", [
    "addition.csv", "subtraction.csv", "multiplication.csv",
    "large_addition.csv", "large_subtraction.csv",
    "large_multiplication.csv",
])
def test_math_operations_using_file(filename):
    """
    loop through the rows of ADDITION SUBTRACTION and MULTIPLICATION data
    assert correctness of the expected vs calculated result
    """
    # ARRANGE
    filepath = "tests/input_data/" + filename
    rows, operation = Reader.process_file(filepath)

    operation_test_loop(rows, operation)

    Writer.write_log(filepath)

@pytest.mark.parametrize("filename", ["division.csv", "large_division.csv"])
def test_division_operation_using_file(filename):
    """
    loop through the rows of DIVISION data
    assert correctness of the expected vs calculated result
    """
    # ARRANGE
    filepath = "tests/input_data/" + filename
    rows, operation = Reader.process_file(filepath)

    with pytest.raises(ZeroDivisionError):
        operation_test_loop(rows, operation)

    Writer.write_division_log()
