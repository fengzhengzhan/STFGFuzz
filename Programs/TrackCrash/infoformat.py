import ast
import os

filename = "crashinfo/" + "info"
outfilename = "crashinfo/" + "rand" + "_format"

with open(filename, "r") as f:
    cont = f.read()

l = ast.literal_eval(cont)

with open(outfilename, "w") as f:
    for each in l:
        f.write(str(each))
        f.write("\n")

os.remove(filename)
