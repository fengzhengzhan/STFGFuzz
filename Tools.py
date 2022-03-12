import datetime


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


def getSeedContent(filepathname: str) -> str:
    """
    Get the content of the seed file.
    @param filepathname:
    @return:
    """
    seed_str = ""
    with open(filepathname, 'r', encoding="UTF-8") as f:
        seed_content = f.readlines()
    for each in seed_content:
        seed_str += each
    return seed_str


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
