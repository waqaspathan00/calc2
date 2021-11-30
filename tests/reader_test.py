import pytest
from calculator.helpers.csv_handler import Reader
from calculator.main import Calculator


def test_get_operation_name():
    """  """
    # ARRANGE
    reader = Reader("tests/input_data/addition.csv")

    # ACT
    operation_name = reader._get_operation_name()

    # ASSERT
    assert operation_name == "addition"

def test_addition_using_file():
    """  """
    reader = Reader("tests/input_data/addition.csv")
    operation = reader.operation

    for row in reader.rows:
        expected_result = row[0]
        vals = row[1:]
        calculated_result = Calculator.calculate_numbers(operation, *vals)

        assert expected_result == calculated_result

def test_subtraction_using_file():
    """  """
    reader = Reader("tests/input_data/subtraction.csv")
    operation = reader.operation

    for row in reader.rows:
        expected_result = row[0]
        vals = row[1:]
        calculated_result = Calculator.calculate_numbers(operation, *vals)

        assert expected_result == calculated_result

def test_multiplication_using_file():
    """  """
    reader = Reader("tests/input_data/multiplication.csv")
    operation = reader.operation

    for row in reader.rows:
        expected_result = row[0]
        vals = row[1:]
        calculated_result = Calculator.calculate_numbers(operation, *vals)

        assert expected_result == calculated_result

def test_division_using_file():
    """  """
    reader = Reader("tests/input_data/division.csv")
    operation = reader.operation

    # why does this work?
    # what if i run a test file that doesnt divide by 0

    with pytest.raises(ZeroDivisionError):
        for row in reader.rows:
            expected_result = row[0]
            vals = row[1:]
            calculated_result = Calculator.calculate_numbers(operation, *vals)

        assert expected_result == calculated_result

def test_large_addition_using_file():
    """  """
    reader = Reader("tests/input_data/large_addition.csv")
    operation = reader.operation

    for row in reader.rows:
        expected_result = row[0]
        vals = row[1:]
        calculated_result = Calculator.calculate_numbers(operation, *vals)

        assert expected_result == calculated_result

def test_large_subtraction_using_file():
    """  """
    reader = Reader("tests/input_data/large_subtraction.csv")
    operation = reader.operation

    for row in reader.rows:
        expected_result = row[0]
        vals = row[1:]
        calculated_result = Calculator.calculate_numbers(operation, *vals)

        assert expected_result == calculated_result

def test_large_multiplication_using_file():
    """  """
    reader = Reader("tests/input_data/large_multiplication.csv")
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
