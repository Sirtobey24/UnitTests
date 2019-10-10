import unittest
from Part1.line import *


class LineTests(unittest.TestCase):
    def test_line(self):
        l1 = Line(2, 2, 4, 4)
        self.assertEqual(l1.x1, 2)
        self.assertEqual(l1.y1, 2)
        self.assertEqual(l1.x2, 4)
        self.assertEqual(l1.y2, 4)


class LineTests2(unittest.TestCase):
    def test_line_again(self):
        l2 = Line(3, 3, 5, 5)
        self.assertEqual(l2.x1, 3)
        self.assertEqual(l2.y1, 3)
        self.assertEqual(l2.x2, 5)
        self.assertEqual(l2.y2, 5)

    # Add code here.
    # 1) Create a Line with x1, y1, x2, y2 values of your choice.
    # 2) Use assertEqual on each field in the new Line to verify
    #    that it holds the expected value.


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
