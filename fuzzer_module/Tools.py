import datetime
import subprocess


def saveAsFile(content: str, filename: str):
    """
    Store mutated strings as files for easy reading by test programs.
    @param content:
    @param filename:
    @return:
    """
    with open(filename, "w") as f:
        f.write(content)


def getMutfilename(label: str) -> str:
    return str(datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')) + "_" + str(label) + ".seed"


def getFileContent(filepathname: str) -> str:
    """
    Get the content of the seed file.
    @param filepathname:
    @return:
    """
    file_str = ""
    with open(filepathname, 'r', encoding="UTF-8") as f:
        file_content = f.readlines()
    for each in file_content:
        file_str += each
    return file_str


def mergeMapReport(inputmap, totalinputmap):
    """
    Generate byte-level mapping reports.
    @param inputmap:
    @param totalinputmap:
    @return:
    """
    for loc, byte in inputmap.items():
        if loc not in totalinputmap:
            totalinputmap[loc] = byte


def runothercmd(cmd: str) -> (int, str, str):
    """
    run cmd to get information from executable files or other tools
    @param cmd:
    @return:
    """
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    # timeout kill child process
    try:
        std_out, std_err = process.communicate()
    except Exception as e:
        process.kill()
        raise Exception("Error cmd ")
    ret_code = 128 - process.returncode
    # print(ret_code, std_out, std_err)
    return ret_code, std_out, std_err


