import os
import time

from Fuzzconfig import *


def display() -> None:
    '''
    This function use to show state during fuzzing on the terminal.
    '''
    os.system("clear")
    xnum = ">" * (int(time.time()) % 4)
    print("  {} {}".format(BTFUZZ, xnum))



if __name__ == "__main__":
    print("ok")
    display()