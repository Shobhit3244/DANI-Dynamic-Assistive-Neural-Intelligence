__author__ = "Shobhit Kundu"
__copyright__ = "Copyright (C) 2020 Shobhit Kundu"
__license__ = "Public Demo"
__version__ = "1.0"

import googlesearch
import Translator
import Spk_Listen as Assistant
import requests
import webbrowser
from moviepy.editor import *
from tkinter.filedialog import askdirectory
# import Replies as Reply
import Calc
from datetime import datetime
import sys
import os
import fnmatch
import random
import pyjokes
import pickle
import pygame

dani = Assistant.AudioExchange()
pygame.init()

listening1 = VideoFileClip(r'Assets\Dani List 1.mp4')
listening2 = pygame.image.load(r'Assets\Dani List 2.png')
listening3 = VideoFileClip(r'Assets\Dani List 3.mp4')


win = pygame.display.set_mode((256, 256))
pygame.display.set_caption("DANI - Dynamic Assistive Neural Intelligence")
programIcon = pygame.image.load(r'Assets\DANI Logo 2.ico')
pygame.display.set_icon(programIcon)
win.fill('black')
win.blit(programIcon, (0, 0))
pygame.display.update()


def speak(text):
    dani.speak(text)


def listen():
    listening1.preview()
    win.blit(listening2, (0, 0))
    text = dani.listen()
    listening3.preview()
    win.blit(programIcon, (0, 0))
    pygame.display.update()
    print(text)
    return text


def setup():        # shobhit kundu
    pdata = {}
    d_list = ["username", "music_folder"]
    speak("What should I call you?")
    while True:
        speak('Please Spell your name')
        name = listen()
        if name != "Nothing Recognisable":
            print(name)
            name = ''.join(name.replace(' ', ""))
            speak("I'll Call you "+name)
            speak("Is that correct?")
            confirmation = listen()
            if confirmation.lower() == 'yes':
                pdata[d_list[0]] = name
                break
    speak("Can you select the music folder location through the popup window")
    pdata[d_list[1]] = str(askdirectory())
    return pdata


def translate(text, tol="en", mode="trans"):    # shobhit kundu
    """
    :param text: text to translate or detect language
    :param mode: trans=translate, dctLang=detect Language
    :param tol: 'af': 'afrikaans', 'sq': 'albanian', 'am': 'amharic', 'ar': 'arabic', 'hy': 'armenian',
                'az': 'azerbaijani', 'eu': 'basque', 'be': 'belarusian', 'bn': 'bengali', 
                'bs': 'bosnian', 'bg': 'bulgarian', 'ca': 'catalan', 'ceb': 'cebuano', 'ny': 'chichewa', 
                'zh-cn': 'chinese (simplified)', 'zh-tw': 'chinese (traditional)', 'co': 'corsican', 'hr': 'croatian', 
                'cs': 'czech', 'da': 'danish', 'nl': 'dutch', 'en': 'english', 'eo': 'esperanto', 
                'et': 'estonian', 'tl': 'filipino', 'fi': 'finnish', 'fr': 'french', 'fy': 'frisian', 
                'gl': 'galician', 'ka': 'georgian', 'de': 'german', 'el': 'greek', 'gu': 'gujarati', 
                'ht': 'haitian creole', 'ha': 'hausa', 'haw': 'hawaiian', 'iw': 'hebrew', 'he': 'hebrew', 
                'hi': 'hindi', 'hmn': 'hmong', 'hu': 'hungarian', 'is': 'icelandic', 'ig': 'igbo', 
                'id': 'indonesian', 'ga': 'irish', 'it': 'italian', 'ja': 'japanese', 'jw': 'javanese', 
                'kn': 'kannada', 'kk': 'kazakh', 'km': 'khmer', 'ko': 'korean', 'ku': 'kurdish (kurmanji)', 
                'ky': 'kyrgyz', 'lo': 'lao', 'la': 'latin', 'lv': 'latvian', 'lt': 'lithuanian', 
                'lb': 'luxembourgish', 'mk': 'macedonian', 'mg': 'malagasy', 'ms': 'malay', 
                'ml': 'malayalam', 'mt': 'maltese', 'mi': 'maori', 'mr': 'marathi', 'mn': 'mongolian', 
                'my': 'myanmar (burmese)', 'ne': 'nepali', 'no': 'norwegian', 'or': 'odia', 'ps': 'pashto', 
                'fa': 'persian', 'pl': 'polish', 'pt': 'portuguese', 'pa': 'punjabi', 'ro': 'romanian', 
                'ru': 'russian', 'sm': 'samoan', 'gd': 'scots gaelic', 'sr': 'serbian', 'st': 'sesotho', 
                'sn': 'shona', 'sd': 'sindhi', 'si': 'sinhala', 'sk': 'slovak', 'sl': 'slovenian', 
                'so': 'somali', 'es': 'spanish', 'su': 'sundanese', 'sw': 'swahili', 'sv': 'swedish', 
                'tg': 'tajik', 'ta': 'tamil', 'te': 'telugu', 'th': 'thai', 'tr': 'turkish', 
                'uk': 'ukrainian', 'ur': 'urdu', 'ug': 'uyghur', 'uz': 'uzbek', 'vi': 'vietnamese', 
                'cy': 'welsh', 'xh': 'xhosa', 'yi': 'yiddish', 'yo': 'yoruba', 'zu': 'zulu'
    """
    if mode == "dctLang": 
        return Translator.lang_detect(text)

    elif mode == "trans": 
        return Translator.translate(text, tol)


def math(eqn):         # shobhit kundu
    """
    :param eqn: Takes verbal or sign based equations and returns answer
    :return: float value either positive or negative
    """
    operators = {'add': ['sum', '+', 'plus', 'with', 'add'], 
                 'sub': ['remove', 'substract', 'sub', 'minus', '-'], 
                 'sqr': ['to the power', 'power', '^', '**'], 
                 'mul': ['into', 'times', 'time', 'multiply', 'x', '*'], 
                 'div': ['by', 'divided', '/'], 
                 'log': ['log'], 
                 'rt': ['root']}
    for i in operators: 
        for k in operators[i]: 
            if k in eqn: 
                eqn = eqn.replace(k, i)
    answer = 0
    eqn_sp = eqn.split()
    func = {'log': 0, 'sqr': 0, 'rt': 0, 'div': 0, 'mul': 0, 'add': 0, 'sub': 0}
    while "sub" in eqn_sp: 
        i = eqn_sp.index("sub")
        tmp = -1*int(eqn_sp[i+1])
        eqn_sp.pop(i)
        eqn_sp.pop(i)
        # noinspection PyTypeChecker
        eqn_sp.insert(i, tmp)
        eqn_sp.insert(i, 'add')

    for i in func: 
        func[i] = eqn_sp.count(i)
    print(f"{func}\n{eqn_sp}")
    for t in func: 
        print(f"\nfunction {t}, appears {func[t]} times")
        if func[t] == 0: 
            print("----skip----\n")
            continue
        for v in range(func[t]): 
            i = eqn_sp.index(t)
            print(f"function at {i+1}")
            if type(eqn_sp[i-1]) == str:
                nm1 = int(eqn_sp[i-1])
            else: 
                nm1 = eqn_sp[i-1]
            if type(eqn_sp[i+1]) == str:
                nm2 = int(eqn_sp[i + 1])
            else: 
                nm2 = eqn_sp[i + 1]
            print("Initial Equation: {}\nFunction on : {} {} {}".format(eqn_sp, nm1, t, nm2, ))
            if t == 'log': 
                answer = Calc.log(nm1, nm2)
            elif t == 'sqr': 
                answer = Calc.sqr(nm1, nm2)
            elif t == 'rt': 
                answer = Calc.rt(nm1, nm2)
            elif t == 'div': 
                answer = Calc.div(nm1, nm2)
            elif t == 'mul': 
                answer = Calc.mul(nm1, nm2)
            elif t == 'add': 
                answer = Calc.add(nm1, nm2)
            elif t == 'sub': 
                answer = Calc.sub(nm1, nm2)

            print(f"Answer: {answer}")
            eqn_sp.pop(i-1)
            eqn_sp.pop(i)
            eqn_sp.pop(i-1)
            eqn_sp.insert(i-1, answer)
            print(f"Final Equation: {eqn_sp}\n")
    return eqn_sp[0]


def joke(category='Random'):         # shobhit kundu
    """
    :param category: Choices: 'neutral', 'chuck', 'all', 'twister', 'Random'
    :return: string based joke
    """
    if category == 'Random': 
        return pyjokes.get_joke(category=random.choice(['neutral', 'chuck', 'all', 'twister']))
    return pyjokes.get_joke(category=category)


def pmusicoffl(m_name):   # shobhit kundu
    """
    :param m_name: Song name or path
    :return: None
    """
    s_file = find_files(m_name, data['music_folder'])
    r = 0
    if 'Nothing Found' not in s_file: 
        if len(s_file) > 1: 
            r = random.randint(0, len(s_file)-1)
        os.startfile(s_file[r])
        print(s_file)
    else: 
        print(s_file)
    return


def find_files(filename, search_path):    # shobhit kundu
    """
    :param filename: name of the file to search
    :param search_path: where to search the file
    :return: list or occurrences of that file or name
    """
    result1 = []
    result = []
    for root, dirt, files in os.walk(search_path): 
        for name in files: 
            if fnmatch.fnmatch(name, f"*{filename}*.mp3"): 
                result1.append(os.path.join(root, name))

    print(result)
    if len(result1) != 0: 
        for i in result1: 
            print(i, i.replace('\\\\', "\\"))
            result.append(i)
    else: 
        result.append('Nothing Found')
    print(result)
    return result


def date_time(mode="None"):     # shobhit kundu
    """
    :param mode: 'date', 'time', 'None'
    :return: time in string format
    """
    day = datetime.now().day
    month = datetime.now().month
    year = datetime.now().year
    hour = datetime.now().hour
    minute = datetime.now().minute
    if mode == 'date': 
        return "Today's Date = {}-{}-{}".format(day, month, year)
    elif mode == 'time': 
        return "Current Time = {}: {}".format(hour, minute)
    else: 
        return "{}: {}, {}-{}-{}".format(hour, minute, day, month, year)


def open_url(url):     # shobhit kundu
    webbrowser.open_new(url)
    return


def net_availability():     # shobhit kundu
    try:
        requests.request('str', url='https://www.google.com/')
        return True
    except:
        return False


def replies():      # shobhit kundu
    pass


def pyoutube():     # yash meshram
    pass


def gsearch(query, count=10):      # shobhit kundu
    """
    :param query: name or item to search
    :param count: number of results wanted
    :return: list of result links
    """
    results = googlesearch.search(query, stop=count)
    return [x for x in results]


def pmusiconl():    # abhishek verma
    pass


if __name__ == '__main__':
    try:
        with open("Config.conf", "rb") as rfile:
            data = pickle.load(rfile)
            if not data or not data['username'] or not data['music_folder']:
                raise ValueError("Nothing Found In File")
            print(data)
        print("Config Loaded Successfully")

    except:
        with open("Config.conf", "wb+") as nfile:
            data = setup()
            pickle.dump(data, nfile)
        print("setup done")

    run = True
    while run:
        pygame.time.delay(100)
        for env in pygame.event.get():
            if env.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if env.type == pygame.MOUSEBUTTONDOWN:
                print(listen(), "mouse")

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] or keys[pygame.MOUSEBUTTONDOWN]:
            print(listen(), "space")
    pygame.display.update()
