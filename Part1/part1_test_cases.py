#
# Test cases example for lab 1.
#

import unittest      # import the module that supports writing unit tests

# Define a class that will be used for these test cases.
# This class will include testing functions.
#
# Much of this code should be viewed as boilerplate for now.
#
class TestsLab1(unittest.TestCase):
   def test_expressions(self):         # Defines one testing function.
      self.assertEqual(0 + 1, 1)

class TestsLab2(unittest.TestCase):
    def test_expressions(self):
        self.assertEqual(2 * 2, 4)

class TestsLab3(unittest.TestCase):
    def test_expressions(self):
        self.assertEqual(19 // 3, 6)

class TestsLab4(unittest.TestCase):
    def test_expressions(self):
        self.assertAlmostEqual(19/3, 6.333333333333333)

class TestsLab5(unittest.TestCase):
    def test_expressions(self):
        self.assertAlmostEqual(19/3.0, 6.333333333333333)

class TestLab6(unittest.TestCase):
    def test_expressions(self):
        self.assertAlmostEqual(19.0/3.0, 6.333333333333333)

class TestLab6(unittest.TestCase):
    def test_expressions(self):
        self.assertEqual(4*2+27 // 3+4, 21)

class TestLab7(unittest.TestCase):
    def test_expressions(self):
        self.assertEqual(4 * (2 + 27) // 3 + 4, 42)



# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

