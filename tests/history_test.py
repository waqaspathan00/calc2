""" testing the History """
import pytest
from calculator.main import Calculator
from calculator.calculations.history import History

@pytest.fixture(name="clear_history")
def fixture_clear_history():
    """ creates an instance of a Calculator with empty history """
    History.clear_history()

@pytest.fixture(name="used_calculator")
def fixture_used_calculator():
    """ return a Calculator object with 4 completed math operations """
    calculator = Calculator()

    calculator.add_number(2, 4)         # 6
    calculator.multiply_number(3, 8)    # 24
    calculator.subtract_number(10, 2)   # 8
    calculator.divide_number(15, 3)     # 5

    return calculator

# pylint: disable=unused-argument
def test_number_of_calculations_in_history_after_clearing(used_calculator, clear_history):
    """ clear the history then test to see if length of history is 0 (empty) """
    assert History.get_num_of_calculations() == 0

# pylint: disable=unused-argument
def test_get_first_calculation(clear_history, used_calculator):
    """ evaluate the result of the first calculation in history """
    # ARRANGE by performing some calculations using pytest fixture: used_calculator

    # ACT by getting the first calculation
    calculation = History.get_first_calculation()

    # ASSERT by confirming the result of the first calculation
    assert calculation.get_result() == 6

# pylint: disable=unused-argument
def test_get_last_calculation(clear_history, used_calculator):
    """ evaluate the result of the last calculation in history """
    calculation = History.get_last_calculation()
    assert calculation.get_result() == 5

# pylint: disable=unused-argument
def test_number_of_calculations_in_history(clear_history, used_calculator):
    """ test completion of 4 calculations from pytest fixture used_calculator """
    assert History.get_num_of_calculations() == 4

# pylint: disable=unused-argument
def test_remove_calculation_from_history(clear_history, used_calculator):
    """
    there should currently be 4 calculations in history
    remove calculation at index 3 of history
    then test if the 3rd calculation is the new last
    """
    History.remove_from_history(3)
    calculation = History.get_last_calculation()
    assert calculation.get_result() == 8
