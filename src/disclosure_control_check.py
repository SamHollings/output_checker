"""
Functions that do:
DONE: check pandas Series for: values less than 5
DONE: check pandas Series for: values not divisible by 5 ( x % 5 <> 0)
TODO: get the rows IDs of any "failed" checks
TODO: apply the above across a dataframe to designated columns returning
    column and row IDs of failures.
TODO: create entitiy recongition of a string function
"""
import pandas as pd
import numpy as np
import spacy

nlp_model = spacy.load("en_core_web_md")


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


def return_sdc_dataframe_fails(data: pd.DataFrame) -> pd.DataFrame:
    """Apply the SDC rules to a dataframe, and then returns only the rows /
    columns which failed
    Attributes:
        data (pd.DataFrame): the data being checked provided as a pandas
                            DataFrame
    Returns:
        pd.DataFrame: a mask which contains the failure entries
    Example:
        >>> #ToDo: add an example for return_sdc_dataframe_fails
        >>> x_dict = {"place":["York", "Sheffield", "Leeds"],
        ... 'count':[0,5,50],
        ... 'count2':[100,20,105],
        ... 'count3':[0,30, 200]
        ... }
        >>> x = pd.DataFrame(x_dict)
        >>> print(return_sdc_dataframe_fails(x))
           count  count3
        0    0.0     0.0
        1    5.0     NaN
    """
    data_numeric = data.select_dtypes(include=np.number)

    # apply sdc to COLUMNs
    data_mask = data_numeric.apply(check_series_sdc, axis=0)

    return data[~data_mask].dropna(axis=1, how="all").dropna(axis=0, how="all")


default_patterns = [{"TYPE": "EMAIL"}, {"TYPE": "PHONE"}, {"TYPE": "NAME"}]


def check_string_entities(text: str, nlp: spacy.lang = nlp_model,
                          # patterns: list = default_patterns
                          ) -> str:
    """Checks the string for entities
    Returns:
        A string containing the found entities
    Example:
        >>> x = "Apple is looking at buying U.K. startup for $1 billion"
        >>> check_string_entities(x)
        [['Apple', 0, 5, 'ORG'], ['U.K.', 27, 31, 'GPE'], ['$1 billion', 44, 54, 'MONEY']]
    """

    # Create doc from text. Doc is a convention in spacy
    doc = nlp(text)
    entities = []
    print("Entities:")
    for ent in doc.ents:
        entities.append([ent.text, ent.start_char, ent.end_char, ent.label_])
    return entities


if __name__ == "__main__":
    import doctest

    doctest.testmod()
