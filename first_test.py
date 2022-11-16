import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
         self.calc = Calculator

    def test_multiply_correctly(self):#проверка метода умножения
        assert self.calc.multiply(self, 2, 2) == 4

    def test_division_correctly(self):#проверка метода деления
        assert self.calc.division(self, 2, 2) == 1

    def test_subtraction_correctly(self):#проверка метода вычитания
        assert self.calc.subtraction(self, 5, 2) == 3

    def test_adding_correctly(self):#проверка метода сложения
        assert self.calc.adding(self, 3, 3) == 6
