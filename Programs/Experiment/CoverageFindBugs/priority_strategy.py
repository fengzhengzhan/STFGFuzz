import matplotlib.pyplot as plt
import numpy as np

class Display():

    def drawBarChart(self, data):
        pass

    def drawBarhChart(self, data):
        labels = []
        p1 = []
        p2 = []
        p3 = []
        p4 = []
        for each in data:
            # trans
            trans = []
            for one in each[3:]:
                trans.append(int(one[:-1]))
            max_trans = max(trans)
            for idx, one in enumerate(trans):
                trans[idx] = one / max_trans


            #
            labels.append(each[1]+"\n"+each[2])
            p1.append(trans[0])
            p2.append(trans[1])
            p3.append(trans[2])
            p4.append(trans[3])

        # print(labels, p1, p2, p3, p4)
        #
        data = []
        for idx in range(0, len(labels)):
            data.append([p1[idx], p2[idx], p3[idx], p4[idx]])
        # print(data, len(labels))

        dim = len(data[0])
        w = 0.6
        dimw = w / dim

        # draw picture
        # fig, ax = plt.subplots(figsize=(6, 9))
        fig, ax = plt.subplots(figsize=(12, 12))
        plt.xlim((0.001, 3.0))
        x = np.arange(len(data))
        # print(x)

        # for i in range(len(data[0])):
        y = [d[0] for d in data]
        b = ax.barh(x + 1.5 * dimw, y, dimw, left=0.001, label="FIFO")

        y = [d[1] for d in data]
        b = ax.barh(x + 0.5 * dimw, y, dimw, left=0.001, label="D")

        y = [d[2] for d in data]
        b = ax.barh(x - 0.5 * dimw, y, dimw, left=0.001, label="D+C")

        y = [d[3] for d in data]
        b = ax.barh(x - 1.5 * dimw, y, dimw, left=0.001, label=r"$D+\frac{1}{C}$")

        ax.set_yticks(x + dimw / 2)
        ax.set_yticklabels(map(str, labels))
        ax.set_xscale('log')

        ax.set_xlabel('Normalized time')
        ax.legend(loc=1)

        # ax.set_title('matplotlib.axes.Axes.barh Example')

        plt.savefig('./priority_time_compare.png', dpi=300)
        # plt.show()


if __name__ == "__main__":
    # cve, program_name, location, no, distance, d+c, d+1/c  (s)

    priority_time_data = [
        # ["CVE-2017-10686", "nasm", ""],
        ["lava292", "file", "cdf.c:316", "7s", "6s", "6s", "6s"],
        ["CVE-2019-6455", "rec2csv", "rec-comment.c:49", "4s", "5s", "4s", "4s"],
        ["CVE-2017-7210", "objdump", "libbfd.c:184", "60s", "47s", "49s", "44s"],
        ["", "mjs-bin", "mjs.c:9320", "16s", "14s", "14s", "14s"],
        # ["", "listswf", "", "", "", ""],
        # ["", "nasm", "", "", "", ""],
        ["", "swftophp", "main.c:111", "7s", "7s", "7s", "7s"],
        ["", "swftophp", "read.c:227", "348s", "340s", "345s", "348s"],
        ["", "swftophp", "decompile.c:868", "2993s", "2979s", "2988s", "2992s"],
        ["", "swftophp", "decompile.c:629", "86400s", "86400s", "86400s", "31549s"],
        ["", "swftophp", "decompile.c:2369", "86400s", "86400s", "86400s", "31577s"],
        ["", "swftophp", "outputscript.c:1429", "86400s", "86400s", "86400s", "31754s"],
        ["", "swftophp", "decompile.c:104", "86400s", "86400s", "86400s", "76982s"],
        ["", "c++flit", "cplus-dem.c:4319", "1596s", "86400s", "870s", "5277s"],
    ]

    # 1. no FIFO
    # priority_value = 0
    # 2. distance
    # priority_value = distance
    # 3. distance + coverage
    # priority_value = int(distance * bit_dis + (coverage) % cover_multiple * bit_cover)
    # 4. distance + 1/coverage
    # priority_value = int(distance * bit_dis + (1 / (coverage + 1)) * cover_multiple * bit_cover)

    # Display().drawBarChart(priority_time_data)
    Display().drawBarhChart(priority_time_data)