import datetime
import queue


class Test:
    def __init__(self, s, b):
        self.s = s
        self.b = b


for i, x in enumerate(range(10, 15)):
    print(i, x)

x = [0, 1, 2]
print(x[0])
print(x[1:3])


def getMutfilename(label: str):
    return str(datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')) + "_" + str(label) + ".seed"

for i in range(0, 100):
    print(getMutfilename(i))

