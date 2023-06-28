from main import option
import unittest
from unittest.mock import patch


class TestOption(unittest.TestCase):
    # Tests that the function returns True when the user inputs 'y'
    def test_y(self):
        with unittest.mock.patch("builtins.input", return_value="y"):
            self.assertTrue(option())

    def test_n(self):
        with unittest.mock.patch("builtins.input", return_value="n"):
            self.assertTrue(option() is False)

    def test_edge_case_non_string_input(self):
        with unittest.mock.patch("builtins.input", side_effect=[1, "y"]):
            self.assertTrue(option())
        with unittest.mock.patch("builtins.input", side_effect=[True, "n"]):
            self.assertFalse(option())

    def test_edge_case_empty_string_input(self):
        with unittest.mock.patch("builtins.input", side_effect=["", "y"]):
            self.assertTrue(option())
        with unittest.mock.patch("builtins.input", side_effect=["", "n"]):
            self.assertFalse(option())
