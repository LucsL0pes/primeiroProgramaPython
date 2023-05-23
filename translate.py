from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import unittest

authenticator = IAMAuthenticator(
    'Mz2537RTtqOWaQPTzs5OiRjpaZMdMVtCzOsBFSpluxpP')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(
    'https://api.us-south.language-translator.watson.cloud.ibm.com/instances/c21cfa78-652b-4ed7-b6ff-0b3315ac7310')


def english_to_french(text):
    translation = language_translator.translate(
        text=text,
        model_id='en-fr').get_result()
    translated_text = translation['translations'][0]['translation']
    return translated_text


def french_to_english(text):
    translation = language_translator.translate(
        text=text,
        model_id='fr-en').get_result()
    translated_text = translation['translations'][0]['translation']
    return translated_text


class TranslationTests(unittest.TestCase):
    def test_english_to_french(self):
        result = english_to_french("Hello")
        self.assertEqual(result, "Bonjour")

        result = english_to_french("Goodbye")
        self.assertEqual(result, "Au revoir")

    def test_french_to_english(self):
        result = french_to_english("Bonjour")
        self.assertEqual(result, "Hello")

        result = french_to_english("Au revoir")
        self.assertEqual(result, "Goodbye")


if __name__ == '__main__':
    unittest.main()
