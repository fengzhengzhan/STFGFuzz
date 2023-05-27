
import os
import re
import time
import subprocess
import datetime
import signal


list_dirname = [
    # 'CVE-2016-4487', 'CVE-2016-4488', 'CVE-2016-4489', 'CVE-2016-4490', 'CVE-2016-4492', 'CVE-2016-4493',
    # 'CVE-2017-14938', 'CVE-2017-7210', 'CVE-2017-8392', 'CVE-2019-9070',
    # 'cplusdem1423', 'cplusdem2744', 'cplusdem4263',
    # 'dwarf22860', 'objcopy3762', 'objdump2112',


    # 'CVE-2016-9827', 'CVE-2016-9828', 'CVE-2019-7582', 'CVE-2021-4214',
    # 'CVE-2017-11731', 'CVE-2017-11732', 'CVE-2017-11734', 'CVE-2017-16883', 'CVE-2018-8807',
    # 'blocktypes145', 'parser1948', 'read441', 'read467',
    # 'decompile1193', 'decompile1238', 'decompile2369', 'decompile2869', 'decompile629', 'decompile654', 'main111', 'outputscript1440', 'read227', 'read232',


    'CVE-2015-5221', 'CVE-2017-9412',
    'CVE-2017-10686',
    # 'CVE-2018-19058',
    'CVE-2019-6455',
    'dumpxml271', 'egiflib771',
    'mjs13671', 'mjs13679', 'mjs9320', 'layer3904', 'preproc3868', 'preproc1227',
    'tiffcp784',
]

template = [
    # c++filt template
    {'filename': 'CVE-2016-4487', 'programname': 'c++filt', 'parameters': ' @@'},
    {'filename': 'CVE-2016-4488', 'programname': 'c++filt', 'parameters': ' @@'},
    {'filename': 'CVE-2016-4489', 'programname': 'c++flit', 'parameters': ' @@'},
    {'filename': 'CVE-2016-4490', 'programname': 'c++filt', 'parameters': ' @@'},
    {'filename': 'CVE-2016-4492', 'programname': 'c++filt', 'parameters': ' @@'},
    {'filename': 'CVE-2016-4493', 'programname': 'c++filt', 'parameters': ' @@'},
    {'filename': 'CVE-2017-14938', 'programname': 'objdump', 'parameters': ' -S @@'},
    {'filename': 'CVE-2017-7210', 'programname': 'objdump', 'parameters': ' -W @@'},
    {'filename': 'CVE-2017-8392', 'programname': 'objdump', 'parameters': ' -W @@'},
    {'filename': 'CVE-2019-9070', 'programname': 'objdump', 'parameters': ' -S @@'},
    {'filename': 'cplusdem1423', 'programname': 'c++filt', 'parameters': ' @@'},
    {'filename': 'cplusdem2744', 'programname': 'c++filt', 'parameters': ' @@'},
    {'filename': 'cplusdem4263', 'programname': 'c++filt', 'parameters': ' @@'},
    {'filename': 'dwarf22860', 'programname': 'objdump', 'parameters': ' -S @@'},
    {'filename': 'objcopy3762', 'programname': 'objcopy', 'parameters': ' --compress-debug-section @@'},
    {'filename': 'objdump2112', 'programname': 'objdump', 'parameters': ' -S @@'},


    # swftophp template
    {'filename': 'CVE-2016-9827', 'programname': 'listswf', 'parameters': ' @@'},
    {'filename': 'CVE-2016-9828', 'programname': 'listswf', 'parameters': ' @@'},
    {'filename': 'CVE-2019-7582', 'programname': 'listswf', 'parameters': ' @@'},
    {'filename': 'CVE-2021-4214', 'programname': 'listswf', 'parameters': ' @@'},
    {'filename': 'CVE-2017-11731', 'programname': 'swftophp', 'parameters': ' @@'},
    {'filename': 'CVE-2017-11732', 'programname': 'swftophp', 'parameters': ' @@'},
    {'filename': 'CVE-2017-11734', 'programname': 'swftophp', 'parameters': ' @@'},
    {'filename': 'CVE-2017-16883', 'programname': 'swftophp', 'parameters': ' @@'},
    {'filename': 'CVE-2018-8807', 'programname': 'swftophp', 'parameters': ' @@'},
    {'filename': 'blocktypes145', 'programname': 'listswf', 'parameters': ' @@'},
    {'filename': 'parser1948', 'programname': 'listswf', 'parameters': ' @@'},
    {'filename': 'read441', 'programname': 'listswf', 'parameters': ' @@'},
    {'filename': 'read467', 'programname': 'listswf', 'parameters': ' @@'},
    {'filename': 'decompile1193', 'programname': 'swftophp', 'parameters': ' @@'},
    {'filename': 'decompile1238', 'programname': 'swftophp', 'parameters': ' @@'},
    {'filename': 'decompile2369', 'programname': 'swftophp', 'parameters': ' @@'},
    {'filename': 'decompile2869', 'programname': 'swftophp', 'parameters': ' @@'},
    {'filename': 'decompile629', 'programname': 'swftophp', 'parameters': ' @@'},
    {'filename': 'decompile654', 'programname': 'swftophp', 'parameters': ' @@'},
    {'filename': 'main111', 'programname': 'swftophp', 'parameters': ' @@'},
    {'filename': 'outputscript1440', 'programname': 'swftophp', 'parameters': ' @@'},
    {'filename': 'read227', 'programname': 'swftophp', 'parameters': ' @@'},
    {'filename': 'read232', 'programname': 'swftophp', 'parameters': ' @@'},

    {'filename': 'CVE-2015-5221', 'programname': 'jasper', 'parameters': ' -f @@ -t mif -F /tmp/out -T jpg'},
    {'filename': 'CVE-2017-9412', 'programname': 'lame', 'parameters': ' @@ /dev/null'},
    {'filename': 'CVE-2017-10686', 'programname': 'nasm', 'parameters': ' -f bin @@ -o /dev/null'},
    {'filename': 'CVE-2019-6455', 'programname': 'rec2csv', 'parameters': ' @@'},
    {'filename': 'preproc3868', 'programname': 'nasm', 'parameters': ' -f bin @@ -o /dev/null'},
    {'filename': 'preproc1227', 'programname': 'nasm', 'parameters': ' -f bin @@ -o /dev/null'},
    {'filename': 'tiffcp784', 'programname': 'tiffcp', 'parameters': ' -i @@ /tmp/out'},

    # other
    {'filename': 'egiflib771', 'programname': 'gifsponge', 'parameters': ''},  # program in the util location.
    {'filename': 'CVE-2018-19058', 'programname': 'pdfdetch', 'parameters': ' --save 1 @@'},
    {'filename': 'dumpxml271', 'programname': 'flvmeta', 'parameters': ' @@'},
    {'filename': 'mjs13671', 'programname': 'mjs-bin', 'parameters': ' -f @@'},
    {'filename': 'mjs13679', 'programname': 'mjs-bin', 'parameters': ' -f @@'},
    {'filename': 'mjs9320', 'programname': 'mjs-bin', 'parameters': ' -f @@'},
    {'filename': 'layer3904', 'programname': 'mp3gain', 'parameters': ' @@'},  # no tar -zxvf, modify Makefile CC=gcc to CC=wllvm.

]

asan_map = {
    "CVE-2016-4487": "/home/fzz/Desktop/STFGFuzz/Programs/Experiment/first_experiment/CVE-2016-4490/code_Bin/CVE-2016-4490",
    "CVE-2016-4488": "/home/fzz/Desktop/STFGFuzz/Programs/Experiment/first_experiment/CVE-2016-4490/code_Bin/CVE-2016-4490",
    "CVE-2016-4489": "/home/fzz/Desktop/STFGFuzz/Programs/Experiment/first_experiment/CVE-2016-4490/code_Bin/CVE-2016-4490",
    "CVE-2016-4490": "/home/fzz/Desktop/STFGFuzz/Programs/Experiment/first_experiment/CVE-2016-4490/code_Bin/CVE-2016-4490",
    "CVE-2016-4492": "/home/fzz/Desktop/STFGFuzz/Programs/Experiment/first_experiment/CVE-2016-4490/code_Bin/CVE-2016-4490",
    "CVE-2016-4493": "/home/fzz/Desktop/STFGFuzz/Programs/Experiment/first_experiment/CVE-2016-4490/code_Bin/CVE-2016-4490",
    "CVE-2015-5221": "/home/fzz/Desktop/STFGFuzz/Programs/Experiment/first_experiment/jasper-CVE-2015-5221/code_Bin/jasper-CVE-2015-5221",
    "CVE-2017-9412": "/home/fzz/Desktop/STFGFuzz/Programs/lame/code_Bin/lame",
    "CVE-2016-9827": "/home/fzz/Desktop/STFGFuzz/Programs/ming47-CVE-2016-9827/code_Bin/ming47-CVE-2016-9827",
    "CVE-2016-9828": "/home/fzz/Desktop/STFGFuzz/Programs/ming47-CVE-2016-9827/code_Bin/ming47-CVE-2016-9827",
    "CVE-2019-7582": "/home/fzz/Desktop/STFGFuzz/Programs/ming48-CVE-2018-8807/code_Bin/ming48-CVE-2018-8807",
    "CVE-2021-4214": "/home/fzz/Desktop/STFGFuzz/Programs/ming47-CVE-2016-9831/code_Bin/ming47-CVE-2016-9831",
    "CVE-2017-10686": "/home/fzz/Desktop/STFGFuzz/Programs/Experiment/first_experiment/CVE-2017-10686/code_Bin/CVE-2017-10686",
    "CVE-2017-7210": "/home/fzz/Desktop/STFGFuzz/Programs/objdump-CVE-2017-8396/code_Bin/objdump-CVE-2017-8396",
    "CVE-2017-14938": "/home/fzz/Desktop/STFGFuzz/Programs/objdump228/code_Bin/objdump228",
    "CVE-2017-8392": "/home/fzz/Desktop/STFGFuzz/Programs/objdump-CVE-2017-8396/code_Bin/objdump-CVE-2017-8396",
    "CVE-2019-9070": "/home/fzz/Desktop/STFGFuzz/Programs/objdump5279478_asan/code_Bin/objdump5279478_asan",
    "CVE-2018-19058": "/home/fzz/Desktop/STFGFuzz/Programs/pdfdetach-CVE-2018-19059/code_Bin/pdfdetach-CVE-2018-19059",
    "CVE-2019-6455": "/home/fzz/Desktop/STFGFuzz/Programs/Experiment/first_experiment/CVE-2019-6455/code_Bin/CVE-2019-6455",
    "CVE-2017-11731": "/home/fzz/Desktop/STFGFuzz/Programs/ming48-CVE-2018-11225/code_Bin/ming48-CVE-2018-11225",
    "CVE-2017-11732": "/home/fzz/Desktop/STFGFuzz/Programs/ming48-CVE-2018-11225/code_Bin/ming48-CVE-2018-11225",
    "CVE-2017-11734": "/home/fzz/Desktop/STFGFuzz/Programs/ming48-CVE-2018-11225/code_Bin/ming48-CVE-2018-11225",
    "CVE-2017-16883": "/home/fzz/Desktop/STFGFuzz/Programs/ming48-CVE-2019-9114/code_Bin/ming48-CVE-2019-9114",
    "CVE-2018-8807": "/home/fzz/Desktop/STFGFuzz/Programs/Experiment/first_experiment/swftophp/code_Bin/swftophp",
    "cplusdem1423": "/home/fzz/Desktop/STFGFuzz/Programs/cxxflit-CVE-2016-6131/code_Bin/cxxflit-CVE-2016-6131",
    "cplusdem2744": "/home/fzz/Desktop/STFGFuzz/Programs/Experiment/first_experiment/CVE-2016-4490/code_Bin/CVE-2016-4490",
    "cplusdem4263": "/home/fzz/Desktop/STFGFuzz/Programs/cxxflit-CVE-2016-6131/code_Bin/cxxflit-CVE-2016-6131",
    "dumpxml271": "/home/fzz/Desktop/STFGFuzz/Programs/flvmeta/code_Bin/flvmeta",
    "egiflib771": "/home/fzz/Desktop/STFGFuzz/Programs/Experiment/first_experiment/giflib-bugs-74/code_Bin/giflib-bugs-74",
    "parser1948": "/home/fzz/Desktop/STFGFuzz/Programs/ming47-CVE-2016-9829/code_Bin/ming47-CVE-2016-9829",
    "read441": "/home/fzz/Desktop/STFGFuzz/Programs/ming47-CVE-2016-9831/code_Bin/ming47-CVE-2016-9831",
    "read467": "/home/fzz/Desktop/STFGFuzz/Programs/ming47-CVE-2016-9827/code_Bin/ming47-CVE-2016-9827",
    "blocktypes145": "/home/fzz/Desktop/STFGFuzz/Programs/ming48-CVE-2018-11225/code_Bin/ming48-CVE-2018-11225",
    "mjs9320": "/home/fzz/Desktop/STFGFuzz/Programs/Experiment/first_experiment/mjs-issues-57/code_Bin/mjs-issues-57",
    "mjs13671": "/home/fzz/Desktop/STFGFuzz/Programs/Experiment/first_experiment/mjs-issues-78/code_Bin/mjs-issues-78",
    "mjs13679": "/home/fzz/Desktop/STFGFuzz/Programs/Experiment/first_experiment/mjs-issues-78/code_Bin/mjs-issues-78",
    "layer3904": "/home/fzz/Desktop/STFGFuzz/Programs/mp3gain/code_Bin/mp3gain",
    "preproc1227": "/home/fzz/Desktop/STFGFuzz/Programs/Experiment/first_experiment/CVE-2017-10686/code_bin/CVE-2017-10686",
    "preproc3868": "/home/fzz/Desktop/STFGFuzz/Programs/Experiment/first_experiment/CVE-2017-10686/code_bin/CVE-2017-10686",
    "dwarf22860": "/home/fzz/Desktop/STFGFuzz/Programs/objdump228/code_Bin/objdump228",
    "objdump2112": "/home/fzz/Desktop/STFGFuzz/Programs/objdump228_asan/code_Bin/objdump228_asan",
    "objcopy3762": "/home/fzz/Desktop/STFGFuzz/Programs/objcopy-CVE-2017-8395/code_Bin/objcopy-CVE-2017-8395",
    "decompile629": "/home/fzz/Desktop/STFGFuzz/Programs/ming48-CVE-2018-11225/code_Bin/ming48-CVE-2018-11225",
    "decompile654": "/home/fzz/Desktop/STFGFuzz/Programs/Experiment/first_experiment/swftophp/code_Bin/swftophp",
    "decompile1193": "/home/fzz/Desktop/STFGFuzz/Programs/ming48-CVE-2019-12982code_Bin/ming48-CVE-2019-12982",
    "decompile1238": "/home/fzz/Desktop/STFGFuzz/Programs/ming48-CVE-2019-9114/code_Bin/ming48-CVE-2019-9114",
    "decompile2369": "/home/fzz/Desktop/STFGFuzz/Programs/ming48-CVE-2018-11226/code_Bin/ming48-CVE-2018-11226",
    "decompile2869": "/home/fzz/Desktop/STFGFuzz/Programs/ming48-CVE-2018-11095/code_Bin/ming48-CVE-2018-11095",
    "main111": "/home/fzz/Desktop/STFGFuzz/Programs/ming48-CVE-2018-11225/code_Bin/ming48-CVE-2018-11225",
    "outputscript1440": "/home/fzz/Desktop/STFGFuzz/Programs/ming48-CVE-2020-6628/code_Bin/ming48-CVE-2020-6628",
    "read227": "/home/fzz/Desktop/STFGFuzz/Programs/ming48-CVE-2018-11225/code_Bin/ming48-CVE-2018-11225",
    "read232": "/home/fzz/Desktop/STFGFuzz/Programs/ming48-CVE-2018-11095/code_Bin/ming48-CVE-2018-11095",
    "tiffcp784": "/home/fzz/Desktop/STFGFuzz/Programs/Experiment/first_experiment/tiffcp/code_Bin/tiffcp",
}


def compareCrash(stderr, dir_patchloc):
    # print(stderr, dir_patchloc)
    errlist = []
    for err_i in str(stderr).split("\\n"):
        re_str = r"\#(\d*).*/(.*?):(\d*?):"
        re_crash = re.findall(re_str, str(err_i))
        # print(str(err_i))
        # print(re_crash)
        if len(re_crash) > 0:
            errlist.append(re_crash)

    patchlist = []
    with open(dir_patchloc, "r") as f:
        cont = f.readlines()
    # print(cont)
    for cont_i in cont:
        re_str = r"\#(\d*).*/(.*?):(\d*?):"
        re_crash = re.findall(re_str, cont_i)
        # print(cont_i)
        # print(re_crash)
        if len(re_crash) > 0:
            patchlist.append(re_crash)

    if errlist == patchlist:
        return "yes"

    return ""

def createFolder():
    lavalist = [292, 357, 660, 1199, 2285, 2543, 3089, 3377, 4049, 4383, 4961, 7002, 7700, 9763, 13796, 14324, 16689, 17222]
    for lavaid in lavalist:
        path = "dataset/lava1_dataset/angora_lava1_"+str(lavaid)
        print(path)
        folder = os.path.exists(path)

        if not folder:
            os.makedirs(path)
            # print(path)

def CVE2016():
    program_name = "CVE2016"
    dir = "dataset/cve2016/aflgo/"
    dir_program = dir + program_name
    dir_datain = dir + program_name + "_dataset/in/in"
    dir_dataout = dir + program_name + "_dataset/out/crashes"
    dir_csv = dir + program_name + ".csv"

    start_time = getFileCreateTime(dir_datain)
    print(start_time)

    # Get crash list
    crashes = os.listdir(dir_dataout)
    crashes.sort()
    # print(crashes)
    for each in crashes:
        each_crash = dir_dataout + "/" + each
        print(each_crash)
        # print(getFileCreateTime(each_crash))
        create_time = getFileCreateTime(each_crash)
        duration_time = create_time - start_time
        # print("./" + dir_program + " @" + each_crash)
        try:
            stdout, stderr = runTimeLimit("./" + dir_program + " @" + each_crash)
            # re_flag = re.search(r'AddressSanitizer', str(stderr))
            # if re_flag != None:
            #     saveToCSV(program_name, each, create_time, duration_time, stderr, stdout)
            saveToCSV(dir_csv, program_name, each, create_time, duration_time, stderr, stdout, "None Compare")
        except Exception as e:
            # raise Exception(e)
            print("Error " + str(e))
        #
        # print()

def LAVA1():
    # lavalist = [292, 357, 660, 1199, 2285, 2543, 3089, 3377, 4049, 4383, 4961, 7002, 7700, 9763, 13796, 14324, 16689, 17222]
    lavalist = [14324]
    for lavaid in lavalist:
        lavaid = str(lavaid)
        program_name = "lava"+lavaid
        dir = "dataset/lava1_dataset/angora_lava1_"+lavaid+"/"
        dir_program = "../../"+program_name+"/code_Bin/"+program_name
        dir_patchloc = "../../" + program_name + "/data_patchloc/crash0.sanitize"
        dir_datain = dir + "seeds"
        dir_dataout = dir + "output/crashes"
        dir_csv = dir + program_name + ".csv"

        start_time = getFileCreateTime(dir_datain)
        print(start_time)

        # Get crash list
        crashes = os.listdir(dir_dataout)
        crashes.sort()
        # print(crashes)
        for each in crashes:
            each_crash = dir_dataout + "/" + each
            print(each_crash)
            # print(getFileCreateTime(each_crash))
            create_time = getFileCreateTime(each_crash)
            duration_time = create_time - start_time
            print(create_time, duration_time)
            # print("./" + dir_program + " @" + each_crash)
            try:
                cmd = "./" + dir_program + " " + each_crash
                # print(cmd)
                stdout, stderr = runTimeLimit(cmd)
                # print(stdout, stderr)
                # re_flag = re.search(r'AddressSanitizer', str(stderr))
                # if re_flag != None:
                #     saveToCSV(program_name, each, create_time, duration_time, stderr, stdout)
                cmpflag = compareCrash(stderr, dir_patchloc)
                saveToCSV(dir_csv, program_name, each, create_time, duration_time, stderr, stdout, cmpflag)
            except Exception as e:
                # raise Exception(e)
                print("Error " + str(e))
            #
            # print()


def gainAFLGoCsv(program_name, sanitize_location, prev_par, next_par):
    dir = "dataset/aflgo/"
    dir_program = sanitize_location
    dir_datain = dir + program_name + "/in"
    dir_dataout = dir + program_name + "/out/crashes"
    dir_csv = dir + program_name + ".csv"

    start_time = getFileCreateTime(dir_datain)
    # start_time = datetime.datetime.strptime("2022-12-04 17:41:27", '%Y-%m-%d %H:%M:%S')
    # print(start_time)

    # Get crash list
    crashes = os.listdir(dir_dataout)
    crashes.sort()
    # print(crashes)
    for each in crashes:
        each_crash = dir_dataout + "/" + each
        # print(each_crash)
        # print(getFileCreateTime(each_crash))
        create_time = getFileCreateTime(each_crash)
        duration_time = create_time - start_time
        # print("./" + dir_program + " @" + each_crash)
        try:
            # swftophp
            # command = dir_program + " " + each_crash
            # jasper
            # command = dir_program + " -f "+each_crash +" -t mif -F /tmp/out -T jpg"
            command = dir_program + " " + prev_par + " " + each_crash + " " + next_par
            print(command)
            stdout, stderr = runTimeLimit(command)
            # re_flag = re.search(r'AddressSanitizer', str(stderr))
            # if re_flag != None:
            #     saveToCSV(program_name, each, create_time, duration_time, stderr, stdout)
            saveToCSV(dir_csv, program_name, each, create_time, duration_time, stderr, stdout, "None Compare")
        except Exception as e:
            # raise Exception(e)
            print("Error " + str(e))
        #
        # print()

def gainAngoraCsv(program_name, sanitize_location, prev_par, next_par):
    dir = "dataset/angora/"
    dir_program = sanitize_location
    dir_datain = dir + program_name + "/seeds"
    dir_dataout = dir + program_name + "/output/crashes"
    dir_csv = dir + program_name + ".csv"

    start_time = getFileCreateTime(dir_datain)
    # start_time = datetime.datetime.strptime("2022-12-04 17:41:27", '%Y-%m-%d %H:%M:%S')
    print(start_time)

    # Get crash list
    crashes = os.listdir(dir_dataout)
    crashes.sort()
    # print(crashes)
    for each in crashes:
        each_crash = dir_dataout + "/" + each
        print(each_crash)
        # print(getFileCreateTime(each_crash))
        create_time = getFileCreateTime(each_crash)
        duration_time = create_time - start_time
        # print("./" + dir_program + " @" + each_crash)
        try:
            # swftophp
            command = dir_program + " " + prev_par + " " + each_crash + " " + next_par
            print(command)
            # command = dir_program + " " + each_crash
            # print("command:{}".format(command))
            stdout, stderr = runTimeLimit(command)
            # re_flag = re.search(r'AddressSanitizer', str(stderr))
            # if re_flag != None:
            #     saveToCSV(program_name, each, create_time, duration_time, stderr, stdout)
            saveToCSV(dir_csv, program_name, each, create_time, duration_time, stderr, stdout, "None Compare")
        except Exception as e:
            # raise Exception(e)
            print("Error " + str(e))
        #
        # print()

def main():
    # CVE2016()
    # LAVA1()
    # createFolder()


    # gainAFLGoCsv("swftophp048", "/home/fzz/Desktop/STFGFuzz/Programs/swftophp/code_Bin/swftophp")
    # gainAFLGoCsv("swftophp2864", "/home/fzz/Desktop/STFGFuzz/Programs/swftophp/code_Bin/swftophp")
    # gainAFLGoCsv("swftophp1042864", "/home/fzz/Desktop/STFGFuzz/Programs/swftophp/code_Bin/swftophp")
    # gainAFLGoCsv("swftophpother", "/home/fzz/Desktop/STFGFuzz/Programs/swftophp/code_Bin/swftophp")
    # gainAFLGoCsv("lava229", "/home/fzz/Desktop/STFGFuzz/Programs/lava292/code_Bin/lava229")
    # gainAFLGoCsv("listswf", "/home/fzz/Desktop/STFGFuzz/Programs/listswf/code_Bin/listswf")
    # gainAFLGoCsv("listswf1226", "/home/fzz/Desktop/STFGFuzz/Programs/listswf/code_Bin/listswf")
    # gainAFLGoCsv("jasper-CVE-2015-5221", "/home/fzz/Desktop/STFGFuzz/Programs/jasper-CVE-2015-5221/code_Bin/jasper-CVE-2015-5221")
    # gainAFLGoCsv("gifsponge", "/home/fzz/Desktop/STFGFuzz/Programs/giflib-bugs-74/code_Bin/giflib-bugs-74", "-f", "")
    gainAFLGoCsv("mjs9320", "/home/fzz/Desktop/STFGFuzz/Programs/mjs-issues-57/code_Bin/mjs-issues-57", "-f", "")
    gainAFLGoCsv("mjs13671", "/home/fzz/Desktop/STFGFuzz/Programs/mjs-issues-78/code_Bin/mjs-issues-78", "-f", "")
    # gainAFLGoCsv("gifsponge", "/home/fzz/Desktop/STFGFuzz/Programs/giflib-bugs-74/code_Bin/giflib-bugs-74", "-f", "")
    gainAFLGoCsv("mjs57", "/home/fzz/Desktop/STFGFuzz/Programs/mjs-issues-57/code_Bin/mjs-issues-57", "-f", "")
    gainAFLGoCsv("mjs78", "/home/fzz/Desktop/STFGFuzz/Programs/mjs-issues-78/code_Bin/mjs-issues-78", "-f", "")
    # gainAFLGoCsv("rec2csv", "//home/fzz/Desktop/STFGFuzz/Programs/CVE-2019-6455/code_Bin/CVE-2019-6455", "", "")
    # gainAFLGoCsv("tiffcp", "/home/fzz/Desktop/STFGFuzz/Programs/tiffcp/code_Bin/tiffcp", "-i", "/tmp/tiffcp_tmp")



    # gainAngoraCsv("swftophp048", "/home/fzz/Desktop/STFGFuzz/Programs/swftophp/code_Bin/swftophp")
    # gainAngoraCsv("listswf048", "/home/fzz/Desktop/STFGFuzz/Programs/listswf/code_Bin/listswf")
    # gainAngoraCsv("angora_listswf", "/home/fzz/Desktop/STFGFuzz/Programs/listswf/code_Bin/listswf")
    # gainAngoraCsv("listswf1226", "/home/fzz/Desktop/STFGFuzz/Programs/listswf/code_Bin/listswf")
    # gainAngoraCsv("rec2csv", "/home/fzz/Desktop/STFGFuzz/Programs/CVE-2019-6455/code_Bin/CVE-2019-6455", "", "")
    # gainAngoraCsv("jasper", "/home/fzz/Desktop/STFGFuzz/Programs/jasper-CVE-2015-5221/code_Bin/jasper-CVE-2015-5221", "-f", "-t mif -F /tmp/out -T jpg")
    # gainAngoraCsv("gifsponge", "/home/fzz/Desktop/STFGFuzz/Programs/giflib-bugs-74/code_Bin/giflib-bugs-74", "<", "")

    # createCVEFolder(cve_list)
    # cpSourceFiles()

    # createAFLGoFolder(aflgo_dataset_list)
    # createAFLGoFolder(uaf_dataset_list)




def runTimeLimit(cmd) -> (str, str):
    """
    run cmd to get information from executable files or other tools
    @param cmd:
    @return:
    """
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         shell=True, close_fds=True, start_new_session=True)

    # timeout kill child process
    try:
        stdout, stderr = p.communicate(timeout=120)
        # ret_code = p.poll()
    except subprocess.TimeoutExpired:
        p.kill()
        p.terminate()
        os.killpg(p.pid, signal.SIGTERM)
        stdout, stderr = b'', b'Error Timeout'
    except Exception as e:
        raise Exception("Error cmd: " + cmd)
    # retcode = 128 - p.returncode
    # print(retcode, stdout, stderr)
    return stdout, stderr

# Get time of start time and crash time list
def getFileCreateTime(file):
    # t = os.path.getctime(file)
    stdout, stderr = runTimeLimit("ls -l --full-time " + file)
    data_str = re.search(r'(\d+-\d+-\d+ \d+:\d+:\d+).\d+', str(stdout)).group(1)
    # print(data_str)
    t = datetime.datetime.strptime(data_str, '%Y-%m-%d %H:%M:%S')
    return t

def getFileCreateTimePlotdata(file):
    # t = os.path.getctime(file)

    with open(file, "r") as f:
        f.readline()
        timestamp = f.readline().split(",")[0]
        # print(timestamp)
    # print("hhh", timestamp)
    try:
        float(timestamp)
    except Exception:
        timestamp = 1682407543
    t = datetime.datetime.fromtimestamp(float(timestamp))
    # print(t)
    return t

def saveToCSV(dir_csv, program_name, id, create_time, duration_time, stderr, stdout, cmpflag):
    with open(dir_csv, "a+", encoding="utf-8") as cf:
        # GEN_CSV_HEADERS = "filename,time,duration,content,stdout,stderr\n"
        linestr = str(program_name) + "," \
                  + str(id).replace(',', 'comma') + "," \
                  + str(create_time) + "," \
                  + str(duration_time) + "," \
                  + str(stderr).replace(',', 'comma') + "," \
                  + str(stdout).replace(',', 'comma') + "," \
                  + str(cmpflag).replace(',', 'comma') + ",,,\n"
        cf.write(linestr)



class GenerateCrashReport:
    def __init__(self):
        pass

    def extractTar(self, path, rootpath):
        list_crashes = []
        for root, dirs, files in os.walk(path):
            # print(root, dirs, files)
            # print(root)
            for file in files:
                file_path = os.path.join(root, file)
                # print(file_path[-4:])
                if file_path[-4:] == ".tar":
                    # print(file_path)
                    if not os.path.isdir(file_path[:-4]):
                        cmd = "tar -xf {} --transform 's/{}/{}/' -C {}".format(file_path, rootpath, file[:-4], root)
                        print(cmd)
                        runTimeLimit(cmd)
                    list_crashes.append("{}/{}".format(os.getcwd(), file_path[:-4]))

        print(list_crashes)
        return list_crashes

    def generateCsv(self, fuzzer, path, crash_location, rootpath):
        list_crashes = self.extractTar(path, rootpath)
        print(list_crashes)
        temp_crash_location = crash_location
        # raise Exception()

        for each in list_crashes:
            # print(each)
            program = (each.split("/")[-1]).split("_")[1]
            if fuzzer == "aflgo":
                crash_location = temp_crash_location + program + "/obj-dist/out/crashes"
            dir_csv = "{}/{}.csv".format(each, program)
            if os.path.exists(dir_csv):
                os.remove(dir_csv)
                # continue
            # print(program)
            if program in asan_map:
                asan_program = asan_map[program]
                print(asan_program)
            else:
                continue

            # file_time = "{}/{}/plot_data".format(each, crash_location[:-8])
            # Angora
            file_time = "{}/{}".format(each, crash_location[:-8])
            # if os.path.getsize(file_time) == 0:
            #     start_time = getFileCreateTime(file_time)
            #     # start_time = getFileCreateTimePlotdata(file_time)
            #     # print(start_time)
            # else:
            #     raise Exception("Error start time.")
            # start_time = getFileCreateTimePlotdata(file_time)
            # Angora
            start_time = getFileCreateTime(file_time[:-3])
            # print(start_time, file_time[:-3])
            # raise Exception()
            # print(file_time)
            # raise Exception()

            # Get crash list
            crashes = os.listdir("{}/{}".format(each, crash_location))
            crashes.sort()
            print(crashes)
            for crash in crashes:
                each_crash = "{}/{}/{}".format(each, crash_location, crash)
                # print(each_crash)
                # print(getFileCreateTime(each_crash))
                create_time = getFileCreateTime(each_crash)
                duration_time = create_time - start_time
                # print("./" + dir_program + " @" + each_crash)

                # swftophp
                # command = dir_program + " " + each_crash
                # jasper
                # command = dir_program + " -f "+each_crash +" -t mif -F /tmp/out -T jpg"
                try:
                    for each_template in template:
                        if program == each_template['filename']:
                            parameters = each_template['parameters']
                            programname = each_template['programname']

                    if programname == "c++filt":
                        command = "{} @{}".format(asan_program, parameters.replace("@@", each_crash))
                    else:
                        command = "{} {}".format(asan_program, parameters.replace("@@", each_crash))
                    print(command)
                    stdout, stderr = runTimeLimit(command)
                    saveToCSV(dir_csv, programname, crash, create_time, duration_time, stderr, stdout, "None Compare")
                except Exception as e:
                    # raise Exception(e)
                    print("Error " + str(e))


    def showCsv(self):
        path = "dataset/all_crashes"

        for root, dirs, files in os.walk(path):
            # print(root, dirs, files)
            for file in files:
                file_path = os.path.join(root, file)
                # print(file_path[-4:])
                if file_path[-4:] == ".tar":
                    print()
                    print(file_path)
                    program = (file[:-4].split("/")[-1]).split("_")[1]
                    # print(program)
                    dir_csv = "{}/{}.csv".format(file_path[:-4], program)
                    # print(dir_csv)
                    if os.path.exists(dir_csv):
                        print("{} {}".format(os.path.getsize(dir_csv), dir_csv))
                        print()





if __name__ == '__main__':
    # GenerateCrashReport().generateCsv("dataset/all_crashes/windranger2_c++filt", "SVF-tools/example/windranger_fuzz/out/crashes")
    # GenerateCrashReport().generateCsv("dataset/all_crashes/winranger1_other", "SVF-tools/example/windranger_fuzz/out/crashes")
    # GenerateCrashReport().generateCsv("dataset/all_crashes/beacon1_swftophp", "Test/out/crashes")
    # GenerateCrashReport().generateCsv("dataset/all_crashes/beacon1_other", "Test/out/crashes")
    # GenerateCrashReport().generateCsv("dataset/all_crashes/beacon1_c++filt", "Test/out/crashes")
    # GenerateCrashReport().generateCsv("aflgo", "dataset/all_crashes/aflgo1_all", "aflgo/scripts/fuzz/", "root")
    GenerateCrashReport().generateCsv("angora", "dataset/all_crashes/angora1_all", "datav5/Angora-1.2.2/experiment/out/crashes", "root")
    # GenerateCrashReport().showCsv()
    # GenerateCrashReport().extractTar("dataset/all_crashes/winranger1_other")