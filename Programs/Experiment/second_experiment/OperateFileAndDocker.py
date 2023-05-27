import os
import docker
from jinja2 import Environment, FileSystemLoader

list_dirname = [
    ###### 'CVE-2016-4487', 'CVE-2016-4488', 'CVE-2016-4489', 'CVE-2016-4490', 'CVE-2016-4492', 'CVE-2016-4493',
    ###### 'CVE-2017-7210',
    'CVE-2017-14938', 'CVE-2017-8392', 'CVE-2019-9070',
    'cplusdem1423', 'cplusdem2744', 'cplusdem4263',
    'dwarf22860', 'objcopy3762', 'objdump2112',

    'CVE-2016-9827', 'CVE-2016-9828',
    ###### 'CVE-2019-7582', 'CVE-2021-4214',
    ###### 'CVE-2017-11731', 'CVE-2017-11732', 'CVE-2017-11734', 'CVE-2017-16883', 'CVE-2018-8807',
    ###### 'blocktypes145', 'parser1948', 'read441', 'read467',
    ###### 'decompile1193', 'decompile1238', 'decompile2369',
    'decompile2869',
    ###### 'decompile629', 'decompile654', 'main111', 'outputscript1440', 'read227',
    'read232',

    ###### 'CVE-2015-5221',
    # 'CVE-2017-9412',
    ###### 'CVE-2017-10686',
    # 'CVE-2018-19058',
    ###### 'CVE-2019-6455',
    ###### 'dumpxml271', 'egiflib771',
    ###### 'mjs13671', 'mjs13679', 'mjs9320',
    # 'layer3904',
    ###### 'preproc3868', 'preproc1227',
    ###### 'tiffcp784',
]

template = [
    # c++filt template
    # {'filename': 'CVE-2016-4487', 'programname': 'c++filt', 'parameters': ' @@'},
    # {'filename': 'CVE-2016-4488', 'programname': 'c++filt', 'parameters': ' @@'},
    # {'filename': 'CVE-2016-4489', 'programname': 'c++flit', 'parameters': ' @@'},
    # {'filename': 'CVE-2016-4490', 'programname': 'c++filt', 'parameters': ' @@'},
    # {'filename': 'CVE-2016-4492', 'programname': 'c++filt', 'parameters': ' @@'},
    # {'filename': 'CVE-2016-4493', 'programname': 'c++filt', 'parameters': ' @@'},
    # {'filename': 'CVE-2017-7210', 'programname': 'objdump', 'parameters': ' -W @@'},
    # {'filename': 'CVE-2017-14938', 'programname': 'objdump', 'parameters': ' -S @@'},
    # {'filename': 'CVE-2017-8392', 'programname': 'objdump', 'parameters': ' -W @@'},
    # {'filename': 'CVE-2019-9070', 'programname': 'objdump', 'parameters': ' -S @@'},
    # {'filename': 'cplusdem1423', 'programname': 'c++filt', 'parameters': ' @@'},
    # {'filename': 'cplusdem2744', 'programname': 'c++filt', 'parameters': ' @@'},
    # {'filename': 'cplusdem4263', 'programname': 'c++filt', 'parameters': ' @@'},
    # {'filename': 'dwarf22860', 'programname': 'objdump', 'parameters': ' -S @@'},
    # {'filename': 'objcopy3762', 'programname': 'objcopy', 'parameters': ' --compress-debug-section @@'},
    # {'filename': 'objdump2112', 'programname': 'objdump', 'parameters': ' -S @@'},

    # {'filename': 'CVE-2016-4487', 'programname': 'c++filt', 'parameters': ' '},
    # {'filename': 'CVE-2016-4488', 'programname': 'c++filt', 'parameters': ' '},
    # {'filename': 'CVE-2016-4489', 'programname': 'c++filt', 'parameters': ' '},
    # {'filename': 'CVE-2016-4490', 'programname': 'c++filt', 'parameters': ' '},
    # {'filename': 'CVE-2016-4492', 'programname': 'c++filt', 'parameters': ' '},
    # {'filename': 'CVE-2016-4493', 'programname': 'c++filt', 'parameters': ' '},
    # {'filename': 'CVE-2017-7210', 'programname': 'objdump', 'parameters': ' -W @@'},
    # {'filename': 'CVE-2017-14938', 'programname': 'objdump', 'parameters': ' -S @@'},
    # {'filename': 'CVE-2017-8392', 'programname': 'objdump', 'parameters': ' -W @@'},
    # {'filename': 'CVE-2019-9070', 'programname': 'objdump', 'parameters': ' -S @@'},
    # {'filename': 'cplusdem1423', 'programname': 'c++filt', 'parameters': ' '},
    # {'filename': 'cplusdem2744', 'programname': 'c++filt', 'parameters': ' '},
    # {'filename': 'cplusdem4263', 'programname': 'c++filt', 'parameters': ' '},
    # {'filename': 'dwarf22860', 'programname': 'objdump', 'parameters': ' -S @@'},
    # {'filename': 'objcopy3762', 'programname': 'objcopy', 'parameters': ' --compress-debug-section @@'},
    # {'filename': 'objdump2112', 'programname': 'objdump', 'parameters': ' -S @@'},

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
    # {'filename': 'egiflib771', 'programname': 'gifsponge', 'parameters': ''},  # program in the util location.
    # {'filename': 'CVE-2018-19058', 'programname': 'pdfdetch', 'parameters': ' --save 1 @@'},
    # {'filename': 'dumpxml271', 'programname': 'flvmeta', 'parameters': ' @@'},
    # {'filename': 'mjs13671', 'programname': 'mjs-bin', 'parameters': ' -f @@'},
    # {'filename': 'mjs13679', 'programname': 'mjs-bin', 'parameters': ' -f @@'},
    # {'filename': 'mjs9320', 'programname': 'mjs-bin', 'parameters': ' -f @@'},
    # {'filename': 'layer3904', 'programname': 'mp3gain', 'parameters': ' @@'},  # no tar -zxvf, modify Makefile CC=gcc to CC=wllvm.

]


def generateTemplates(path, name, location, template_file, data):
    for each in data:
        file_loader = FileSystemLoader(location)
        env = Environment(loader=file_loader)

        template = env.get_template(template_file)

        output = template.render(filename=each['filename'], programname=each['programname'],
                                 parameters=each['parameters'])
        # print(output)
        filelocation = "dataset/{}/{}/{}".format(path, each['filename'], name)
        print(filelocation)
        with open(filelocation, "w") as f:
            f.write(output)


def createDir(location, list_dirname):
    for each in list_dirname:
        dir_path = location + each
        # dir_path = location + each + "/in"
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        # filepath = dir_path + "/targets.txt"
        # if not os.path.exists(filepath):
        #     with open(filepath, "w") as file:
        #         file.write("")


def validDir(location, list_dirname):
    for each in list_dirname:
        dir_path = location + each
        dir_inpath = location + each + "/in/"
        files = os.listdir(dir_inpath)
        print(files)
        targetfile = dir_path + "/targets.txt"
        print(targetfile)
        with open(targetfile, "r") as f:
            print(f.read())


class OperateDockerWindranger:
    def __init__(self, list_dirname):
        self.client = docker.from_env()
        # self.volumes_path = "/home/fzz/Desktop/STFGFuzz/dataset/CONFF:/root/dataset"
        self.volumes_path = "/home/lxf/fuzzdata/dataset:/root/dataset"
        # self.crash_path = "/home/fzz/Desktop/STFGFuzz/dataset/CONFF/crash/"
        self.crash_path = "/home/lxf/fuzzdata/dataset/crash/"
        self.image = "20230421_windranger"
        self.list_dirname = list_dirname
        self.fuzzname = "windranger_"

    def dockerRun(self):
        for cpui, each in enumerate(self.list_dirname):
            container_name = self.fuzzname + each
            # cpui += 26

            print(container_name, str(cpui))
            # print(docker_name)

            container = self.client.containers.run(name=container_name, image=self.image, volumes=[self.volumes_path],
                                                   privileged=True, detach=True, tty=True,
                                                   # remove=True,
                                                   restart_policy={'Name': 'always'},
                                                   command="/bin/bash",
                                                   cpuset_cpus=str(cpui))  # , cpuset_cpus=str(cpui)

            # Run command line
            # container = self.client.containers.get(container_name)
            exec_output = container.exec_run("rm -rf /home/SVF-tools/example/windranger_fuzz")
            exec_output = container.exec_run("mkdir /home/SVF-tools/example/windranger_fuzz")

            exec_output = container.exec_run(
                "cp -r /root/dataset/source_code/" + each + "/" + each + ".tar.gz /home/SVF-tools/example/")
            exec_output = container.exec_run(
                "cp -r /root/dataset/source_code/" + each + "/in /home/SVF-tools/example/windranger_fuzz/")
            exec_output = container.exec_run(
                "cp -r /root/dataset/source_code/" + each + "/targets.txt /home/SVF-tools/example/windranger_fuzz/")
            exec_output = container.exec_run(
                "cp -r /root/dataset/windranger/" + each + "/windranger.sh /home/SVF-tools/example/windranger_fuzz/")

            # print(exec_output)
            fuzz_command = "tmux new -d -s " + container_name + " 'cd /home/SVF-tools/example/windranger_fuzz && ./windranger.sh -t " + str(
                cpui) + " ; bash'"
            print(fuzz_command)
            # exec_output = container.exec_run("tmux new -s "+container_name+" 'source env_python/bin/activate && "+each[1]+"; bash'")
            # exec_id = self.client.api.exec_create(container.id, cmd=["/bin/bash", "-c", fuzz_command], tty=True)["Id"]
            # self.client.api.exec_resize(exec_id, height=30, width=100)
            # exec_output = self.client.api.exec_start(exec_id, tty=True, stream=False)
            exec_output = container.exec_run(fuzz_command, tty=True, privileged=True, detach=True)
            print(exec_output)

            # raise Exception("stop")

    def dockerStatus(self):
        for each in self.list_dirname:
            container_name = self.fuzzname + each
            container = self.client.containers.get(container_name)

            print()
            print(container_name)
            exec_output = container.exec_run("head -n 2 /home/SVF-tools/example/windranger_fuzz/out/plot_data")
            print(exec_output)
            exec_output = container.exec_run("tail -n 1 /home/SVF-tools/example/windranger_fuzz/out/plot_data")
            print(exec_output)
            # exec_output = container.exec_run("cp -r /home/fzz/Desktop/STFGFuzz/Programs/" + container_name + "/seeds_crash/vis.csv /root/dataset/")

    def dockerSaveCrash(self):
        if not os.path.exists(self.crash_path):
            os.mkdir(self.crash_path)

        for each in self.list_dirname:
            container_name = self.fuzzname + each
            container = self.client.containers.get(container_name)

            crash_name = container_name + "_seeds_crash"

            if os.path.exists(self.crash_path + crash_name):
                raise Exception("Error: Crash file exists.")
            else:
                try:
                    save_command = "tar -cf /home/SVF-tools/example/windranger_fuzz/{}.tar /home/SVF-tools/example/windranger_fuzz/out".format(
                        crash_name)
                    exec_output = container.exec_run(save_command)
                    print(save_command)
                    save_command = "cp -r /home/SVF-tools/example/windranger_fuzz/{}.tar /root/dataset/crash/".format(
                        crash_name)
                    exec_output = container.exec_run(save_command)
                    print(exec_output)
                except Exception as e:
                    with open("error.log", "a+") as f:
                        f.write(str(e) + "\n")

    def dockerStop(self):
        for each in self.list_dirname:
            container_name = self.fuzzname + each
            container = self.client.containers.get(container_name)
            container.stop()
            container.remove()

            print(container_name + " stop remove")

            # raise Exception("stop")


class OperateDockerBeacon:
    def __init__(self, list_dirname):
        self.client = docker.from_env()
        # self.volumes_path = "/home/fzz/Desktop/STFGFuzz/dataset/CONFF:/root/dataset"
        self.volumes_path = "/home/lxf/fuzzdata/dataset:/root/dataset"
        # self.crash_path = "/home/fzz/Desktop/STFGFuzz/dataset/CONFF/crash/"
        self.crash_path = "/home/lxf/fuzzdata/dataset/crash/"
        self.image = "20230425_beacon"
        self.list_dirname = list_dirname
        self.fuzzname = "beacon_"

    def dockerRun(self):
        for cpui, each in enumerate(self.list_dirname):
            container_name = self.fuzzname + each
            # cpui += 26
            # cpui += 10
            # if cpui >= 27:
            #     cpui += 7

            print(container_name, str(cpui))
            # print(docker_name)

            container = self.client.containers.run(name=container_name, image=self.image, volumes=[self.volumes_path],
                                                   privileged=True, detach=True, tty=True,
                                                   # remove=True,
                                                   restart_policy={'Name': 'always'},
                                                   command="/bin/bash",
                                                   cpuset_cpus=str(cpui))  # , cpuset_cpus=str(cpui)

            # Run command line
            # container = self.client.containers.get(container_name)

            exec_output = container.exec_run(
                "cp -r /root/dataset/source_code/" + each + "/" + each + ".tar.gz /Beacon/Test")
            exec_output = container.exec_run("cp -r /root/dataset/source_code/" + each + "/in /Beacon/Test")
            exec_output = container.exec_run("cp -r /root/dataset/source_code/" + each + "/targets.txt /Beacon/Test")
            exec_output = container.exec_run("cp -r /root/dataset/beacon/" + each + "/beacon.sh /Beacon/Test")

            # print(exec_output)
            fuzz_command = "tmux new -d -s " + container_name + " 'cd /Beacon/Test && ./beacon.sh -t " + str(
                cpui) + " ; bash'"
            print(fuzz_command)
            # exec_output = container.exec_run("tmux new -s "+container_name+" 'source env_python/bin/activate && "+each[1]+"; bash'")
            # exec_id = self.client.api.exec_create(container.id, cmd=["/bin/bash", "-c", fuzz_command], tty=True)["Id"]
            # self.client.api.exec_resize(exec_id, height=30, width=100)
            # exec_output = self.client.api.exec_start(exec_id, tty=True, stream=False)
            exec_output = container.exec_run(fuzz_command, tty=True, privileged=True, detach=True)
            print(exec_output)

            # raise Exception("stop")

    def dockerStatus(self):
        for each in self.list_dirname:
            container_name = self.fuzzname + each
            container = self.client.containers.get(container_name)

            print()
            print(container_name)
            exec_output = container.exec_run("head -n 2 /Beacon/Test/out/plot_data")
            print(exec_output)
            exec_output = container.exec_run("tail -n 1 /Beacon/Test/out/plot_data")
            print(exec_output)

            # exec_output = container.exec_run("cp -r /home/fzz/Desktop/STFGFuzz/Programs/" + container_name + "/seeds_crash/vis.csv /root/dataset/")

    def dockerSaveCrash(self):
        if not os.path.exists(self.crash_path):
            os.mkdir(self.crash_path)

        for each in self.list_dirname:
            container_name = self.fuzzname + each
            container = self.client.containers.get(container_name)

            crash_name = container_name + "_seeds_crash"

            if os.path.exists(self.crash_path + crash_name):
                raise Exception("Error: Crash file exists.")
            else:
                try:
                    save_command = "tar -cf /Beacon/Test/{}.tar /Beacon/Test/out".format(crash_name)
                    exec_output = container.exec_run(save_command)
                    print(save_command)
                    save_command = "cp -r /Beacon/Test/{}.tar /root/dataset/crash/".format(crash_name)
                    exec_output = container.exec_run(save_command)
                    print(exec_output)
                except Exception as e:
                    with open("error.log", "a+") as f:
                        f.write(str(e) + "\n")

    def dockerStop(self):
        for each in self.list_dirname:
            container_name = self.fuzzname + each
            container = self.client.containers.get(container_name)
            container.stop()
            container.remove()

            print(container_name + " stop remove")


class OperateDockerAFLGo:
    def __init__(self, list_dirname):
        self.client = docker.from_env()
        # self.volumes_path = "/home/fzz/Desktop/STFGFuzz/dataset/CONFF:/root/dataset"
        self.volumes_path = "/home/lxf/fuzzdata/dataset:/root/dataset"
        # self.crash_path = "/home/fzz/Desktop/STFGFuzz/dataset/CONFF/crash/"
        self.crash_path = "/home/lxf/fuzzdata/dataset/crash/"
        self.image = "20221206_aflgo_experiment"
        self.list_dirname = list_dirname
        self.fuzzname = "aflgo_"

    def dockerRun(self):
        for cpui, each in enumerate(self.list_dirname):
            container_name = self.fuzzname + each

            print(container_name, str(cpui))
            # print(docker_name)

            container = self.client.containers.run(name=container_name, image=self.image, volumes=[self.volumes_path],
                                                   privileged=True, detach=True, tty=True,
                                                   # remove=True,
                                                   restart_policy={'Name': 'always'},
                                                   command="/bin/bash",
                                                   cpuset_cpus=str(cpui))  # , cpuset_cpus=str(cpui)

            # Run command line
            # container = self.client.containers.get(container_name)

            exec_output = container.exec_run(
                "cp -r /root/dataset/source_code/" + each + "/" + each + ".tar.gz /root/aflgo/scripts/fuzz")
            exec_output = container.exec_run("cp -r /root/dataset/source_code/" + each + "/in /root/aflgo/scripts/fuzz")
            exec_output = container.exec_run("cp -r /root/dataset/source_code/" + each + "/targets.txt /root/aflgo/scripts/fuzz")
            exec_output = container.exec_run("cp -r /root/dataset/aflgo/" + each + "/aflgo.sh /root/aflgo/scripts/fuzz")

            # print(exec_output)
            fuzz_command = "tmux new -d -s " + container_name + " 'cd /root/aflgo/scripts/fuzz && ./aflgo.sh -t " + str(
                cpui) + " ; bash'"
            print(fuzz_command)
            # exec_output = container.exec_run("tmux new -s "+container_name+" 'source env_python/bin/activate && "+each[1]+"; bash'")
            # exec_id = self.client.api.exec_create(container.id, cmd=["/bin/bash", "-c", fuzz_command], tty=True)["Id"]
            # self.client.api.exec_resize(exec_id, height=30, width=100)
            # exec_output = self.client.api.exec_start(exec_id, tty=True, stream=False)
            exec_output = container.exec_run(fuzz_command, tty=True, privileged=True, detach=True)
            print(exec_output)

            # raise Exception("stop")

    def dockerStatus(self):
        for each in self.list_dirname:
            container_name = self.fuzzname + each
            container = self.client.containers.get(container_name)

            print()
            print(container_name)
            exec_output = container.exec_run("head -n 2 /root/aflgo/scripts/fuzz/{}/obj-dist/out/plot_data".format(each))
            print(exec_output)
            exec_output = container.exec_run("tail -n 1 /root/aflgo/scripts/fuzz/{}/obj-dist/out/plot_data".format(each))
            print(exec_output)

            # exec_output = container.exec_run("cp -r /home/fzz/Desktop/STFGFuzz/Programs/" + container_name + "/seeds_crash/vis.csv /root/dataset/")

    def dockerSaveCrash(self):
        if not os.path.exists(self.crash_path):
            os.mkdir(self.crash_path)

        for each in self.list_dirname:
            container_name = self.fuzzname + each
            container = self.client.containers.get(container_name)

            crash_name = container_name + "_seeds_crash"

            if os.path.exists(self.crash_path + crash_name):
                raise Exception("Error: Crash file exists.")
            else:
                try:
                    save_command = "tar -cf /root/aflgo/scripts/fuzz/{}/obj-dist/{}.tar /root/aflgo/scripts/fuzz/{}/obj-dist/out".format(each, crash_name, each)
                    exec_output = container.exec_run(save_command)
                    print(save_command)
                    save_command = "cp -r /root/aflgo/scripts/fuzz/{}/obj-dist/{}.tar /root/dataset/crash/".format(each, crash_name)
                    exec_output = container.exec_run(save_command)
                    print(exec_output)
                except Exception as e:
                    with open("error.log", "a+") as f:
                        f.write(str(e) + "\n")

    def dockerStop(self):
        for each in self.list_dirname:
            container_name = self.fuzzname + each
            container = self.client.containers.get(container_name)
            container.stop()
            container.remove()

            print(container_name + " stop remove")


class OperateDockerAngora:
    def __init__(self, list_dirname):
        self.client = docker.from_env()
        # self.volumes_path = "/home/fzz/Desktop/STFGFuzz/dataset/CONFF:/root/dataset"
        self.volumes_path = "/home/lxf/fuzzdata/dataset:/root/dataset"
        # self.crash_path = "/home/fzz/Desktop/STFGFuzz/dataset/CONFF/crash/"
        self.crash_path = "/home/lxf/fuzzdata/dataset/crash/"
        self.image = "20221222_angora_experiment"
        self.list_dirname = list_dirname
        self.fuzzname = "angora_"

    def dockerRun(self):
        for cpui, each in enumerate(self.list_dirname):
            container_name = self.fuzzname + each

            print(container_name, str(cpui))
            # print(docker_name)

            container = self.client.containers.run(name=container_name, image=self.image, volumes=[self.volumes_path],
                                                   privileged=True, detach=True, tty=True,
                                                   # remove=True,
                                                   restart_policy={'Name': 'always'},
                                                   command="/bin/bash",
                                                   cpuset_cpus=str(cpui))  # , cpuset_cpus=str(cpui)

            # Run command line
            # container = self.client.containers.get(container_name)

            exec_output = container.exec_run(
                "cp -r /root/dataset/source_code/" + each + "/" + each + ".tar.gz /root/datav5/Angora-1.2.2/experiment")
            exec_output = container.exec_run("cp -r /root/dataset/source_code/" + each + "/in /root/datav5/Angora-1.2.2/experiment")
            exec_output = container.exec_run("cp -r /root/dataset/source_code/" + each + "/targets.txt /root/datav5/Angora-1.2.2/experiment")
            exec_output = container.exec_run("cp -r /root/dataset/angora/" + each + "/angora.sh /root/datav5/Angora-1.2.2/experiment")

            # print(exec_output)
            fuzz_command = "tmux new -d -s " + container_name + " 'cd /root/datav5/Angora-1.2.2/experiment && ./angora.sh -t " + str(
                cpui) + " ; bash'"
            print(fuzz_command)
            # exec_output = container.exec_run("tmux new -s "+container_name+" 'source env_python/bin/activate && "+each[1]+"; bash'")
            # exec_id = self.client.api.exec_create(container.id, cmd=["/bin/bash", "-c", fuzz_command], tty=True)["Id"]
            # self.client.api.exec_resize(exec_id, height=30, width=100)
            # exec_output = self.client.api.exec_start(exec_id, tty=True, stream=False)
            exec_output = container.exec_run(fuzz_command, tty=True, privileged=True, detach=True)
            print(exec_output)

            # raise Exception("stop")

    def dockerStatus(self):
        for each in self.list_dirname:
            container_name = self.fuzzname + each
            container = self.client.containers.get(container_name)

            print()
            print(container_name)
            exec_output = container.exec_run("head -n 2 /root/datav5/Angora-1.2.2/experiment/out/angora.log")
            print(exec_output)
            exec_output = container.exec_run("head -n 2 /root/datav5/Angora-1.2.2/experiment/out/angora.log")
            print(exec_output)

            # exec_output = container.exec_run("cp -r /home/fzz/Desktop/STFGFuzz/Programs/" + container_name + "/seeds_crash/vis.csv /root/dataset/")

    def dockerSaveCrash(self):
        if not os.path.exists(self.crash_path):
            os.mkdir(self.crash_path)

        for each in self.list_dirname:
            container_name = self.fuzzname + each
            container = self.client.containers.get(container_name)

            crash_name = container_name + "_seeds_crash"

            if os.path.exists(self.crash_path + crash_name):
                raise Exception("Error: Crash file exists.")
            else:
                try:
                    save_command = "tar -cf /root/datav5/Angora-1.2.2/experiment/{}.tar /root/datav5/Angora-1.2.2/experiment/out".format(crash_name)
                    exec_output = container.exec_run(save_command)
                    print(save_command)
                    save_command = "cp -r /root/datav5/Angora-1.2.2/experiment/{}.tar /root/dataset/crash/".format(crash_name)
                    exec_output = container.exec_run(save_command)
                    print(exec_output)
                except Exception as e:
                    with open("error.log", "a+") as f:
                        f.write(str(e) + "\n")

    def dockerStop(self):
        for each in self.list_dirname:
            container_name = self.fuzzname + each
            container = self.client.containers.get(container_name)
            container.stop()
            container.remove()

            print(container_name + " stop remove")


if __name__ == '__main__':
    # print(len(list_dirname))
    # print(len(set(list_dirname)))
    # for i in range(len(list_dirname)):
    #     for j in range(len(list_dirname)):
    #         if i != j and list_dirname[i] == list_dirname[j]:
    #             print(list_dirname[i])

    # createDir("/home/fzz/Desktop/STFGFuzz/Programs/Experiment/second_experiment/dataset/source_code/", list_dirname)
    # validDir("/home/fzz/Desktop/STFGFuzz/Programs/Experiment/second_experiment/dataset/source_code/", list_dirname)

    # OperateDockerWindranger(list_dirname).dockerRun()
    # OperateDockerWindranger(list_dirname).dockerStatus()
    # OperateDockerWindranger(list_dirname).dockerSaveCrash()
    # OperateDockerWindranger(list_dirname).dockerStop()

    # OperateDockerBeacon(list_dirname).dockerRun()
    # OperateDockerBeacon(list_dirname).dockerStatus()
    # OperateDockerBeacon(list_dirname).dockerSaveCrash()
    # OperateDockerBeacon(list_dirname).dockerStop()

    # OperateDockerAFLGo(list_dirname).dockerRun()
    # OperateDockerAFLGo(list_dirname).dockerStatus()
    # OperateDockerAFLGo(list_dirname).dockerSaveCrash()
    # OperateDockerAFLGo(list_dirname).dockerStop()

    # OperateDockerAngora(list_dirname).dockerRun()
    # OperateDockerAngora(list_dirname).dockerStatus()
    # OperateDockerAngora(list_dirname).dockerSaveCrash()
    # OperateDockerAngora(list_dirname).dockerStop()

    # generateTemplates("windranger", "windranger.sh", "dataset/templates", "windranger_c++filt.sh", template)
    # generateTemplates("windranger", "windranger.sh", "dataset/templates", "windranger_swftophp.sh", template)

    # generateTemplates("beacon", "beacon.sh", "dataset/templates", "beacon_c++filt.sh", template)
    # generateTemplates("beacon", "beacon.sh", "dataset/templates", "beacon_swftophp.sh", template)

    # generateTemplates("aflgo", "aflgo.sh", "dataset/templates", "aflgo_c++filt.sh", template)
    # generateTemplates("aflgo", "aflgo.sh", "dataset/templates", "aflgo_swftophp.sh", template)

    # generateTemplates("angora", "angora.sh", "dataset/templates", "angora_c++filt.sh", template)
    generateTemplates("angora", "angora.sh", "dataset/templates", "angora_swftophp.sh", template)
