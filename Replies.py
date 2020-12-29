__author__ = "Shobhit Kundu"
__copyright__ = "Copyright (C) 2020 Shobhit Kundu"
__license__ = "Public Demo"
__version__ = "1.0"


from tensorflow import keras
import nltk
from nltk.stem import LancasterStemmer
import pickle
import numpy as np
stemmer = LancasterStemmer()


with open('Assets/wd_lbl.txt', 'rb') as file:
    words, labels = pickle.load(file)
    if not words:
        raise EOFError
    if not labels:
        raise EOFError
model = keras.models.load_model("Assets/chatbot.h5")
print(model.summary())


def bag_of_words(text):
    trn = []
    wrd = nltk.word_tokenize(text.lower())
    print(wrd)
    # print(words)
    jk = np.zeros(len(words))
    for idt, dt in enumerate(words):
        if dt in wrd:
            jk[idt] = 1
    trn.append(jk)
    trn = np.array(trn)
    return trn, wrd


def reply(text):
    bow, word_lst = bag_of_words(text)
    beta = model.predict(bow)
    highest = int(np.argmax(beta))
    print(highest, labels[highest])
    category = labels[highest]
    return category, word_lst
