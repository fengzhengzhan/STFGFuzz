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
    # "validated.txt"
    vfname = "validated.txt"
    if os.path.exists(vfname):
        os.remove(vfname)

    vf = open(vfname, "a+")
    for i in range(len_valibugs):
        fuzz_cmd = "./code_Bin/" + PROGRAM_NAME + " -d seeds_crash/validate_inputs/utmp-fuzzed-" + str(valibugslist[i]) + ".b64"
        # fuzz_cmd = "./code_Bin/" + PROGRAM_NAME + " -d seeds_init/rand.b64"
        ret_code, std_out, std_err = run(fuzz_cmd)
        find_state = std_out.find(bytes("Successfully triggered bug {}, crashing now!".format(str(valibugslist[i])), encoding="utf-8"))
        if find_state != -1:
            num_success += 1
            print("{}:{}->{} ".format(i+1, str(valibugslist[i]), "Success"))
        else:
            print("{}:{}->{} ".format(i+1, str(valibugslist[i]), "Fail"))
        vf.write(str(valibugslist[i]) + " " + str(ret_code) + "\n")
    vf.close()
    print()
    print("Validated {} / {} bugs".format(num_success, len_valibugs))
    print("You can see validated.txt for the exit code of each buggy version.")



