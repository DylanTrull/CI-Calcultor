"""
Test for calc app
"""

import calculator

class TestCalculatorApp:
    def test_add(self):
        assert 5 == calculator.add(2, 3)

    def test_subtract(self):
        assert 5 == calculator.subtract(10, 5)

    def test_division(self):
        assert 5 == calculator.division(10, 2)

    def test_multiplication(self):
        assert 10 == calculator.multiplication(5, 2)

