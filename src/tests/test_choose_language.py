from main import choose_language
import unittest
from unittest.mock import patch
from unittest import mock


class TestChooseLanguage(unittest.TestCase):
    def test_valid_input(self):
        with unittest.mock.patch("builtins.input", return_value="3"):
            self.assertEqual(choose_language(4), 3)

if __name__ == "__main__":
    unittest.main()
