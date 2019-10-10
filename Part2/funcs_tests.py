import unittest
from Part2.funcs import *


class TestCases(unittest.TestCase):
	def test_f_1(self):
		result = f(2)
		self.assertEqual(result, 32)
		pass

	def test_f_2(self):
		result = f(3)
		self.assertEqual(result, 69)
		pass

	def test_g_1(self):
		result = g(2, 3)
		self.assertEqual(result, 13)
		pass

	def test_g_2(self):
		result = g(3, 4)
		self.assertEqual(result, 25)
		pass

	def test_hypotenuse_1(self):
		result = hypotenuse(3, 4)
		self.assertEqual(result, 5)
		pass

	def test_hypotenuse_2(self):
		result = hypotenuse(1, 2)
		self.assertEqual(result, 2.23606797749979)
		pass

	def test_ispositive_1(self):
		result = is_positive(1)
		self.assertTrue(result, True)
		pass

	def test_ispositive_2(self):
		result = is_positive(-2)
		self.assertFalse(result, True)
		pass


# Run the unit tests.
if __name__ == '__main__':
	unittest.main()
