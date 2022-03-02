import os
import time

from Fuzzconfig import *

def display() -> None:
    '''
    This function use to show state during fuzzing on the terminal.
    '''
    xnum = ">" * (int(time.time()) % 4)
    print("  {} {}".format(BTFUZZ, xnum))


    while True:
        for i in range(10):
            time.sleep(0.2)
            os.system("clear")
            j = i + 10
            print("Loading... {}\{}".format(i, j))
            print("Loading... {}\{}".format(i, j))





if __name__ == "__main__":
    print("ok")
    display()