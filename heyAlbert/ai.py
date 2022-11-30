## heyAlbert ai file
## created by rightrice
import pyttsx3
import speech_recognition as sr


class ai():
    __name = ""
    __skill = []

    def __init__(self, name=None):
        self.engine = pyttsx3.init()
        self.r = sr.Recognizer()
        self.m = sr.Microphone()
