import sys
from time import sleep
from typing import Tuple

DELAY: float = .1
def clickClack(*paragraph:str) -> None:
    for sentence in paragraph:
        for char in sentence:
            sys.stdout.write(char)
            sys.stdout.flush()
            sleep(DELAY)
        print()
        sleep(DELAY)

clickClack("hello, I am rightrice.")
name0 = input("what is your name? ")
clickClack("hello, " + name0 + "!")