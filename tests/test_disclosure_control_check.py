"""disclosure_control_check tests"""
import unittest
import doctest
import pandas as pd
import numpy as np
import src.disclosure_control_check as src_disc
import src.make_data
from src import utils


def load_tests(loader, tests, ignore):  # pylint: disable=unused-argument
    """This creates a unittest.TestCase from the doctests described in the
    module
    """
    tests.addTests(doctest.DocTestSuite(src.disclosure_control_check))
    return tests


class TestCheckSeriesSdc(unittest.TestCase):
    """Testing the check_series_sdc function"""

    def test_output_correct_all_true(self):
        """checks the output of the function is as expected"""

        self.assertEqual(src_disc.check_series_sdc(pd.Series([10, 15, 20, 25, 30])).tolist(),
                         pd.Series([True, True, True, True, True]).tolist(),
                         "incorrect check for sdc")

    def test_output_correct_small_values(self):
        """Tests the function can identify small values"""
        self.assertEqual(src_disc.check_series_sdc(pd.Series([5, 30, 1005, -3, -100])).tolist(),
                         pd.Series([False, True, True, False, True]).tolist(),
                         "incorrect check for sdc")

    def test_output_correct_unrounded_values(self):
        """Tests the function can identify unrounded values"""
        self.assertEqual(src_disc.check_series_sdc(pd.Series([5, 31, 1005, -10, -100])).tolist(),
                         pd.Series([False, False, True, True, True]).tolist(),
                         "incorrect check for sdc")

    def test_output_correct_string_errors(self):
        """Tests the function can identify strings"""
        self.assertEqual(src_disc.check_series_sdc(pd.Series(["Egg", 25, -15, "Adam", 10052020])).tolist(),
                         pd.Series([False, True, True, False, True]).tolist(),
                         "incorrect check for sdc")

    def test_output_correct_mixed_errors(self):
        """Tests the function against a mixture of errors at the same time"""
        self.assertEqual(src_disc.check_series_sdc(pd.Series(["Egg", 27, -17, "Adam", 10052022])).tolist(),
                         pd.Series([False, False, False, False, False]).tolist(),
                         "incorrect check for sdc")


class TestReturnSdcDataframeFails(unittest.TestCase):
    """Testing the return_sdcs_dataframe_fails function"""

    def test_output_correct(self):
        """checks the output of the function is as expected"""
        test_dict = {
            "place": ["York", "Sheffield", "Leeds"],
            "count": [0, 5, 50],
            "count2": [100, 20, 105],
            "count3": [0, 30, 200],
        }
        test_df = pd.DataFrame(test_dict)
        result = src.disclosure_control_check.return_sdc_dataframe_fails(test_df)
        expected = pd.DataFrame(
            {'count': [0.0, 5.0], 'count3': [0.0, np.NaN]}, index=[0, 1]
        )
        self.assertEqual(
            utils.prep_df_for_tests(result),
            utils.prep_df_for_tests(expected),
            "incorrect identification of error rows",
        )


if __name__ == "__main__":
    unittest.main()
