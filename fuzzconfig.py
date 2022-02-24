import logging


LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='InfoData/log_data/BTFuzzer.log', level=logging.WARNING, format=LOG_FORMAT)
logging.debug("-------------------------")


def FUZZLOGGING(loggingtype: str, infomation: str) -> None:
    if loggingtype == "DEBUG":
        logging.debug(infomation)
    elif loggingtype == "INFO":
        logging.info(infomation)
    elif loggingtype == "WARNING":
        logging.warning(infomation)
    elif loggingtype == "ERROR":
        logging.error(infomation)
    elif loggingtype == "CRITICAL":
        logging.critical(infomation)
    else:
        raise Exception("Error logging.")