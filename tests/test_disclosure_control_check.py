"""disclosure_control_check tests"""
import unittest
import doctest
import src.disclosure_control_check


def load_tests(loader, tests, ignore):
    """This creates a unittest.TestCase from the doctests described in the
    module"""
    tests.addTests(doctest.DocTestSuite(src.disclosure_control_check))
    return tests


if __name__ == "__main__":
    unittest.main()
