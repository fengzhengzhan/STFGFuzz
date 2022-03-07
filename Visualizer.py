import os
import time
import curses
import psutil

from Fuzzconfig import *

class Visualizer:
    def __init__(self):
        self.stdscr = curses.initscr()
        curses.start_color()
        curses.noecho()  # Turn off command line display back
        self.stdscr.nodelay(True)


    def display(self, start_time, seed_content: str, eachloop_input_map: dict) -> None:
        '''
        This function use to show state during fuzzing on the terminal.
        '''
        xnum = ">" * (int(time.time()) % 5)
        runtime = time.strftime("%H:%M:%S", time.gmtime(time.time()-start_time))

        # Title.
        self.stdscr.erase()
        self.stdscr.noutrefresh()
        self.stdscr.addstr(0, 0, " {} {}".format(BTFUZZ, xnum))
        # self.stdscr.refresh()

        # Initual terminal status.
        self.terminal_status = curses.newwin(16, 80, 1, 0)
        self.terminal_status.box()
        self.terminal_status.erase()
        self.terminal_status.border()

        self.terminal_status.addstr(0, 2, "Status")  # (y ->, x |V)
        self.terminal_status.addstr(1, 1, "Runtime: {}".format(runtime))
        self.terminal_status.addstr(2, 1, "CPU: {}%".format(psutil.cpu_percent()))
        self.terminal_status.addstr(3, 1, "Mem: {}%".format(psutil.virtual_memory()[2]))
        self.terminal_status.hline(4, 1, curses.ACS_HLINE, 64)
        self.terminal_status.vline(1, 20, curses.ACS_VLINE, 3)

        self.terminal_status.noutrefresh()

        # Initual terminal seeds.
        self.terminal_seeds = curses.newwin(9, 80, 17, 0)
        self.terminal_seeds.box()
        self.terminal_seeds.erase()
        self.terminal_seeds.border()
        self.terminal_seeds.addstr(0, 2, "Hex")  # (y ->, x |V)
        for i in range(1, 8):
            self.terminal_seeds.addstr(i, 1, "00{}0: ".format(i-1))


        self.terminal_seeds.noutrefresh()


        if self.stdscr.getch() == 113:
            curses.endwin()
            return 1
        else:
            self.stdscr.getch()









if __name__ == "__main__":
    test = {0: 'T', 1: 'h', 2: 'e', 3: ' ', 4: 'q', 5: 'u', 6: 'i', 7: 'c', 8: 'k', 9: ' ', 10: 'b',
            11: 'r', 12: 'o', 13: 'w', 14: 'n', 15: ' ', 16: 'f', 17: 'o', 18: 'x', 19: ' '}
    start_time = time.time()
    v = Visualizer()
    while True:
        time.sleep(0.1)
        res = v.display(start_time, "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA", test)
        if res == 1:
            break

    # os.system("clear")
    # xnum = ">" * (int(time.time()) % 4)
    # runtime = time.strftime("%d:%H:%M:%S", time.localtime(time.time()-start_time))
    #
    # print("  {} {}".format(BTFUZZ, xnum))
    # print("+----------------------------------------------+------------------------------+")
    # print("| Runtime:  {}".format(runtime))
