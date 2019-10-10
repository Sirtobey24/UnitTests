import unittest
from Part1.vehicle import *


class VehicleTests(unittest.TestCase):
    def test_vehicle(self):
        sedan = Vehicle(4, 100, 4, True)
        self.assertEqual(sedan.numofwheels, 4)
        self.assertEqual(sedan.amountoffuelrem, 100)
        self.assertEqual(sedan.numofdoors, 4)
        self.assertEqual(sedan.have_roof, True)


class VehicleTests2(unittest.TestCase):
    def test_vehicle2(self):
        coupe = Vehicle(4, 100, 2, True)
        self.assertEqual(coupe.numofwheels, 4)
        self.assertEqual(coupe.amountoffuelrem, 100)
        self.assertEqual(coupe.numofdoors, 2)
        self.assertEqual(coupe.have_roof, True)


class VehicleTests3(unittest.TestCase):
    def test_vehicle3(self):
        semitruck = Vehicle(18, 200, 2, True)
        self.assertEqual(semitruck.numofwheels, 18)
        self.assertEqual(semitruck.amountoffuelrem, 200)
        self.assertEqual(semitruck.numofdoors, 2)
        self.assertEqual(semitruck.have_roof, True)


class VehicleTests4(unittest.TestCase):
    def test_vehicle3(self):
        motorcycle = Vehicle(2, 200, 0, False)
        self.assertEqual(motorcycle.numofwheels, 2)
        self.assertEqual(motorcycle.amountoffuelrem, 200)
        self.assertEqual(motorcycle.numofdoors, 0)
        self.assertEqual(motorcycle.have_roof, False)


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
