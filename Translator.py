__author__ = "Shobhit Kundu"
__copyright__ = "Copyright (C) 2020 Shobhit Kundu"
__license__ = "Public Demo"
__version__ = "1.0"

from googletrans import Translator
from googletrans.constants import (LANGUAGES, SPECIAL_CASES)
assist = Translator()


def lang_detect(text):
    dct = assist.detect(text)
    try:
        return LANGUAGES[dct.lang]
    except:
        return dct.lang



def translate(text, toL='en'):
    trnd = assist.translate(text, dest=toL)
    return trnd.text

