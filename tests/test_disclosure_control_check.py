"""disclosure_control_check tests"""
import sys

sys.path.append("../src")

import unittest
import doctest
import pandas as pd
from src.disclosure_control_check import check_series_sdc

# def load_tests(loader, tests, ignore):  # pylint: disable=unused-argument
#     """This creates a unittest.TestCase from the doctests described in the
#     module
#     """
#     tests.addTests(doctest.DocTestSuite(src.disclosure_control_check))
#     return tests


class TestCheckSeriesSdc(unittest.TestCase):
    """Testing the check_series_sdc function"""

    def test_output_correct(self):
        """checks the output of the function is as expected"""
        self.assertEqual(check_series_sdc(pd.Series([10, 15, 20, 25, 30])).tolist(), 
                        pd.Series([True, True, True, True, True]).tolist(), 
                        "incorrect check for sdc")
        self.assertEqual(check_series_sdc(pd.Series([5, 31, 1005, -5, -100])).tolist(), 
                        pd.Series([False, False, True, False, True]).tolist(), 
                        "incorrect check for sdc")
        self.assertEqual(check_series_sdc(pd.Series(["Egg", 27, -17, "Adam", 10052022])).tolist(), 
                        pd.Series([False, False, False, False, False]).tolist(),  # should be false as the value is date like
                        "incorrect check for sdc")
                    


if __name__ == "__main__":
    unittest.main()
