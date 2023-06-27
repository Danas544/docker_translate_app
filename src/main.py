# 1) Create a CLI Program that would take a sentence of at least 10 words (>= 10)
# and would let you translate to at least 5 different languages (10 better for fun).
# Plus there have to be an option to get symbols/letters amount of the translation.
# And there should be the option to translate to all languages at the same time. The whole program should be dockerized and tested.
# Please find, which translation have the shortest/longest variation.Write some unittests for non translation functionality.
#  Test should be executed before the main program.
from deep_translator import GoogleTranslator
from typing import Optional


def enter_text_to_translation() -> str:
    while True:
        text = input("Enter text: ")
        if len(text.split(" ")) < 10:
            print("Need to enter more than 10 words")
            continue
        return text


def choose_language(count: int) -> Optional[int]:
    while True:
        choice_list = []
        for x in range(1, count + 1):
            choice_list.append(x)
        try:
            choice = int(input("Choose language to tranlate: "))
        except ValueError:
            print(f"you can choose from {choice_list}")
            continue
        if choice not in choice_list:
            print(f"you can choose from {choice_list}")
            continue
        elif choice is choice_list[-1]:
            return False
        return choice


def option() -> bool:
    while True:
        text = str(input("Do you wanna know how letters have translated text? (y/n): "))
        if text.lower() not in ["y", "n"]:
            print("Just write y or n")
            continue
        if text.lower() == "y":
            return True
        else:
            return False


def option_shortes_longest() -> bool:
    while True:
        text = str(
            input(
                "Do you wanna know which tranleted text is longest and shortest? (y/n): "
            )
        )
        if text.lower() not in ["y", "n"]:
            print("Just write y or n")
            continue
        if text.lower() == "y":
            return True
        else:
            return False


class Language:
    def __init__(self):
        self.english_language = "English"
        self.spanish_language = "Spanish"
        self.chinese_language = "Chinese (traditional)"
        self.portugal_language = "Serbian"
        self.germany_language = "German"

    def get_all_language_names(self) -> list:
        return [
            self.english_language,
            self.spanish_language,
            self.chinese_language,
            self.portugal_language,
            self.germany_language,
        ]


class CLI(Language):
    def __init__(self, languages: str, text: str):
        self.languages = languages
        self.text = text

    def translate_text(self) -> str:
        translated = GoogleTranslator(
            source="auto", target=self.languages.lower()
        ).translate(self.text)
        return translated


text = enter_text_to_translation()
language = Language()
language_names = language.get_all_language_names()
count = 1
for x in language_names:
    print(f"{count}. {x}")
    count += 1
print(f"{count}. Translate from all languages")
choose = choose_language(count=count)
if choose is False:
    tranleted_list = []
    for language in language_names:
        power = CLI(languages=language, text=text)
        transleted = power.translate_text()
        print(transleted)
        tranleted_list.append(transleted)
    longest_text = option_shortes_longest()
    if longest_text is True:
        print(
            f"Longest translented text: {min(tranleted_list)}, letters: {len(min(tranleted_list))},"
            f" Shortest translented text: {max(tranleted_list)}, letters: {len(max(tranleted_list))}"
        )

else:
    power = CLI(languages=language_names[choose - 1], text=text)
    transleted = power.translate_text()
    print(transleted)
    letters = option()
    if letters is True:
        print(f"text: {len(text)}, tranleted text: {len(transleted)}")
