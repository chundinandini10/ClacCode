from django.test import TestCase
from calculator.services import CalculatorService

class CalculatorServiceTest(TestCase):
    def test_add(self):
        self.assertEqual(CalculatorService.add(10, 5), 15)
        self.assertEqual(CalculatorService.add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(CalculatorService.subtract(10, 5), 5)
        self.assertEqual(CalculatorService.subtract(5, 10), -5)

    def test_multiply(self):
        self.assertEqual(CalculatorService.multiply(10, 5), 50)
        self.assertEqual(CalculatorService.multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(CalculatorService.divide(10, 5), 2)
        with self.assertRaises(ValueError):
            CalculatorService.divide(10, 0)

    def test_power(self):
        self.assertEqual(CalculatorService.power(2, 3), 8)
        self.assertEqual(CalculatorService.power(9, 0.5), 3)

    def test_sqrt(self):
        self.assertEqual(CalculatorService.sqrt(16), 4)
        with self.assertRaises(ValueError):
            CalculatorService.sqrt(-1)
