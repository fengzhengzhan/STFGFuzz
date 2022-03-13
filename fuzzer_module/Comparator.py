
from fuzzer_module.Fuzzconfig import *


def getDirectedLocation(programe_name: str, filetype: str, ):
    """
    Get the required number of lines of directed functions corresponding to the binary block position.
    There are three types: git patch, sanitizer, manual.
    @return:
    """
    if filetype == COM_PATCH:
        pass

    if filetype == COM_SANITIZER:
        pass

    if filetype == COM_MANUAL:
        # target:stack:funcname:line
        # A blank line is required between the different targets of the manual mutation target.
        temp_manualfile = PROGRAMS + os.sep
        pass


def reuseHistorySTFG():
    """
    Compare functions and reuse the constraint flow graphs used in the history.
    @return:
    """
    pass

