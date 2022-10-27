# $ python -m unittest tests.py - команда для запуска теста

import unittest
from math import sqrt

# 1 Пример:

class BasicTestCase(unittest.TestCase):

    def test_using_asserttrue(self):
        list_a = [0, 1, 2]
        list_b = [1, 2]
        self.assertTrue(list_a == list_b)

    def test_using_assertequal(self):
        list_a = [0, 1, 2]
        list_b = [1, 2]
        self.assertEqual(list_a, list_b)

if __name__=='__main__':
    unittest.main()


# 2 Пример: Калькулятор.


class Calculator:
    def __init__(self):
        pass

    def add(self, x1, x2):
        return x1 + x2

    def multiply(self, x1, x2):
        return x1 * x2

    def subtract(self, x1, x2):
        return x1 - x2

    def divide(self, x1, x2):
        if x2 != 0:
            return x1/x2

    def more(self, x1, x2):
        return x1>x2
    
    def less(self, x1, x2):
        return x1<x2


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(4, 7), 11)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(3, 7), 21)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(10, 2), 5)
    
    def test_more(self):
        self.assertTrue(self.calculator.more(10, 2))

    def test_less(self):
        self.assertFalse(self.calculator.less(12, 11))

if __name__ == "__main__":
    unittest.main()


# 3 Пример: Нужно ввести три числа (a, b, c) и найти корни квадратного уравнения.


def square_eq_solver(a, b, c):
   result = []
   discriminant = b * b - 4 * a * c

   if discriminant == 0:
       result.append(-b / (2 * a))
   elif discriminant > 0:
       result.append((-b + sqrt(discriminant)) / (2 * a))
       result.append((-b - sqrt(discriminant)) / (2 * a))

   return result

def show_result(data):
   if len(data) > 0:
       for index, value in enumerate(data):
           print(f'Корень номер {index+1} равен {value:.02f}')
   else:
       print('Уравнение с заданными параметрами не имеет корней')

def main():
   a, b, c = map(int, input('Пожалуйста, введите три числа через пробел: ').split())
   result = square_eq_solver(a, b, c)
   show_result(result)

if __name__ == '__main__':
   main()


class SquareEqSolverTestCase(unittest.TestCase):
    def test_no_root(self):
        res = square_eq_solver(10, 0, 2)
        self.assertEqual(len(res), 0)

    def test_single_root(self):
        res = square_eq_solver(10, 0, 0)
        self.assertEqual(len(res), 1)
        self.assertEqual(res, [0])

    def test_multiple_root(self):
        res = square_eq_solver(2, 5, -3)
        self.assertEqual(len(res), 2)
        self.assertEqual(res, [0.5, -3])

if __name__=='__main__':
    unittest.main()