import unittest
from Part3.conditional import *


class TestCases(unittest.TestCase):
    def test_case(self):
        result = max_of_two(3, 4)
        self.assertEqual(result, 4)
        pass

    def test_case2(self):
        result = max_of_two(5, 2)
        self.assertEqual(result, 5)
        pass

    def test_case3(self):
        result = max_of_three(1, 2, 3)
        self.assertEqual(result, 3)
        pass

    def test_case4(self):
        result = max_of_three(5, 4, 6)
        self.assertEqual(result, 6)
        pass

    def test_case5(self):
        result = max_of_three(8, 10, 9)
        self.assertEqual(result, 10)
        pass


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
