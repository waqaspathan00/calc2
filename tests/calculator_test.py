""" testing the Calculator """
import pytest
from calculator.main import Calculator
from calculator.calculations.history import History

# RESULT IS DEPRECATED
# def test_calculator_result():
#     """ Testing calculator result is 0 """
#     calc = Calculator()
#     assert calc.result == 0
#
# def test_calculator_get_result():
#     """ Testing the Get result method of the calculator """
#     calc = Calculator()
#
#     assert calc.get_result() == 0

@pytest.fixture
def clear_history():
    """ creates an instance of a Calculator with empty history """
    History.clear_history()

@pytest.fixture
def new_calculator():
    return Calculator()

def test_add(new_calculator):
    """ testing the Add function of the calculator """
    # ARRANGE by instantiating the calc class using pytest fixture

    # ACT by calling the method to be tested
    total = new_calculator.add_number(1, 2, 3)

    # ASSERT that the results are correct
    assert total == 6

def test_calculator_subtract(new_calculator):
    """ Testing the subtract method of the calculator """
    result = new_calculator.subtract_number(10, 8)
    assert result == 2

def test_calculator_multiply(new_calculator):
    """ Testing the multiply method of the calculator """
    result = new_calculator.multiply_number(2, 3, 2)
    assert result == 12

def test_calculator_divide(new_calculator):
    """ Testing the divide method of the calculator """
    result = new_calculator.divide_number(20, 2)
    assert result == 10

def test_calculator_divide_by_zero(new_calculator):
    """ Testing divide by zero on divide method of calculator"""

    # the 'with' keyword here is saying the following block of code must throw given exception
    with pytest.raises(ZeroDivisionError):
        result = new_calculator.divide_number(10, 0)
