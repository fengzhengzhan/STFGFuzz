import datetime


def getMutfilename(label: str) -> str:
    return str(datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')) + "_" + str(label) + ".seed"

def saveAsFile(content: str, filename: str):
    '''
    Store mutated strings as files for easy reading by test programs.
    '''
    with open(filename, "w") as f:
        f.write(content)


def getSeedContent(filepathname: str) -> str:
    '''
    Get the content of the seed file.
    '''
    seed_str = ""
    with open(filepathname, 'r', encoding="UTF-8") as f:
        seed_content = f.readlines()
    for each in seed_content:
        seed_str += each
    return seed_str
