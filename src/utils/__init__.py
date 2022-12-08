"""This code will make test dataset for use in the other scripts
"""
import pandas as pd
import numpy as np

# utils
def test_data() -> pd.Dataframe:
    ''' Returns a pandas dataframe with some common test cases
    Args:
        None
    Returns:
        pd.Dataframe: the test data
    Example:
        >>> x = test_data
        >>> len(x)
        6
        >>> x.loc[3, 'cat_field']
        "John Doe"
    '''
    test_data = pd.Dataframe(
                    dict(id=[0,1,2,3,4,5],
                        count=[0,1,5,10,11,101],
                        cat_field=["a","b","a","John Doe","a","b"],
                        freetext_field=["","a", "I thought Doctor Smith, who lived at 1 privett drive, was very friendly, "b", "c", None],
                        )
                    )
                     
    return test_data

if __name__ == "__main__":
    import doctest
    doctest.testmod()
