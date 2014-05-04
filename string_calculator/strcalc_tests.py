import unittest
from strcalc import StringCalculator

class StringCalculatorTests(unittest.TestCase):
	def test_add_returns_0_for_empty_string(self):
		sc = StringCalculator()
		self.assertEqual(0, sc.add(""))

	def test_add_one_number_returns_number(self):
		sc = StringCalculator()
		self.assertEqual(1, sc.add("1"))

if __name__ == "__main__":
	unittest.main()
