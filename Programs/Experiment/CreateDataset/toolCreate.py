import os

# lava_list = [4961, 7002, 13796, 292, 660, 3089, 4383, 7700, 14324,
#              2543, 4049, 1199, 2285, 9763, 16689, 17222, 357, 3377]
lava_list = [292, 357, 660, 1199, 2285, 2543, 3089, 3377, 4049,
             4383, 4961, 7002, 7700, 9763, 13796, 14324, 16689, 17222]
lava_branch = ['292_R_0x12345678-0x12545678', '357_R_0x12345678-0x12345678',
               '660_R_0x12345678-0x12545678', '1199_R_0x12345678-0x123456f8',
               '2285_R_0x12345678-0x123456f8', '2543_R_0x12345678-0x12349678',
               '3089_R_0x12345678-0x12345678', '3377_R_0x12345678-0x12345678',
               '4049_R_0x12345678-0x12349678', '4383_R_0x12345678-0x12545678',
               '4961_R_0x12345678-0x22345678', '7002_R_0x12345678-0x22345678',
               '7700_R_0x12345678-0x12545678', '9763_R_0x12345678-0x123456f8',
               '13796_R_0x12345678-0x22345678', '14324_R_0x12345678-0x12545678',
               '16689_R_0x12345678-0x123456f8', '17222_R_0x12345678-0x123456f8']


def createDir():
    # Adjust path of location.
    print(os.getcwd())
    os.chdir('/home/fzz/Desktop/STFGFuzz/Programs')
    print(os.getcwd())
    for one in lava_list:
        dirname = "lava" + str(one)
        # if not os.path.exists(dirname):
        #     os.makedirs(dirname)
        #
        # sourcename = "lava"+str(one)+"/"+"code_sources"
        # if not os.path.exists(sourcename):
        #     os.makedirs(sourcename)
        #
        # patchname = "lava" + str(one) + "/data_patchloc/"
        # if not os.path.exists(patchname):
        #     os.makedirs(patchname)

        # crashname = "lava" + str(one) + "/seeds_crash/"
        # if not os.path.exists(crashname):
        #     os.makedirs(crashname)
        #
        # initname = "lava" + str(one) + "/seeds_init/"
        # if not os.path.exists(initname):
        #     os.makedirs(initname)

        # patchfile = "lava" + str(one) + "/data_patchloc/" + "crash0.sanitizer"
        # with open(patchfile, "a+") as f:
        #     f.write("\n")



def createBC():
    # createBC.sh
    pass


def cpFiles():
    for idx in range(0, len(lava_branch)):
        lavadirname = "file-5.22." + lava_branch[idx]
        dirname = "lava" + str(lava_list[idx])

        # cmd = "cp /home/fzz/Desktop/STFGFuzz/dataset/datav5/lava_corpus/LAVA-1/"+lavadirname+"/lava-install/bin/file.bc /home/fzz/Desktop/STFGFuzz/Programs/"+dirname+"/code_sources/"+dirname+".bc"
        # print(cmd)
        # os.system(cmd)



        cmd = "cp /home/fzz/Desktop/STFGFuzz/dataset/datav5/lava_corpus/LAVA-1/" + lavadirname + "/CRASH_INPUT /home/fzz/Desktop/STFGFuzz/Programs/" + dirname + "/seeds_crash/crash.seed"
        print(cmd)
        os.system(cmd)

        cmd = "cp /home/fzz/Desktop/STFGFuzz/rand.seed /home/fzz/Desktop/STFGFuzz/Programs/" + dirname + "/seeds_init/rand.seed"
        print(cmd)
        os.system(cmd)

def buildFiles():
    print(os.getcwd())
    os.chdir('/home/fzz/Desktop/STFGFuzz/Programs')
    print(os.getcwd())
    for idx in range(0, len(lava_branch)):
        dirname = "lava" + str(lava_list[idx])
        buildcmd = "./build.sh -n "+dirname+" clang"
        print(buildcmd)
        os.system(buildcmd)


def printFuzz():
    for one in lava_list:
        dirname = "lava" + str(one)
        # print(dirname + "/code_Bin/" + dirname + " " + dirname + "/seeds_crash/crash.seed")
        print("python3.7 STFGFuzzer.py -n " + dirname + " -t sanitizer -- Programs/" + dirname + "/code_Bin/" + dirname + " @@")
        print()



if __name__ == '__main__':
    # 0
    # ./createBC.sh

    # 1
    # createDir()
    # 2
    # cpFiles()
    # 3 root
    buildFiles()
    # 4
    # printFuzz()
