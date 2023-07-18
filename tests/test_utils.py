"""utils tests"""

import unittest
import pandas as pd
from src import utils


class TestPrepDfForTests(unittest.TestCase):
    """test the prep_df_for_tests function"""

    def test_output(self):
        """Simply do an output test to ensure basic function"""
        df_test = pd.DataFrame({'col1':["dog", "cat"], 'count':[3, 4]})
        expected = ["dog", 3, "cat", 4]
        result = utils.prep_df_for_tests(df_test)
        error_message = "squashed dataframe didn't match list"
        self.assertEqual(result, expected, error_message)


if __name__ == "__main__":
    unittest.main()
