__author__ = "Shobhit Kundu"
__copyright__ = "Copyright (C) 2020 Shobhit Kundu"
__license__ = "Public Demo"
__version__ = "1.0"

import Calc
from datetime import datetime
import fnmatch
import googlesearch
import json
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.io.preview import preview
import os
import pickle
import pygame
import pyjokes
import random
import re
import Replies as Reply
import requests
import Spk_Listen as Assistant
import sys
from tkinter import *
from tkinter.filedialog import askdirectory
import Translator
import webbrowser

dani = Assistant.AudioExchange()
pygame.init()

months = ['January', 'February', 'March', 'April', 'May', 'June',
         'July', 'August', 'September', 'October', 'November', 'December']

intro = VideoFileClip(r'Assets\Dani Intro.mp4')
listening1 = VideoFileClip(r'Assets\Dani List 1.mp4')
listening2 = pygame.image.load(r'Assets\Dani List 2.png')
listening3 = VideoFileClip(r'Assets\Dani List 3.mp4')
speaking1 = VideoFileClip(r'Assets\Dani Spk 1.mp4')
speaking2 = pygame.image.load(r'Assets\Dani Spk 2.png')
speaking3 = VideoFileClip(r'Assets\Dani Spk 3.mp4')
exitmsg = VideoFileClip(r'Assets\Dani Exit.mp4')

responses = {}

with open('Assets/intents.json', 'r') as file:
    rp_data = json.load(file)
    for intent in rp_data['intents']:
        responses[intent['tag']] = intent["responses"]
with open('Assets/wd_lbl.txt', 'rb') as file:
    word_list, lbl = pickle.load(file)


def speak(text):
    preview(speaking1, 30, False)
    win.blit(speaking2, (0, 0))
    dani.speak(text)
    preview(speaking3, 30, False)
    win.blit(programIcon, (0, 0))
    pygame.display.update()
    print("Dani:", text)


def listen():
    preview(listening1, 30, False)
    win.blit(listening2, (0, 0))
    text = dani.listen()
    preview(listening3, 30, False)
    win.blit(programIcon, (0, 0))
    pygame.display.update()
    try:
        print(f'{data["username"]}:', text)
    except NameError:
        print('user:', text)
    return text


def setup():  # shobhit kundu
    pdata = {}
    d_list = ["username", "music_folder"]
    speak("What should I call you?")
    while True:
        speak('Please Spell your name')
        name = listen()
        if name != "Nothing Recognisable":
            print(name)
            name = ''.join(name.replace(' ', ""))
            speak("I'll Call you " + name)
            speak("Is that correct?")
            confirmation = listen()
            if 'y' in confirmation.lower():
                pdata[d_list[0]] = name
                break
    speak("Can you select the music folder location through the popup window")
    root = Tk()
    pdata[d_list[1]] = str(askdirectory())
    root.destroy()
    return pdata


def ext():
    speak("Are you Sure you want to Exit DANI, The Dynamic Assistive Neural Intelligence?")
    ans = listen()
    if ans == "yes":
        preview(exitmsg, 30, False)
        pygame.quit()
        sys.exit()


def math(eqn):  # shobhit kundu
    """
    :param eqn: Takes verbal or sign based equations and returns answer
    :return: float value either positive or negative
    """
    print(eqn)
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
        tmp = -1 * int(eqn_sp[i + 1])
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
            print(f"function at {i + 1}")
            if type(eqn_sp[i - 1]) == str:
                nm1 = int(eqn_sp[i - 1])
            else:
                nm1 = eqn_sp[i - 1]
            if type(eqn_sp[i + 1]) == str:
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
            eqn_sp.pop(i - 1)
            eqn_sp.pop(i)
            eqn_sp.pop(i - 1)
            eqn_sp.insert(i - 1, answer)
            print(f"Final Equation: {eqn_sp}\n")
    speak(eqn_sp[0])
    print(eqn_sp[0])
    return eqn_sp[0]


def joke(category='Random'):  # shobhit kundu
    """
    :param category: Choices: 'neutral', 'chuck', 'all', 'twister', 'Random'
    :return: string based joke
    """
    if category == 'Random':
        return pyjokes.get_joke(category=random.choice(['neutral', 'chuck', 'all', 'twister']))
    return pyjokes.get_joke(category=category)


def pmusicoffl(m_name):  # shobhit kundu
    """
    :param m_name: Song name or path
    :return: None
    """
    s_file = find_files(m_name, data['music_folder'])
    r = 0
    if 'Nothing Found' not in s_file:
        if len(s_file) > 1:
            r = random.randint(0, len(s_file) - 1)
        os.startfile(s_file[r])
        print(s_file)
    else:
        print(s_file)
        try:
            pmusiconl(m_name)
        except:
            pass
    return


def find_files(filename, search_path):  # shobhit kundu
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


def date_time(mode="None"):  # shobhit kundu
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
        return "Today's Date is {}th of {}, {}".format(day, months[month-1], year)
    elif mode == 'time':
        m = ''
        if hour >= 12:
            m = "pm"
        else:
            m = 'am'
        return "Current Time = {}:{} {}".format(hour, minute, m)
    else:
        return "{}: {}, {}-{}-{}".format(hour, minute, day, month, year)


def open_url(url):  # shobhit kundu
    webbrowser.open_new(url)
    return


def net_availability():  # shobhit kundu
    try:
        requests.request('str', url='https://www.google.com/')
        return True
    except:
        return False


def pyoutube():  # yash meshram
    pass


def gsearch(query, count=10):  # shobhit kundu
    """
    :param query: name or item to search
    :param count: number of results wanted
    :return: list of result links
    """
    results = googlesearch.search(query, stop=count)
    return [x for x in results]


def pmusiconl(m_name):  # abhishek verma
    pass


def wiki(query):
    """
    :param query: name or item to search
    :return: short text and link to webpage
    """
    url = "https://en.wikipedia.org/w/api.php"
    params = {"action": "query", "format": "json", "list": "search", "srsort": "just_match",
              "srsearch": query, 'snippet': 'True'}

    try:
        r = requests.get(url=url, params=params)
        jdat = r.json()
        searches = jdat['query']['search']

        ignorets = ['<span class="searchmatch">', '</span>', '&quot;']
        text = searches[0]['snippet']
        for i in ignorets:
            text = text.replace(i, "")
            return text, r.url
    except:
        return


def reply():  # shobhit kundu
    replies = ''
    text = listen()

    if text == "Nothing Recognisable":
        return "Nothing Recognisable"

    actions = {'goodbye': ext,
               'music': pmusicoffl,
               'time': date_time,
               'date': date_time,
               'maths': math,
               'joke': joke,
               'yt-video': pyoutube,
               'google': gsearch,
               'open-webpage': open_url,
               'connectivity-check': net_availability()}
    rep = {'category': (Reply.reply(text))[0], 'ign_words': (Reply.reply(text))[1]}

    if rep['category'] in ['devs', 'greeting', 'name', "thanks", "help"]:
        replies = random.choice(responses[rep['category']])

    else:
        tmp = []

        for i in rep['ign_words']:
            if i not in word_list:
                tmp.append(i)

        dt = rep['ign_words']
        print(tmp, dt)

        if rep['category'] == 'goodbye':
            ext()

        elif rep['category'] == 'music':
            callable(actions[rep['category']](' '.join(tmp)))

        elif rep['category'] == 'time':
            return date_time("time")

        elif rep['category'] == 'date':
            return date_time("date")

        elif rep['category'] == 'maths':
            replies = math(' '.join(dt))
            print(replies)

        elif rep['category'] == 'joke':
            return joke('all')

        elif rep['category'] == 'yt-video':
            if not net_availability():
                return "Sorry, You're not Connected to the internet"
            pass

        elif rep['category'] == 'google':
            if not net_availability():
                return "Sorry, You're not Connected to the internet"
            searches = gsearch(" ".join(tmp))
            try:
                text, link = wiki(" ".join(tmp))

            except:
                text = ''
                link = ''
            if text != '':
                speak(text)
                speak('would you like me to open the wiki page for your search?')
                rtpl = listen()
                if rtpl == 'yes':
                    open_url(link)
            speak(f'got first 10 search results for {" ".join(tmp)} from google. would you like me to open them?')
            rtpl = listen()
            if rtpl == 'yes':
                for i in searches:
                    open_url(i)

        elif rep['category'] == 'open-webpage':
            if not net_availability():
                return "Sorry, You're not Connected to the internet"
            open_url(tmp[0])

        elif rep['category'] == 'connectivity-check':
            if net_availability():
                replies = "You're Connected to the internet"
            else:
                replies = "You're Disconnected from the internet"
    return replies


if __name__ == '__main__':

    win = pygame.display.set_mode((256, 256))
    pygame.display.set_caption("DANI")
    programIcon = pygame.image.load(r'Assets\DANI Logo 2.ico')
    pygame.display.set_icon(programIcon)
    win.fill('black')
    pygame.time.delay(1000)
    preview(intro, 30, False)
    intro.close()
    win.blit(programIcon, (0, 0))
    pygame.display.update()

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

    running = True
    while running:
        pygame.time.delay(100)
        for env in pygame.event.get():
            if env.type == pygame.QUIT:
                preview(exitmsg, 30, False)
                pygame.quit()
                sys.exit()

            if env.type == pygame.MOUSEBUTTONDOWN:
                print("mouse")
                rpl = reply()
                speak(rpl)
                print(rpl)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] or keys[pygame.MOUSEBUTTONDOWN]:
            print("space")
            rpl = reply()
            speak(rpl)
            print(rpl)

    pygame.display.update()
