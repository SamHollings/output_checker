import os

def get_file_type(file_path):
    """Gets the file type of a file.

    Args:
      file_path: The path to the file.

    Returns:
      The file type of the file.
    """

    file_extension = os.path.splitext(file_path)[1]
    file_type = file_extension.lstrip(".").lower()
    return file_type
