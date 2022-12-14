## heyAlfred ai file
## created by rightrice
import pyttsx3
import speech_recognition as sr


class ai():
    __name = "Alfred"
    __skill = []

    def __init__(self, name=None):
        self.engine = pyttsx3.init()
        self.r = sr.Recognizer()
        self.m = sr.Microphone()

        if name is not None:
            self.__name = name

        print("Listening")
        with self.m as source:
            self.r.adjust_for_ambient_noise(source)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        sentence = "Hello, my name is" + self.__name
        self.__name = value
        self.engine.say(sentence)
        self.engine.runAndWait()

    def say(self, sentence):
        self.engine.say(sentence)
        self.engine.runAndWait()

    def listen(self):
        print("You rang?")
        with self.m as source:
            audio = self.r.listen(source)
        print("on it")
        try:
            phrase = self.r.recognize_google(audio, show_all=False, language="en")
            sentence = "Just to confirm, you said" + phrase
            self.engine.say(sentence)
            self.engine.runAndWait()
        except error as error:
            print("Sorry, I didn't hear you",error)
            self.engine.say("Sorry, I misunderstood")
            self.engine.runAndWait()
        print("You said," + phrase)
        return phrase