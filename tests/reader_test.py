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
    results = Calculator.calculate_file("tests/test_data/addition.csv")

    for result in results:
        expected = result[0]
        calculated = result[1]

        assert expected == calculated
