"""disclosure_control_check tests"""
import unittest
import doctest
import pandas as pd
import numpy as np
import src.disclosure_control_check
import src.make_data
import src.utils as utils


def load_tests(loader, tests, ignore):  # pylint: disable=unused-argument
    """This creates a unittest.TestCase from the doctests described in the
    module
    """
    tests.addTests(doctest.DocTestSuite(src.disclosure_control_check))
    return tests


class TestCheckSeriesSdc(unittest.TestCase):
    """Testing the check_series_sdc function"""

    def test_output_correct(self):
        """checks the output of the function is as expected"""
        data = pd.Series([10, 15, 20, 25, 30])
        result = src.disclosure_control_check.check_series_sdc(data).tolist()
        expected = pd.Series([True, True, True, True, True]).tolist()
        self.assertEqual(result, expected, "incorrect check for sdc")


class TestReturnSdcDataframeFails(unittest.TestCase):
    """Testing the return_sdcs_dataframe_fails function"""

    def test_output_correct(self):
        """checks the output of the function is as expected"""
        x_dict = {
            "place": ["York", "Sheffield", "Leeds"],
            "count": [0, 5, 50],
            "count2": [100, 20, 105],
            "count3": [0, 30, 200],
        }
        x = pd.DataFrame(x_dict)
        result = src.disclosure_control_check.return_sdc_dataframe_fails(x)
        expected = pd.DataFrame(
            dict(count=[0.0, 5.0], count3=[0.0, np.NaN]), index=[0, 1]
        )
        self.assertEqual(
            utils.prep_df_for_tests(result),
            utils.prep_df_for_tests(expected),
            "incorrect identification of error rows",
        )


if __name__ == "__main__":
    unittest.main()
