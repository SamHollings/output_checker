"""make_data tests"""
import unittest
import doctest
import src.make_data


def load_tests(loader, tests, ignore):
    """This creates a unittest.TestCase from the doctests described in the
    module"""
    tests.addTests(doctest.DocTestSuite(src.make_data))
    return tests


if __name__ == "__main__":
    unittest.main()
