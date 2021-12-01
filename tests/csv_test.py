import pytest
from calculator.helpers.csv_handler import Reader, Writer
from calculator.main import Calculator


def test_get_operation_name():
    """ this is a private function """
    # ARRANGE
    filepath = "tests/input_data/addition.csv"

    # ACT
    operation_name = Reader._get_operation_name(filepath)

    # ASSERT
    assert operation_name == "addition"

def operation_test_loop(rows, operation):
    # ARRANGE by looping through the test data and extracting vars
    for row in rows:
        expected_result = row[0]
        vals = row[1:]

        # ACT on the data by performing calculation
        calculated_result = Calculator.calculate_numbers(operation, *vals)

        # ASSERT that the expected and calculated are same result
        assert expected_result == calculated_result

def test_addition_using_file():
    """  """
    rows, operation = Reader.process_file("tests/input_data/addition.csv")

    operation_test_loop(rows, operation)

def test_subtraction_using_file():
    """  """
    rows, operation = Reader.process_file("tests/input_data/subtraction.csv")

    operation_test_loop(rows, operation)

def test_multiplication_using_file():
    """  """
    rows, operation = Reader.process_file("tests/input_data/multiplication.csv")

    operation_test_loop(rows, operation)

def test_division_using_file():
    """  """
    rows, operation = Reader.process_file("tests/input_data/division.csv")

    with pytest.raises(ZeroDivisionError):
        # operation_test_loop(rows, operation)
        for row in rows:
            expected_result = row[0]
            vals = row[1:]
            calculated_result = Calculator.calculate_numbers(operation, *vals)

            assert expected_result == calculated_result

def test_large_addition_using_file():
    """  """
    rows, operation = Reader.process_file("tests/input_data/large_addition.csv")

    operation_test_loop(rows, operation)

def test_large_subtraction_using_file():
    """  """
    rows, operation = Reader.process_file("tests/input_data/large_subtraction.csv")

    operation_test_loop(rows, operation)

def test_large_multiplication_using_file():
    """  """
    rows, operation = Reader.process_file("tests/input_data/large_multiplication.csv")

    operation_test_loop(rows, operation)
