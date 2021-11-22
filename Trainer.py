__author__ = "Shobhit Kundu"
__copyright__ = "Copyright (C) 2020 Shobhit Kundu"
__license__ = "Public Demo"
__version__ = "1.0"

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, models
import nltk
from nltk.stem import LancasterStemmer
from sklearn.utils import shuffle
from tensorflow.keras.layers.experimental.preprocessing import TextVectorization
import pickle
import numpy as np
import string
import re
import json
stemmer = LancasterStemmer()


try:
    with open('Assets/wd_lbl.txt', 'rb') as file:
        words, labels = pickle.load(file)
        if not words:
            raise EOFError
        if not labels:
            raise EOFError
    model = keras.models.load_model("Assets/chatbot.h5")
    raise SyntaxError
except:
    stemmer = LancasterStemmer()

    words = []
    labels = []
    doc_x = []
    doc_y = []


    def custom_standardization(input_data):
        lowercase = tf.strings.lower(input_data)
        stripped_html = tf.strings.regex_replace(lowercase, '<br />', ' ')
        return tf.strings.regex_replace(stripped_html, '[%s]' % re.escape(string.punctuation), '')


    max_features = 10000
    sequence_length = 250

    vectorize_layer = TextVectorization(
        standardize=custom_standardization,
        max_tokens=max_features,
        output_mode='int',
        output_sequence_length=sequence_length)

    with open('Assets/intents.json') as file:
        data = json.load(file)

    for intent in data['intents']:
        labels.append(intent['tag'])
        for pattern in intent['patterns']:
            word = nltk.word_tokenize(pattern.lower())
            words.extend(word)
            doc_x.append(word)
            doc_y.append(intent['tag'])

    doc_xv = []
    doc_yv = []
    vectorize_layer.adapt([' '.join(i) for i in doc_x])
    words = [stemmer.stem(w.lower()) for w in words if w not in ["?", '{', '}']]
    words = sorted(list(set(words + vectorize_layer.get_vocabulary())))

    for i in doc_x:
        tmp = np.zeros(len(words))
        for x, p in enumerate(words):
            if p in i:
                tmp[x] = 1
        doc_xv.append(tmp)
    for i in doc_y:
        tmp = np.zeros(len(labels))
        for y, p in enumerate(labels):
            if p == i:
                tmp[y] = 1
        doc_yv.append(tmp)

    doc_xv, doc_yv = shuffle(doc_xv, doc_yv)
    doc_xv, doc_yv = np.array(doc_xv), np.array(doc_yv)
    print(f"labels:\n{labels}\n\nwords:\n{words}\n\ndoc_x:\n{doc_x}\n\ninput data:\n{doc_xv}\n\ndoc_y:\n{doc_y}\n\n",
          f"output data:\n{doc_yv}")

    optimizer = tf.optimizers.Adam(learning_rate=0.0001)
    model = models.Sequential([
        layers.Dense(50, 'linear', input_shape=np.shape(doc_xv)),
        layers.Dense(30, 'linear'),
        layers.Dense(len(doc_yv[0]), 'linear'),
        layers.Activation('softmax')
    ])

    model.summary()

    doc_xv, doc_yv = shuffle(doc_xv, doc_yv)
    doc_xv, doc_yv = np.array(doc_xv), np.array(doc_yv)

    model.compile(loss='MeanSquaredError', optimizer=optimizer, metrics=['accuracy'])
    model.fit(x=doc_xv, y=doc_yv, batch_size=5, epochs=1000, verbose=2)

    model.save("Assets/chatbot.h5")
    with open("Assets/wd_lbl.txt", "wb+") as file:
        pickle.dump((words, labels), file)

print(model.summary())
# main part


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
