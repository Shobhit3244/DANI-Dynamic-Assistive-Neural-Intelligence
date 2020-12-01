__author__ = "Shobhit Kundu"
__copyright__ = "Copyright (C) 2020 Shobhit Kundu"
__license__ = "Public Demo"
__version__ = "1.0"

import speech_recognition as vr
import pyttsx3 as tts
from playsound import playsound as mplayer
assistant = tts.init()
MicInp = vr.Recognizer()


class AudioExchange(object):
    def __init__(self, name=None, voice_threshold=500, min_phase=0.2, word_break=0.5, assist_gender=1, hfxtra=0):
        self.name = name
        self.voice_th = voice_threshold
        self.breadth_delay = word_break
        self.pause_th = min_phase
        self.gender = assist_gender
        self.hfxtra = hfxtra

    def speak(self, audio_data):
        assistant.setProperty('voice', assistant.getProperty('voices')[self.gender].id)
        assistant.say(audio_data)
        assistant.runAndWait()

    def listen(self, timeout=None):
        MicInp.pause_threshold = self.breadth_delay
        MicInp.phrase_threshold = self.pause_th
        MicInp.energy_threshold = self.voice_th
        MicInp.non_speaking_duration = self.hfxtra
        MicInp.operation_timeout = timeout
        with vr.Microphone() as Mic:
            mplayer("start.mp3")
            RcdAudio = MicInp.listen(Mic)
            mplayer("end.mp3")
        try:
            statement = MicInp.recognize_google(RcdAudio)
        except Exception:
            statement = "nothing Recognisable"
        return statement
