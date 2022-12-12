import unittest
import doctest
from src.disclosure_control_check import check_series_sdc
import src.make_data
import pandas as pd


def load_tests(loader, tests, ignore):
    """This creates a unittest.TestCase from the doctests described in the
    module"""
    tests.addTests(doctest.DocTestSuite(src.disclosure_control_check))
    return tests

class test_check_series_sdc(unittest.TestCase):
    def runTest(self):
        data = pd.Series([10,15,20,25,30])
        self.assertEqual(check_series_sdc(data), 
        pd.Series({0 : True, 1: True, 2: True, 3: True, 4: True}), 
        "incorrect check for sdc")


if __name__ == "__main__":
    unittest.main()
