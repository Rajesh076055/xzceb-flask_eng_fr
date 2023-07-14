"""
This module demonstrates translation between English and French using the deep_translator library.
"""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    Function to translate english to french
    """

    french_text = MyMemoryTranslator(source='en-GB', target='fr-CA').translate(english_text)

    return french_text


def french_to_english(french_text):
    """
    Function to translate french to english
    """

    english_text = MyMemoryTranslator(source="fr-CA",target='en-GB').translate(french_text)

    return english_text


if __name__ == "__main__":
    print(english_to_french("Hello"))
    print(french_to_english("Bonjour"))