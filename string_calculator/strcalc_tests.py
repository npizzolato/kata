import unittest
from strcalc import StringCalculator

class StringCalculatorTests(unittest.TestCase):
	def test_add_returns_0_for_empty_string(self):
		sc = StringCalculator()
		self.assertEqual(0, sc.add(""))

if __name__ == "__main__":
	unittest.main()
