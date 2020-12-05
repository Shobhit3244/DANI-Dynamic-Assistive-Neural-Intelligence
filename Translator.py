__author__ = "Shobhit Kundu"
__copyright__ = "Copyright (C) 2020 Shobhit Kundu"
__license__ = "Public Demo"
__version__ = "1.0"

from googletrans import Translator
from googletrans.constants import (LANGUAGES, SPECIAL_CASES)
assist = Translator()


def lang_detect(text):
    """
    It detects the language of the input text
    :param text: str of the text language to be detected
    :return: str language of the text
    """
    dct = assist.detect(text)
    try:
        return LANGUAGES[dct.lang]
    except:
        return dct.lang


def translate(text, toL='en'):
    """
    It translates the given text to desired language. default to language is english
    :param text: str text to translate
    :param toL: str language to translate the text to
    :return: str of the translated text
    """
    trnd = assist.translate(text, dest=toL)
    return trnd.text

