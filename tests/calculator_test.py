"""Testing the Calculator"""
import pytest
from calculator.main import Calculator

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

def test_add():
    """ Testing the Add function of the calculator """
    # ARRANGE by instantiating the calc class
    calc = Calculator()

    # ACT by calling the method to be tested
    total = calc.add_number(1, 2, 3)

    # ASSERT that the results are correct
    assert total == 6

def test_get_first_calculation():
    """ evaluate the result of the first calculation in history """
    calc = Calculator()

    calculation = calc.get_first_calculation()

    assert calculation.get_result() == 6

def test_add_and_get_last_calculation():
    """ evaluate the result of the last calculation in history """
    calc = Calculator()

    calc.add_number(3, 4)
    calc.add_number(5, 5)
    calculation = calc.get_last_calculation()

    assert calculation.get_result() != 7
    assert calculation.get_result() == 10

def test_number_of_calculations_in_history():
    """ test that all previous calculations were added to history """
    calc = Calculator()

    assert calc.get_num_of_calculations() == 3

def test_remove_calculation_from_history():
    """
    remove calculation at index 2 of history
    then test if the 2nd calculation is the new last
    """
    calc = Calculator()

    calc.remove_from_history(2)
    calculation = calc.get_last_calculation()

    assert calculation.get_result() == 7

def test_number_of_calculations_in_history_after_clearing():
    """ clear the history then test to see if length of history is 0 (empty) """
    calc = Calculator()

    calc.clear_history()

    assert calc.get_num_of_calculations() == 0

def test_calculator_subtract():
    """ Testing the subtract method of the calculator """
    calc = Calculator()

    calc.subtract_number(10, 8)

    calculation = calc.get_last_calculation()

    assert calculation.get_result() == 2

def test_calculator_multiply():
    """ Testing the multiply method of the calculator """
    calc = Calculator()

    calc.multiply_number(2, 3, 2)

    calculation = calc.get_last_calculation()

    assert calculation.get_result() == 12

def test_calculator_divide():
    """ Testing the divide method of the calculator """
    calc = Calculator()

    calc.divide_number(20, 2)

    calculation = calc.get_last_calculation()

    assert calculation.get_result() == 10

def test_calculator_divide_by_zero():
    """ Testing divide by zero on divide method of calculator"""

    # the 'with' keyword here is saying the following block of code must throw given exception
    with pytest.raises(ZeroDivisionError):
        calc = Calculator()
        calc.divide_number(10, 0)
