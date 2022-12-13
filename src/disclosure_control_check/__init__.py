"""
Functions that do:
DONE: check pandas Series for: values less than 5
DONE: check pandas Series for: values not divisible by 5 ( x % 5 <> 0)
TODO: get the rows IDs of any "failed" checks
TODO: apply the above across a dataframe to designated columns returning
    column and row IDs of failures.
"""
import pandas as pd


def check_series_sdc(column: pd.Series) -> pd.Series:
    """Checks the series following the disclosure control rules
    Attributes:
        column (pd.Series): the column being checked provided as a pandas
                            Series
    Returns:
        pd.Series: a mask which describes which rows passed and which failed
    Example:
        >>> x = pd.Series([0,1,5,10,11,101], name='count')
        >>> check_series_sdc(x).to_list()
        [False, False, False, True, False, False]
    """

    divisible_by_five = ((column % 5) == 0).fillna(1)
    greater_equal_ten = column >= 10

    mask = divisible_by_five.combine(greater_equal_ten, min, fill_value=0)

    return mask


if __name__ == "__main__":
    import doctest

    doctest.testmod()
