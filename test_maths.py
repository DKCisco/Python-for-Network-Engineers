from audioop import mul
import unittest
from unit_test_module_1 import multiplier, subtractor

class TestMaths(unittest.TestCase):

    def test_multiplier(self):
        total = multiplier(2, 4)
        self.assertEqual(total, 9)