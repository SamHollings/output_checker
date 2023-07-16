import pandas as pd

def create_dataframe():
  """Creates a Pandas DataFrame with realistic personality identifiable data."""

  dictionary = {
      'NHSNUMBER': ['1234567890', '9876543210', '0123456789'],
      'GENDER': ['Male', 'Female', 'Non-binary'],
      'DIAGNOSIS': ['Depression', 'Anxiety', 'Bipolar disorder'],
  }

  dataframe = pd.DataFrame.from_dict(dictionary)

  return dataframe

if __name__ == "__main__":
  dataframe = create_dataframe()

  print(dataframe)
