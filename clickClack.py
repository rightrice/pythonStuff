import sys
from time import sleep
from typing import Tuple
from playsound import playsound

DELAY: float = .1
def clickClack(*paragraph:str) -> None:
    for sentence in paragraph:
        for char in sentence:
            sys.stdout.write(char)
            sys.stdout.flush()
            sleep(DELAY)
        print()
        sleep(DELAY)
        playsound('typewriter-1.wav')

clickClack("hello, I am rightrice.")
name0 = input("what is your name? ")
clickClack("hello, " + name0 + "!")