import os
import time

def display() -> None:
    '''
    This function use to show state during fuzzing on the terminal.
    '''
    try:
        size = os.get_terminal_size()
    except Exception as e:
        print("Run with terminal for better format.")




    while True:
        for i in range(10):
            time.sleep(0.2)
            os.system("clear")
            j = i + 10
            xx = ">" * (int(time.time()) % 4)
            print("  BTFuzz {}".format(xx))
            print("Loading... {}\{}".format(i, j))
            print("Loading... {}\{}".format(i, j))





if __name__ == "__main__":
    print("ok")
    display()