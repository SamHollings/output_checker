"""General utilities"""

import pandas as pd


def prep_df_for_tests(test_df: pd.DataFrame) -> list:
    """It's not easy for the testing modules to compare dataframes, so this
    function simply squashes them flat into a list which is easy to compare"""
    return test_df.fillna(999999999).to_numpy().flatten().tolist()
