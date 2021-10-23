"""Testing the Calculator"""
from calculator.main import Calculator

def test_calculator_result():
    """ testing calculator result is 0 """
    calc = Calculator()
    assert calc.result == 0

def test_calculator_get_result():
    """ Testing the Get result method of the calculator """
    calc = Calculator()

    assert calc.get_result() == 0

def test_calculator_add_multiple():
    """ Testing the add function of the calculator with multiple vals """
    # ARRANGE by instantiating the calc class
    calc = Calculator()
    # ACT by calling the method to be tested
    calc.add_number(1, 2, 3)
    # ASSERT that the results are correct
    assert calc.result == 6

def test_calculator_subtract_multiple():
    """ Testing the subtract method of the calculator with multiple vals """
    calc = Calculator()
    calc.subtract_number(5, 10)
    assert calc.get_result() == -15

def test_calculator_multiply_multiple():
    """ Testing the multiply method of the calculator with multiple vals """
    calc = Calculator()
    calc.add_number(1)
    calc.multiply_number(5, 4, 5)
    assert calc.get_result() == 100

def test_calculator_divide_multiple():
    """ Testing the divide method of the calculator with multiple vals """
    calc = Calculator()
    calc.add_number(12)
    calc.divide_number(3, 2)
    assert calc.get_result() == 2
