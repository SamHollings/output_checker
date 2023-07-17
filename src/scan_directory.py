""""Contains functions which will scan a directory and apply the
battery of checks"""
import glob
import pandas as pd
import file_size_checks

default_checks = dict(size_mb=file_size_checks.get_file_size_mb,
                      #length_rows=file_size_checks.get_file_length_rows
                      )


def get_all_filepaths_in_directory(dir_path):
    """Returns a list of all the filepaths in the directory

    Example:
        >>> get_all_filepaths_in_directory("tests/test_get_filepaths_in_directory")
        ['tests/test_get_filepaths_in_directory/test.txt']
    """
    all_files = glob.glob(dir_path + '/**/*', recursive=True)
    return all_files


def scan_directory(dir_path, checks=default_checks):
    """Applies the supplied checks to each file in the directory

    Example:
    >>> scan_directory("tests/test_get_filepaths_in_directory")
                                                 path  size_mb
    0  tests/test_get_filepaths_in_directory/test.txt      0.0
    """
    list_file_paths = get_all_filepaths_in_directory(dir_path)

    df_files = pd.DataFrame(dict(path=list_file_paths))

    for check_name, check_func in checks.items():
        df_files[check_name] = df_files.apply(lambda x: check_func(x['path']),
                                              axis=1)

    return df_files


if __name__ == "__main__":
    import doctest

    doctest.testmod()
