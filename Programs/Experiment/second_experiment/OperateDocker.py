import os
import docker


list_cve_second = [
    # ["demo", "python3 STFGFuzzer.py -n demo -t sanitize -- ./Programs/demo/code_Bin/demo -f @seed@"],
    # # ming 4.7
    # ["ming47-CVE-2016-9827", "python3 STFGFuzzer.py -n ming47-CVE-2016-9827 -t sanitize -- ./Programs/ming47-CVE-2016-9827/code_Bin/ming47-CVE-2016-9827 @seed@ "],
    # ["ming47-CVE-2016-9829", "python3 STFGFuzzer.py -n ming47-CVE-2016-9829 -t sanitize -- ./Programs/ming47-CVE-2016-9829/code_Bin/ming47-CVE-2016-9829 @seed@ "],
    # ["ming47-CVE-2016-9831", "python3 STFGFuzzer.py -n ming47-CVE-2016-9831 -t sanitize -- ./Programs/ming47-CVE-2016-9831/code_Bin/ming47-CVE-2016-9831 @seed@ "],
    # ["ming47-CVE-2017-7578", "python3 STFGFuzzer.py -n ming47-CVE-2017-7578 -t sanitize -- ./Programs/ming47-CVE-2017-7578/code_Bin/ming47-CVE-2017-7578 @seed@ "],
    # ["ming47-CVE-2017-9988", "python3 STFGFuzzer.py -n ming47-CVE-2017-9988 -t sanitize -- ./Programs/ming47-CVE-2017-9988/code_Bin/ming47-CVE-2017-9988 @seed@ "],
    # ["ming47-CVE-2017-11728", "python3 STFGFuzzer.py -n ming47-CVE-2017-11728 -t sanitize -- ./Programs/ming47-CVE-2017-11728/code_Bin/ming47-CVE-2017-11728 @seed@ /dev/null "],
    # ["ming47-CVE-2017-11729", "python3 STFGFuzzer.py -n ming47-CVE-2017-11729 -t sanitize -- ./Programs/ming47-CVE-2017-11729/code_Bin/ming47-CVE-2017-11729 @seed@ /dev/null "],
    # # ming 4.8
    # ["ming48-CVE-2018-7868", "python3 STFGFuzzer.py -n ming48-CVE-2018-7868 -t sanitize -- ./Programs/ming48-CVE-2018-7868/code_Bin/ming48-CVE-2018-7868 @seed@ /dev/null "],
    # ["ming48-CVE-2018-8807", "python3 STFGFuzzer.py -n ming48-CVE-2018-8807 -t sanitize -- ./Programs/ming48-CVE-2018-8807/code_Bin/ming48-CVE-2018-8807 @seed@ "],
    # ["ming48-CVE-2018-8962", "python3 STFGFuzzer.py -n ming48-CVE-2018-8962 -t sanitize -- ./Programs/ming48-CVE-2018-8962/code_Bin/ming48-CVE-2018-8962 @seed@ "],
    # ["ming48-CVE-2018-11095", "python3 STFGFuzzer.py -n ming48-CVE-2018-11095 -t sanitize -- ./Programs/ming48-CVE-2018-11095/code_Bin/ming48-CVE-2018-11095 @seed@ "],
    # ["ming48-CVE-2018-11225", "python3 STFGFuzzer.py -n ming48-CVE-2018-11225 -t sanitize -- ./Programs/ming48-CVE-2018-11225/code_Bin/ming48-CVE-2018-11225 @seed@ "],
    # ["ming48-CVE-2018-11226", "python3 STFGFuzzer.py -n ming48-CVE-2018-11226 -t sanitize -- ./Programs/ming48-CVE-2018-11226/code_Bin/ming48-CVE-2018-11226 @seed@ "],
    # ["ming48-CVE-2018-20427", "python3 STFGFuzzer.py -n ming48-CVE-2018-20427 -t sanitize -- ./Programs/ming48-CVE-2018-20427/code_Bin/ming48-CVE-2018-20427 @seed@ "],
    # ["ming48-CVE-2019-9114", "python3 STFGFuzzer.py -n ming48-CVE-2019-9114 -t sanitize -- ./Programs/ming48-CVE-2019-9114/code_Bin/ming48-CVE-2019-9114 @seed@ "],
    # ["ming48-CVE-2019-12982", "python3 STFGFuzzer.py -n ming48-CVE-2019-12982 -t manual -- ./Programs/ming48-CVE-2019-12982/code_Bin/ming48-CVE-2019-12982 @seed@ "],
    # ["ming48-CVE-2020-6628", "python3 STFGFuzzer.py -n ming48-CVE-2020-6628 -t manual -- ./Programs/ming48-CVE-2020-6628/code_Bin/ming48-CVE-2020-6628 @seed@ "],
    # # lzip
    # ["lzip-CVE-2017-8846", ],
    # ["lzip-CVE-2018-11496", ],
    # c++flit
    # # # # ["cxxflit-CVE-2016-4491", "python3 STFGFuzzer.py -n cxxflit-CVE-2016-4491 -t sanitize -- ./Programs/cxxflit-CVE-2016-4491/code_Bin/cxxflit-CVE-2016-4491 @@seed@ "],
    # # # # ["cxxflit-CVE-2016-6131", "python3 STFGFuzzer.py -n cxxflit-CVE-2016-6131 -t sanitize -- ./Programs/cxxflit-CVE-2016-6131/code_Bin/cxxflit-CVE-2016-6131 @@seed@ "],
    # # # # # # xmllint
    # # # # ["xmllint-CVE-2017-5969", "python3 STFGFuzzer.py -n xmllint-CVE-2017-5969 -t sanitize -- ./Programs/xmllint-CVE-2017-5969/code_Bin/xmllint-CVE-2017-5969 --recover @seed@ "],
    # # # # ["xmllint-CVE-2017-9047", "python3 STFGFuzzer.py -n xmllint-CVE-2017-9047 -t sanitize -- ./Programs/xmllint-CVE-2017-9047/code_Bin/xmllint-CVE-2017-9047 --valid @seed@ "],
    # # # # ["xmllint-CVE-2017-9048", "python3 STFGFuzzer.py -n xmllint-CVE-2017-9048 -t sanitize -- ./Programs/xmllint-CVE-2017-9048/code_Bin/xmllint-CVE-2017-9048 --memory --oldxml10 @seed@ "],
    # # # # ["xmllint-CVE-2017-9049", "python3 STFGFuzzer.py -n xmllint-CVE-2017-9049 -t sanitize -- ./Programs/xmllint-CVE-2017-9049/code_Bin/xmllint-CVE-2017-9049 --oldxml10 @seed@ "],
    # # # # # objdump
    # # # # ["objdump-CVE-2017-8392", "python3 STFGFuzzer.py -n objdump-CVE-2017-8392 -t sanitize -- ./Programs/objdump-CVE-2017-8392/code_Bin/objdump-CVE-2017-8392 -SD @seed@ "],
    # # # # ["objdump-CVE-2017-8396", "python3 STFGFuzzer.py -n objdump-CVE-2017-8396 -t sanitize -- ./Programs/objdump-CVE-2017-8396/code_Bin/objdump-CVE-2017-8396 -W @seed@ "],
    # # # # ["objdump-CVE-2017-8397", "python3 STFGFuzzer.py -n objdump-CVE-2017-8397 -t sanitize -- ./Programs/objdump-CVE-2017-8397/code_Bin/objdump-CVE-2017-8397 -W @seed@ "],
    # # # # ["objdump-CVE-2017-8398", "python3 STFGFuzzer.py -n objdump-CVE-2017-8398 -t sanitize -- ./Programs/objdump-CVE-2017-8398/code_Bin/objdump-CVE-2017-8398 -W @seed@ "],
    # # # # ["objdump-CVE-2017-14940", "python3 STFGFuzzer.py -n objdump-CVE-2017-14940 -t sanitize -- ./Programs/objdump-CVE-2017-14940/code_Bin/objdump-CVE-2017-14940 -A -a -l -S -s --special-syms --synthetic --with-symbol-versions -D @seed@ "],  # nm
    # # # # ["objdump-CVE-2017-16828", "python3 STFGFuzzer.py -n objdump-CVE-2017-16828 -t sanitize -- ./Programs/objdump-CVE-2017-16828/code_Bin/objdump-CVE-2017-16828 -w @seed@ "],  # readelf
    # # # # # ## ["objdump-CVE-2017-17360", ""],  # REJECT
    # # # # # # objcopy
    # # # # ["objcopy-CVE-2017-7303", "python3 STFGFuzzer.py -n objcopy-CVE-2017-7303 -t sanitize -- ./Programs/objcopy-CVE-2017-7303/code_Bin/objcopy-CVE-2017-7303 @seed@ "],
    # # # # ["objcopy-CVE-2017-8393", "python3 STFGFuzzer.py -n objcopy-CVE-2017-8393 -t sanitize -- ./Programs/objcopy-CVE-2017-8393/code_Bin/objcopy-CVE-2017-8393 --compress-debug-sections @seed@ "],
    # # # # ["objcopy-CVE-2017-8394", "python3 STFGFuzzer.py -n objcopy-CVE-2017-8394 -t sanitize -- ./Programs/objcopy-CVE-2017-8394/code_Bin/objcopy-CVE-2017-8394 -Gs @seed@ "],
    # # # # ["objcopy-CVE-2017-8395", "python3 STFGFuzzer.py -n objcopy-CVE-2017-8395 -t sanitize -- ./Programs/objcopy-CVE-2017-8395/code_Bin/objcopy-CVE-2017-8395 --compress-debug-section @seed@ "],
    # cjpeg
    # ## ["cjpeg-CVE-2018-14498", "python3 STFGFuzzer.py -n cjpeg-CVE-2018-14498 -t sanitize -- ./Programs/cjpeg-CVE-2018-14498/code_Bin/cjpeg-CVE-2018-14498 -outfile /dev/null @seed@ "],
    # ["cjpeg-CVE-2020-13790", "python3 STFGFuzzer.py -n cjpeg-CVE-2020-13790 -t sanitize -- ./Programs/cjpeg-CVE-2020-13790/code_Bin/cjpeg-CVE-2020-13790 @seed@ "],
    # pngimage
    # ["pngimage-CVE-2018-13785", "python3 STFGFuzzer.py -n pngimage-CVE-2018-13785 -t manual -- ./Programs/pngimage-CVE-2018-13785/code_Bin/pngimage-CVE-2018-13785 @seed@ "],
    # ["pngimage-CVE-2018-13785_nochecksum", "python3 STFGFuzzer.py -n pngimage-CVE-2018-13785_nochecksum -t manual -- ./Programs/pngimage-CVE-2018-13785_nochecksum/code_Bin/pngimage-CVE-2018-13785_nochecksum @seed@ "],
    # pdftoppm
    # ["pdftoppm-CVE-2019-10872", "python3 STFGFuzzer.py -n pdftoppm-CVE-2019-10872 -t sanitize -- ./Programs/pdftoppm-CVE-2019-10872/code_Bin/pdftoppm-CVE-2019-10872 -cropbox -mono @seed@ "],
    # ["pdftoppm-CVE-2019-10873", "python3 STFGFuzzer.py -n pdftoppm-CVE-2019-10873 -t sanitize -- ./Programs/pdftoppm-CVE-2019-10873/code_Bin/pdftoppm-CVE-2019-10873 -cropbox -jpeg -freetype yes @seed@ tmp "],
    # ["pdftoppm-CVE-2019-14494", "python3 STFGFuzzer.py -n pdftoppm-CVE-2019-14494 -t sanitize -- ./Programs/pdftoppm-CVE-2019-14494/code_Bin/pdftoppm-CVE-2019-14494 -cropbox -gray @seed@ "],
    # pdftops
    # ["pdftops-CVE-2019-10871", "python3 STFGFuzzer.py -n pdftops-CVE-2019-10871 -t sanitize -- ./Programs/pdftops-CVE-2019-10871/code_Bin/pdftops-CVE-2019-10871 -level1sep @seed@ /dev/null "],
    # pdfdetach
    # ["pdfdetach-CVE-2018-19058", "python3 STFGFuzzer.py -n pdfdetach-CVE-2018-19058 -t sanitize -- ./Programs/pdfdetach-CVE-2018-19058/code_Bin/pdfdetach-CVE-2018-19058 --save 1 @seed@ "],
    # ["pdfdetach-CVE-2018-19059", "python3 STFGFuzzer.py -n pdfdetach-CVE-2018-19059 -t sanitize -- ./Programs/pdfdetach-CVE-2018-19059/code_Bin/pdfdetach-CVE-2018-19059 --save 1 @seed@ "],
    # ["pdfdetach-CVE-2018-19060", "python3 STFGFuzzer.py -n pdfdetach-CVE-2018-19060 -t sanitize -- ./Programs/pdfdetach-CVE-2018-19060/code_Bin/pdfdetach-CVE-2018-19060 --save 1 @seed@ "],
    # avconv
    # ["avconv-CVE-2018-11102", "python3 STFGFuzzer.py -n avconv-CVE-2018-11102 -t manual -- ./Programs/avconv-CVE-2018-11102/code_Bin/avconv-CVE-2018-11102 -y -i @seed@ "],
    # ["avconv-CVE-2018-11224", "python3 STFGFuzzer.py -n avconv-CVE-2018-11224 -t manual -- ./Programs/avconv-CVE-2018-11224/code_Bin/avconv-CVE-2018-11224 -y -i @seed@ "],
    # ["avconv-CVE-2018-18829", "python3 STFGFuzzer.py -n avconv-CVE-2018-18829 -- ./Programs/avconv-CVE-2018-18829/code_Bin/avconv-CVE-2018-18829 -y -i @seed@ "],
    # ["avconv-CVE-2019-14441", "python3 STFGFuzzer.py -n avconv-CVE-2019-14441 -- ./Programs/avconv-CVE-2019-14441/code_Bin/avconv-CVE-2019-14441 -y -i @seed@ "],
    # ["avconv-CVE-2019-14443", "python3 STFGFuzzer.py -n avconv-CVE-2019-14443 -- ./Programs/avconv-CVE-2019-14443/code_Bin/avconv-CVE-2019-14443 -y -i @seed@ "],
    #####################
    # windranger
    ["bento4", "python3 STFGFuzzer.py -n bento4 -t manual -- ./Programs/bento4/code_Bin/bento4 @seed@ /dev/null "],
    ["objdump228", "python3 STFGFuzzer.py -n objdump228 -t manual -- ./Programs/objdump228/code_Bin/objdump228 -S @seed@ "],
    ["cflow", "python3 STFGFuzzer.py -n cflow -- ./Programs/cflow/code_Bin/cflow @seed@ "],
    ## ["ffmpeg", "python3 STFGFuzzer.py -n ffmpeg -- ./Programs/ffmpeg/code_Bin/ffmpeg  -y -i @seed@ -c:v mpeg4 -c:a copy -f mp4 /dev/null "],
    ["flvmeta", "python3 STFGFuzzer.py -n flvmeta -- ./Programs/flvmeta/code_Bin/flvmeta @seed@ "],
    ["jhead", "python3 STFGFuzzer.py -n jhead -- ./Programs/jhead/code_Bin/jhead @seed@ "],
    ["jq", "python3 STFGFuzzer.py -n jq -- ./Programs/jq/code_Bin/jq . @seed@ "],
    ["lame", "python3 STFGFuzzer.py -n lame -t manual -- ./Programs/lame/code_Bin/lame @seed@ /dev/null "],
    ["mp3gain", "python3 STFGFuzzer.py -n mp3gain -- ./Programs/mp3gain/code_Bin/mp3gain @seed@ "],
    ["mujs", "python3 STFGFuzzer.py -n mujs -t manual -- ./Programs/mujs/code_Bin/mujs @seed@ "],
    ## ["tcpdump", "python3 STFGFuzzer.py -n tcpdump -t manual -- ./Programs/tcpdump/code_Bin/tcpdump -e -vv -nr @seed@ "],
    ##
    # asan compile again
    ["mp42aac_asan", "python3 STFGFuzzer.py -n mp42aac_asan -t manual -- ./Programs/mp42aac_asan/code_Bin/mp42aac_asan @seed@ /dev/null "],
    ["objdump228_asan", "python3 STFGFuzzer.py -n objdump228_asan -t manual -- ./Programs/objdump228_asan/code_Bin/objdump228_asan -S @seed@ "],
    ["objdump5279478_asan", "python3 STFGFuzzer.py -n objdump5279478_asan -t manual -- ./Programs/objdump5279478_asan/code_Bin/objdump5279478_asan -S @seed@ "],
    ["lame_asan", "python3 STFGFuzzer.py -n lame_asan -t manual -- ./Programs/lame_asan/code_Bin/lame_asan @seed@ /dev/null "],
    ["mujs_asan", "python3 STFGFuzzer.py -n mujs_asan -t manual -- ./Programs/mujs_asan/code_Bin/mujs_asan @seed@ "],
    ## ["tcpdump_asan", "python3 STFGFuzzer.py -n tcpdump_asan -t manual -- ./Programs/tcpdump_asan/code_Bin/tcpdump_asan -e -vv -nr @seed@ "],
    ["imginfo_asan", "python3 STFGFuzzer.py -n imginfo_asan -t manual -- ./Programs/imginfo_asan/code_Bin/imginfo_asan -f @seed@ "],
    ## export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
]


class OperateDocker():
    def __init__(self):
        self.client = docker.from_env()
        self.volumes_path = "/home/fzz/Desktop/STFGFuzz/dataset/CONFF:/root/dataset"
        # self.volumes_path = "/home/lxf/fuzzdata/CONFF:/root/dataset"
        self.crash_path = "/home/fzz/Desktop/STFGFuzz/dataset/CONFF/crash/"
        # self.crash_path = "/home/lxf/fuzzdata/CONFF/crash/"

    def dockerRun(self):
        for each in list_cve_second:
            container_name = each[0]


            print(each)
            # print(docker_name)

            container = self.client.containers.run(name=container_name, image="conff", volumes=[self.volumes_path],
                                  privileged=True, detach=True, tty=True, remove=True, command="/bin/bash")

            # Run command line
            # container = self.client.containers.get(container_name)
            exec_output = container.exec_run("cp -r /root/dataset/STFGFuzzer.py /home/fzz/Desktop/STFGFuzz/")
            exec_output = container.exec_run("cp -r /root/dataset/fuzzer_module /home/fzz/Desktop/STFGFuzz/")
            exec_output = container.exec_run("cp -r /root/dataset/"+container_name+" /home/fzz/Desktop/STFGFuzz/Programs/")


            # exec_output = container.exec_run("cd /home/fzz/Desktop/STFGFuzz/")
            exec_output = container.exec_run("echo 0 > /proc/sys/kernel/randomize_va_space")
            # exec_output = container.exec_run("apt install -y liblzo2-dev")
            # print(exec_output)
            fuzz_command = "tmux new -s " + container_name + " 'echo 0 > /proc/sys/kernel/randomize_va_space && cd /home/fzz/Desktop/STFGFuzz/ && export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH && source env_python/bin/activate && " + each[1] + "; bash'"
            print(fuzz_command)
            # exec_output = container.exec_run("tmux new -s "+container_name+" 'source env_python/bin/activate && "+each[1]+"; bash'")
            exec_output = container.exec_run(fuzz_command, tty=True, privileged=True, detach=True)
            print(exec_output)

            raise Exception("stop")

    def dockerStatus(self):
        for each in list_cve_second:
            container_name = each[0]
            container = self.client.containers.get(container_name)

            exec_output = container.exec_run("cat /home/fzz/Desktop/STFGFuzz/Programs/" + container_name + "/seeds_crash/vis.csv")
            print(exec_output)
            # exec_output = container.exec_run("cp -r /home/fzz/Desktop/STFGFuzz/Programs/" + container_name + "/seeds_crash/vis.csv /root/dataset/")

            # raise Exception("stop")

    def dockerSaveCrash(self):
        for each in list_cve_second:
            container_name = each[0]
            container = self.client.containers.get(container_name)

            if not os.path.exists(self.crash_path):
                os.mkdir(self.crash_path)


            crash_name = container_name + "_seeds_crash"

            if os.path.exists(self.crash_path + crash_name):
                raise Exception("Error: Crash file exists.")
            else:
                try:
                    save_command = "cp -r /home/fzz/Desktop/STFGFuzz/Programs/" + container_name + "/seeds_crash /root/dataset/crash/"+crash_name
                    print(save_command)
                    exec_output = container.exec_run(save_command)
                    print(exec_output)
                except Exception as e:
                    with open("error.log", "a+") as f:
                        f.write(str(e) + "\n")

            # raise Exception("stop")

    def dockerStop(self):
        for each in list_cve_second:
            container_name = each[0]
            container = self.client.containers.get(container_name)
            container.stop()

            print(container_name + " stop")

            # raise Exception("stop")



def buildFiles():
    print(os.getcwd())
    os.chdir('/home/fzz/Desktop/STFGFuzz/Programs')
    print(os.getcwd())
    for idx in range(0, len(list_cve_second)):
        dirname = str(list_cve_second[idx])
        buildcmd = "./build.sh -n "+dirname+" clang"
        print(buildcmd)
        os.system(buildcmd)

if __name__ == '__main__':
    # buildFiles()
    OperateDocker().dockerRun()
    # OperateDocker().dockerStatus()
    # OperateDocker().dockerSaveCrash()
    # OperateDocker().dockerStop()
