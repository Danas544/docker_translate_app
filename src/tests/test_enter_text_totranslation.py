from main import enter_text_to_translation
import unittest
from unittest.mock import patch


class TestEnterTextToTranslation(unittest.TestCase):
    def test_valid_input_returns_text(self):
        text = "Test this is a valid input with more than 10 words"
        with unittest.mock.patch("builtins.input", return_value=text):
            self.assertEqual(enter_text_to_translation(), text)

    def test_valid_input_with_10_words_returns_text(self):
        text = "Test this is a valid input with exactly 10 words"
        with unittest.mock.patch("builtins.input", return_value=text):
            self.assertEqual(enter_text_to_translation(), text)

    def test_input_with_special_characters_returns_text(self):
        text = "Test this is a valid input with special characters: !@#$%^&*()_+"
        with unittest.mock.patch("builtins.input", return_value=text):
            self.assertEqual(enter_text_to_translation(), text)

    def test_input_with_leading_trailing_spaces_returns_text(self):
        text = "   This is a valid input with leading/trailing spaces   "
        with unittest.mock.patch("builtins.input", return_value=text):
            self.assertEqual(enter_text_to_translation(), text)

    def test_input_with_less_10_words(self):
        with unittest.mock.patch(
            "builtins.input",
            side_effect=["     ", "This is a test input with more than 10 words"],
        ):
            with unittest.mock.patch("builtins.print") as mock_print:
                self.assertEqual(
                    enter_text_to_translation(),
                    "This is a test input with more than 10 words",
                )
                mock_print.assert_called_with("Need to enter more than 10 words")


if __name__ == "__main__":
    unittest.main()
