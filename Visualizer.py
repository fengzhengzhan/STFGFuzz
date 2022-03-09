import os
import time
import curses
import psutil

from Fuzzconfig import *


class Visualizer:
    def __init__(self):
        # sudo apt reinstall ncurses-base
        self.stdscr = curses.initscr()
        curses.start_color()
        curses.use_default_colors()
        # curses.noecho()  # Turn off command line display back
        self.stdscr.nodelay(True)
        # curses.color_pair(1)
        curses.init_pair(1, curses.COLOR_BLACK, -1)
        curses.init_pair(2, curses.COLOR_BLUE, -1)
        curses.init_pair(3, curses.COLOR_CYAN, -1)
        curses.init_pair(4, curses.COLOR_GREEN, -1)
        curses.init_pair(5, curses.COLOR_MAGENTA, -1)
        curses.init_pair(6, curses.COLOR_RED, -1)
        curses.init_pair(7, curses.COLOR_WHITE, -1)
        curses.init_pair(8, curses.COLOR_YELLOW, -1)


    def display(self, start_time, seed_content: str, eachloop_input_map: dict) -> int:
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
        self.terminal_status = curses.newwin(16, 76, 1, 0)
        self.terminal_status.box()
        self.terminal_status.erase()
        self.terminal_status.border()

        self.terminal_status.addstr(0, 2, "Status")  # (y ->, x |V)
        self.terminal_status.addstr(1, 1, "Runtime: {}".format(runtime))
        self.terminal_status.addstr(2, 1, "    CPU: {}%".format(psutil.cpu_percent()))
        self.terminal_status.addstr(3, 1, "    Mem: {}%".format(psutil.virtual_memory()[2]))
        self.terminal_status.hline(4, 1, curses.ACS_HLINE, 74)
        self.terminal_status.vline(1, 20, curses.ACS_VLINE, 3)
        self.terminal_status.addstr(15, 2, "Q", curses.color_pair(VIS_MAGENTA))
        self.terminal_status.addstr(15, 3, "uit")
        self.terminal_status.addstr(15, 8, "P", curses.color_pair(VIS_MAGENTA))
        self.terminal_status.addstr(15, 9, "ause")


        self.terminal_status.noutrefresh()

        # Initual terminal seeds.
        self.terminal_seeds = curses.newwin(9, 76, 17, 0)
        self.terminal_seeds.box()
        self.terminal_seeds.erase()
        self.terminal_seeds.border()
        self.terminal_seeds.addstr(0, 2, "Hex")  # (y ->, x |V)
        for i in range(1, 8):
            self.terminal_seeds.addstr(i, 1, "00{}0: ".format(i-1))
        seed_len = len(seed_content)
        layout_x = int(seed_len / VIS_SEED_LINE)
        layout_y = int(seed_len % VIS_SEED_LINE)
        for i in range(0, layout_x+1):
            if i < layout_x:
                j_len = VIS_SEED_LINE
            else:
                j_len = layout_y
            for j in range(0, j_len):
                seed_index = i*16+j
                show_char = seed_content[seed_index]
                color_pair = curses.color_pair(VIS_WHITE)
                if seed_index in eachloop_input_map:
                    show_char = eachloop_input_map[seed_index]
                    color_pair = curses.color_pair(VIS_RED)
                self.terminal_seeds.addstr(i+1, j*3+int(j/4)+7, "{} ".format(hex(ord(show_char)))[2:], color_pair)
                self.terminal_seeds.addstr(i+1, j+58, "{}".format(show_char), color_pair)

        self.terminal_seeds.noutrefresh()

        if self.stdscr.getch() == VIS_Q:
            curses.endwin()
            return 1

        return -1









if __name__ == "__main__":
    try:
        test = {0: 'T', 1: 'h', 2: 'e', 3: ' ', 4: 'q', 5: 'u', 6: 'i', 7: 'c', 8: 'k', 9: ' ', 10: 'b',
                11: 'r', 12: 'o', 13: 'w', 14: 'n', 15: ' ', 16: 'f', 17: 'o', 18: 'x', 19: ' '}
        start_time = time.time()
        v = Visualizer()
        while True:
            time.sleep(0.1)
            res = v.display(start_time, "abcdefghijklmnopqrstuvwxyz", test)
            if res == 1:
                break
    except Exception as e:
        curses.endwin()
        print(e)
    # os.system("clear")
    # xnum = ">" * (int(time.time()) % 4)
    # runtime = time.strftime("%d:%H:%M:%S", time.localtime(time.time()-start_time))
    #
    # print("  {} {}".format(BTFUZZ, xnum))
    # print("+----------------------------------------------+------------------------------+")
    # print("| Runtime:  {}".format(runtime))
