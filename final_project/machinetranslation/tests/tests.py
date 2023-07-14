from unittest import TestCase
import unittest
from machinetranslation.translator import english_to_french,french_to_english



class testTranslation(TestCase):

    def test_english2french(self):

        self.assertEqual(english_to_french("Hello"),"Bonjour")

    def test_french2english(self):
        self.assertEqual(french_to_english("Bonjour"),"Hello")



unittest.main()
