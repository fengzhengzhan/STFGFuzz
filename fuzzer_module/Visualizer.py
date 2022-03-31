import os
import time
import curses
import psutil
import graphviz
import matplotlib
import matplotlib.pyplot as plt
import networkx as nx
from PIL import Image  # Read .png format images.

from fuzzer_module.Fuzzconfig import *


class Visualizer:
    def __init__(self):
        # sudo apt reinstall ncurses-base
        self.terminal_switch = VIS_TERMINAL
        self.showgraph_switch = VIS_SHOWGRAPH

        if self.terminal_switch:
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

        if self.showgraph_switch:
            pass
            # plt.ion()

    def __del__(self):
        try:
            if self.stdscr is not None:
                curses.endwin()
        except Exception as e:
            pass

    def display(self, start_time, mutseed: StructSeed, eachloop_input_map: dict, loop: int, total: int) -> int:
        """
        This function use to show state during fuzzing on the terminal.
        @param start_time:
        @param mutseed:
        @param eachloop_input_map:
        @param loop:
        @param total:
        @return:
        """
        if self.terminal_switch:
            xnum = ">" * (int(time.time()) % 5)
            last_time = time.time()-start_time
            runtime = time.strftime("%H:%M:%S", time.gmtime(last_time))


            # Title.
            self.stdscr.erase()
            self.stdscr.noutrefresh()
            self.stdscr.addstr(0, 0, " {} {}".format(FUZZNAME, xnum), curses.color_pair(VIS_BLUE))
            # self.stdscr.refresh()

            # Initual terminal status.
            self.terminal_status = curses.newwin(16, 78, 1, 0)
            self.terminal_status.box()
            self.terminal_status.erase()
            self.terminal_status.border()

            self.terminal_status.addstr(0, 2, "Status")  # (y ->, x |V)
            self.terminal_status.addstr(1, 1, "Runtime: {}".format(runtime))
            self.terminal_status.addstr(2, 1, "    CPU: {}%".format(psutil.cpu_percent()))
            self.terminal_status.addstr(3, 1, "    Mem: {}%".format(psutil.virtual_memory()[2]))
            self.terminal_status.addstr(1, 21, " Loop Number: {}".format(loop))
            self.terminal_status.addstr(2, 21, "Total Number: {}".format(total))
            self.terminal_status.addstr(3, 21, "       Speed: {} e/s".format(int(total/last_time)))
            self.terminal_status.hline(4, 1, curses.ACS_HLINE, 76)
            self.terminal_status.vline(1, 20, curses.ACS_VLINE, 3)
            self.terminal_status.addstr(15, 2, "Q", curses.color_pair(VIS_MAGENTA))
            self.terminal_status.addstr(15, 3, "uit")
            self.terminal_status.addstr(15, 8, "S", curses.color_pair(VIS_MAGENTA))
            self.terminal_status.addstr(15, 9, "how_graph")
            self.terminal_status.addstr(15, 20, "N", curses.color_pair(VIS_MAGENTA))
            self.terminal_status.addstr(15, 21, "ot_show")

            self.terminal_status.noutrefresh()

            # Initual terminal seeds.
            seed_len = len(mutseed.content)
            layout_x = int(seed_len / VIS_SEED_LINE)
            layout_y = int(seed_len % VIS_SEED_LINE)

            self.terminal_seeds = curses.newwin(layout_x+1+2, 78, 17, 0)
            self.terminal_seeds.box()
            self.terminal_seeds.erase()
            self.terminal_seeds.border()
            self.terminal_seeds.addstr(0, 2, "Hex")  # (y ->, x |V)

            for i in range(0, min(layout_x, VIS_MAX_LINE)+1):
                self.terminal_seeds.addstr(i + 1, 1, "{:0>3d}0: ".format(i))
                if i < layout_x or layout_x > VIS_MAX_LINE:
                    j_len = VIS_SEED_LINE
                else:
                    j_len = layout_y

                for j in range(0, j_len):
                    seed_index = i*16+j
                    show_char = mutseed.content[seed_index]
                    color_pair = curses.color_pair(VIS_WHITE)
                    if seed_index in mutseed.location:
                        color_pair = curses.color_pair(VIS_YELLOW)
                    if seed_index in eachloop_input_map:
                        show_char = eachloop_input_map[seed_index]
                        color_pair = curses.color_pair(VIS_RED)
                    self.terminal_seeds.addstr(i+1, j*3+int(j/4)+7, "{} ".format(hex(ord(show_char)))[2:], color_pair)
                    self.terminal_seeds.addstr(i+1, j+int(j/4)+58, "{}".format(show_char), color_pair)

            self.terminal_seeds.noutrefresh()

            if self.stdscr.getch() == VIS_Q:
                return 1
            elif self.stdscr.getch() == VIS_S:
                self.showgraph_switch = True
            elif self.stdscr.getch() == VIS_N:
                self.showgraph_switch = False

        return -1

    def showGraph(self, filepath_graph: str, cggraph: 'Graph', cfggraph: 'Graph'):
        if self.showgraph_switch:
            # Call Graph
            dotcg = graphviz.Digraph(comment="Call Graoh")
            for one in cggraph.dg.nodes:
                # print(one, cggraph.dg.nodes[one][BUI_NODE_LABEL])
                dotcg.node(str(one), str(cggraph.dg.nodes[one][BUI_NODE_LABEL]))

            for one in cggraph.dg.edges:
                # print(one)
                dotcg.edge(str(one[0]), str(one[1]), "")

            cgpath = dotcg.render(directory=filepath_graph, filename=VIS_CG_NAME, format='png')

            # Control Flow Graph
            dotcfg = graphviz.Digraph(comment="Control Flow Graph")
            for one in cfggraph.dg.nodes:
                # print(one, cggraph.dg.nodes[one][BUI_NODE_LABEL])
                node_cont = ""
                if len(cfggraph.dg.nodes[one][BUI_NODE_LABEL]) > 0:
                    node_cont = cfggraph.dg.nodes[one][BUI_NODE_LABEL]
                    node_cont = str(node_cont)[1:-1]
                if len(cfggraph.dg.nodes[one][BUI_NODE_ST]) > 0:
                    for nodest in cfggraph.dg.nodes[one][BUI_NODE_ST]:
                        node_cont += "\n"
                        for each in nodest:
                            node_cont += str(each) + " "

                dotcfg.node(str(one), node_cont)

            for one in cfggraph.dg.edges:
                # edge_cont = ""
                # if len(cfggraph.dg.edges[one][BUI_GRAPH_ST]) > 0:
                #     edge_cont = cfggraph.dg.edges[one][BUI_GRAPH_ST]
                # dotcfg.edge(str(one[0]), str(one[1]), str(edge_cont))
                dotcfg.edge(str(one[0]), str(one[1]), "")

            cfgpath = dotcfg.render(directory=filepath_graph, filename=VIS_CFG_NAME, format='png')

            # print(path)
            # Show graph
            cg = Image.open(cgpath)
            # round() function, rounding five into two, that is, 4 rounding 6 into 5 to make even.
            plt.figure(num='CG', figsize=(round(cg.size[0]/VIS_DPI, 1), round(cg.size[1]/VIS_DPI,1)),)
            # plt.title('CG')
            plt.imshow(cg)  # show picture
            plt.axis('off')  # not show axis
            plt.subplots_adjust(left=0.0, right=1.0, top=1.0, bottom=0.0)
            plt.show()
            plt.draw()
            plt.pause(0.01)

            cfg = Image.open(cfgpath)
            plt.figure(num='CFG', figsize=(round(cfg.size[0]/VIS_DPI, 1), round(cfg.size[1]/VIS_DPI, 1)),)
            # plt.title('CFG')
            plt.imshow(cfg)  # show picture
            plt.axis('off')  # not show axis
            plt.subplots_adjust(left=0.0, right=1.0, top=1.0, bottom=0.0)
            plt.show()
            plt.draw()
            plt.pause(0.01)


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
        print(e)
    # os.system("clear")
    # xnum = ">" * (int(time.time()) % 4)
    # runtime = time.strftime("%d:%H:%M:%S", time.localtime(time.time()-start_time))
    #
    # print("  {} {}".format(BTFUZZ, xnum))
    # print("+----------------------------------------------+------------------------------+")
    # print("| Runtime:  {}".format(runtime))
