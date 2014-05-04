import unittest
from strcalc import StringCalculator

class StringCalculatorTests(unittest.TestCase):
	def setUp(self):
		self.sc = StringCalculator()

	def test_add_returns_0_for_empty_string(self):
		self.assertEqual(0, self.sc.add(""))

	def test_add_one_number_returns_number(self):
		self.assertEqual(1, self.sc.add("1"))

	def test_add_two_numbers(self):
		self.assertEqual(3, self.sc.add("1,2"))

	def test_add_many_numbers(self):
		self.assertEqual(10, self.sc.add("1,2,3,4"))

	def test_newline_delimiter(self):
		self.assertEqual(3, self.sc.add("1\n2"))

	def test_split_single(self):
		self.assertEqual(
			["2", "3"], 
			self.sc.split("2,3", [","]))

	def test_split_multiple(self):
		self.assertEqual(
			["2", "3", "4"], 
			self.sc.split("2,3.4", [",", "."]))

if __name__ == "__main__":
	unittest.main()
