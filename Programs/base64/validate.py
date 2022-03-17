import os
import subprocess


PROGRAM_NAME = "base64"

def run(cmd: str) -> (int, str, str):
    """
    run cmd to get information from executable files or other tools
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


if __name__ == "__main__":
    print("Checking if buggy {} succeeds on non-trigger input...".format(PROGRAM_NAME))
    run_cmd = "./code_Bin/" + PROGRAM_NAME + " -d seeds_init/rand.b64"
    ret_code, std_out, std_err = run(run_cmd)
    # print(ret_code, std_err)
    if not std_err:
        print("Success: {} returned {}".format(run_cmd, ret_code))
    else:
        print("ERROR: {} returned {}".format(run_cmd, ret_code))

    print("Validating bugs...")
    valibugslist = []
    with open("validated_bugs", 'r') as f:
        for line in f:
            valibugslist.append(line.replace('\n', ''))
    len_valibugs = len(valibugslist)
    num_success = 0
    "validated.txt"
    vfname = "validated.txt"
    if os.path.exists(vfname):
        os.remove(vfname)

    vf = open(vfname, "a+")
    for i in range(len_valibugs):
        fuzz_cmd = "./code_Bin/" + PROGRAM_NAME + " -d validate_inputs/utmp-fuzzed-" + str(valibugslist[i]) + ".b64"
        ret_code, std_out, std_err = run(fuzz_cmd)
        print(std_out.decode("utf-8"))
        num_success += 1
        vf.write(str(valibugslist[i]) + " " + str(ret_code) + "\n")
    vf.close()
    print("Validated {} / {} bugs".format(num_success, len_valibugs))
    print("You can see validated.txt for the exit code of each buggy version.")


# Successfully triggered bug 1, crashing now!
# Successfully triggered bug 1, crashing now!
# Segmentation fault (core dumped)

