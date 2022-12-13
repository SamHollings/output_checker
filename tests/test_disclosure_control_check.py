"""disclosure_control_check tests"""
import unittest
import doctest
import pandas as pd
from src.disclosure_control_check import check_series_sdc
import src.make_data


def load_tests(loader, tests, ignore):  # pylint: disable=unused-argument
    """This creates a unittest.TestCase from the doctests described in the
    module
    """
    tests.addTests(doctest.DocTestSuite(src.disclosure_control_check))
    return tests


class TestCheckSeriesSdc(unittest.TestCase):
    """Testing the check_series_sdc function"""

    def output_correct(self):
        """checks the output of the function is as expected"""
        data = pd.Series([10, 15, 20, 25, 30])
        result = check_series_sdc(data).tolist()
        expected = pd.Series([True, True, True, True, True]).tolist()
        self.assertEqual(result, expected, "incorrect check for sdc")


if __name__ == "__main__":
    unittest.main()
