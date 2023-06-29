import unittest
from main import CLI


class TestCLI(unittest.TestCase):
    def test_translation_english_to_spanish(self):
        cli = CLI("spanish", "Hello")
        result = cli.translate_text()
        self.assertEqual(result, "Hola")

    def test_translation_spanish_to_english(self):
        cli = CLI("english", "Hogar")
        result = cli.translate_text()
        self.assertEqual(result, "Home")

    def test_translation_chinese_to_german(self):
        cli = CLI("german", "你好")
        result = cli.translate_text()
        self.assertEqual(result, "Hallo")

    def test_translation_indonesian_to_chinese(self):
        cli = CLI("chinese (traditional)", "Nama")
        result = cli.translate_text()
        self.assertEqual(result, "不")

    def test_translation_german_to_indonesian(self):
        cli = CLI("indonesian", "Hallo")
        result = cli.translate_text()
        self.assertEqual(result, "Halo")

    def test_translation_empty_text(self):
        cli = CLI("spanish", "")
        result = cli.translate_text()
        self.assertEqual(result, "")

if __name__ == "__main__":
    unittest.main()
