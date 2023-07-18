"""disclosure_control_check tests"""

import unittest
import doctest
import src.scan_directory


def load_tests(loader, tests, ignore):  # pylint: disable=unused-argument
    """This creates a unittest.TestCase from the doctests described in the
    module
    """
    tests.addTests(doctest.DocTestSuite(src.scan_directory))
    return tests


if __name__ == "__main__":
    unittest.main()
