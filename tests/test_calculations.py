import unittest
from example_package import calculations

class CalculationsTestCase(unittest.TestCase):
    def test_double(self):
        assert calculations.double(4) == 8