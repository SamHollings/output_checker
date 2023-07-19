"""
Functions to check files to ensure they aren't too big, or too long.
"""

import pathlib
import os


def get_file_size_mb(file_path: pathlib.Path) -> float:
    """Returns the size of the file (in megabytes) at the supplied filepath
    Attributes:
        file_path (pathlib.Path): the path to the file to be checked
    Returns:
        float: the size of the file in megabytes
    Example:
        >>> get_file_size_mb("tests/one_mb_file.txt")
        1.0
    """
    size_in_bytes = os.path.getsize(file_path)
    size_in_megabytes = size_in_bytes / (1024 * 1024)

    return size_in_megabytes


def get_file_length_rows(file_path: pathlib.Path, encoding) -> int:
    """Returns the number of rows in the file at the supplied filepath
    Attributes:
        file_path (pathlib.Path): the path to the file to be checked
        **kwargs: keyword arguments to be passed through to the "open" function
    Returns:
        int: the number of rows in the file
    Example:
        >>> get_file_length_rows("tests/ten_line_file.txt")
        10
    """

    with open(file_path, 'r', encoding=encoding) as file:
        row_count = sum(1 for _ in file)

    return row_count


if __name__ == "__main__":
    import doctest

    doctest.testmod()
