import unittest
from Part3.logic import *


class TestCases(unittest.TestCase):
    def test_case(self):
        result = is_even(2)
        self.assertTrue(result, True)
        pass

    def test_case2(self):
        result = is_even(3)
        self.assertFalse(result, True)

    def test_case3(self):
        result = in_an_interval(101)
        self.assertTrue(result, True)

    def test_case4(self):
        result = in_an_interval(10)
        self.assertFalse(result, True)


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
