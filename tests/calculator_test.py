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
    calc = Calculator()

    calculation = calc.get_first_calculation()

    assert calculation.get_result() == 6

def test_add_and_get_last_calculation():
    calc = Calculator()

    calc.add_number(3, 4)
    calc.add_number(5, 5)
    calculation = calc.get_last_calculation()

    assert calculation.get_result() != 7
    assert calculation.get_result() == 10

def test_number_of_calculations_in_history():
    calc = Calculator()

    assert calc.get_num_of_calculations() == 3


def test_number_of_calculations_in_history_after_clearing():
    calc = Calculator()

    calc.clear_history()

    assert calc.get_num_of_calculations() == 0

def test_calculator_subtract():
    """ Testing the subtract method of the calculator """
    calc = Calculator()

    calc.subtract_number(1)

    calculation = calc.get_last_calculation()

    assert calculation.get_result() == -1

# def test_calculator_multiply():
#     """ Testing the multiply method of the calculator """
#     calc = Calculator()
#     calc.multiply_number(1)
#     assert calc.get_result() == 0
#
# def test_calculator_divide():
#     """ Testing the divide method of the calculator """
#     calc = Calculator()
#     calc.divide_number(1)
#     assert calc.get_result() == 0
#
# def test_calculator_divide_by_zero():
#     """ Testing divide by zero on divide method of calculator"""
#     # the WITH keyword here is saying the following block of code must throw given exception
#     with pytest.raises(ZeroDivisionError):
#         calc = Calculator()
#         calc.add_number(10)
#         calc.divide_number(0)

# def test_calculator_history():
#     calc = Calculator()
#     calc.add_number(1)
#     print(calc.history)
#     assert calc.get_result() == 0