import os

# initname = "crashone/lava13796init1"
# crashname = "crashone/lava13796crash"
initname = "crashone/info_formatELF"
crashname = "crashone/info_formatnoELF"


initdiff = "crashone/initdiff"
crashdiff = "crashone/crashdiff"

with open(initname, "r") as f:
    initcont = f.readlines()

with open(crashname, "r") as f:
    crashcont = f.readlines()

print(len(initcont), len(crashcont))

cf = 0

if os.path.exists(initdiff):
    os.remove(initdiff)
if os.path.exists(crashdiff):
    os.remove(crashdiff)


for idx in range(0, min(len(initcont), len(crashcont))):
    if initcont[idx] != crashcont[idx]:
        with open(initdiff, "a+") as f:
            f.write(initcont[idx])
        with open(crashdiff, "a+") as f:
            f.write(crashcont[idx])
        print(idx, initcont[idx], crashcont[idx])
        # cf += 1
    # if cf > 10:
    #     break