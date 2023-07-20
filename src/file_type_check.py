"""Functions which check the type of the files"""
import os


def get_file_type(file_path):
    """Gets the file type of a file.

    Args:
      file_path: The path to the file.

    Returns:
      The file type of the file.

    Example:
      >>> get_file_type("README.md")
      'md'
    """

    file_extension = os.path.splitext(file_path)[1]
    file_type = file_extension.lstrip(".").lower()
    return file_type


if __name__ == "__main__":
    import doctest

    doctest.testmod()
