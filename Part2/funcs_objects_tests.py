import unittest
from Part2.funcs_objects import *


class TestCases(unittest.TestCase):
    def test_point(self):
        p1 = Point(2, 2)
        self.assertEqual(p1.x, 2)
        self.assertEqual(p1.y, 2)
        pass

    def test_circle(self):
        c1 = Circle(3, 4, 5)
        self.assertEqual(c1.x, 3)
        self.assertEqual(c1.y, 4)
        self.assertEqual(c1.r, 5)
        pass

    def test_distance(self):
        p1 = Point(2, 2)
        p2 = Point(3, 3)
        result = distance(p1, p2)
        self.assertEqual(result, 1.4142135623730951)
        pass

    def test_circle_overlap(self):
        c1 = Circle(2, 2, 4)
        c2 = Circle(3, 3, 5)
        result = circles_overlap(c1, c2)
        self.assertTrue(result, True)


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
