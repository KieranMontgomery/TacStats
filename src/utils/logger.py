import datetime
import logging
import os


class Colors:
    CEND = "\33[0m"
    CBOLD = "\33[1m"
    CITALIC = "\33[3m"
    CURL = "\33[4m"
    CBLINK = "\33[5m"
    CBLINK2 = "\33[6m"
    CSELECTED = "\33[7m"

    CBLACK = "\33[30m"
    CRED = "\33[31m"
    CGREEN = "\33[32m"
    CYELLOW = "\33[33m"
    CBLUE = "\33[34m"
    CVIOLET = "\33[35m"
    CBEIGE = "\33[36m"
    CWHITE = "\33[37m"

    CBLACKBG = "\33[40m"
    CREDBG = "\33[41m"
    CGREENBG = "\33[42m"
    CYELLOWBG = "\33[43m"
    CBLUEBG = "\33[44m"
    CVIOLETBG = "\33[45m"
    CBEIGEBG = "\33[46m"
    CWHITEBG = "\33[47m"

    CGREY = "\33[90m"
    CRED2 = "\33[91m"
    CGREEN2 = "\33[92m"
    CYELLOW2 = "\33[93m"
    CBLUE2 = "\33[94m"
    CVIOLET2 = "\33[95m"
    CBEIGE2 = "\33[96m"
    CWHITE2 = "\33[97m"

    CGREYBG = "\33[100m"
    CREDBG2 = "\33[101m"
    CGREENBG2 = "\33[102m"
    CYELLOWBG2 = "\33[103m"
    CBLUEBG2 = "\33[104m"
    CVIOLETBG2 = "\33[105m"
    CBEIGEBG2 = "\33[106m"
    CWHITEBG2 = "\33[107m"


class LogFormatter(logging.Formatter):
    COLOR_CODES = {
        logging.CRITICAL: Colors.CVIOLET2,  # bright/bold magenta
        logging.ERROR: Colors.CRED2,  # bright/bold red
        logging.WARNING: Colors.CYELLOW2,  # bright/bold yellow
        logging.INFO: Colors.CWHITE2,  # white / light gray
        logging.DEBUG: Colors.CBLUE2,  # bright/bold black / dark gray
    }

    def __init__(self, color, *args, **kwargs):
        super(LogFormatter, self).__init__(*args, **kwargs)
        self.color = color

    def format(self, record, *args, **kwargs):
        msg = super(LogFormatter, self).format(record, *args, **kwargs)
        if self.color and record.levelno in self.COLOR_CODES:
            return self.COLOR_CODES[record.levelno] + msg + Colors.CEND
        else:
            return msg


class Logger(logging.Logger):
    def __init__(self, name, level=logging.DEBUG):
        super().__init__(name, level)
        self.formatter = LogFormatter(
            fmt="[%(asctime)s] %(levelname)-8s | %(message)s",
            color=True,
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        self.handler = logging.StreamHandler()
        self.handler.setFormatter(self.formatter)
        self.addHandler(self.handler)

        # Get current datetime as a string
        now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        if not os.path.exists("./logs"):
            os.mkdir("./logs")

        file_handler = logging.FileHandler(f"logs/TacStats_{now}.log")
        file_formatter = LogFormatter(
            fmt="[%(asctime)s] %(levelname)-8s | %(message)s | %(module)s.%(funcName)s@%(lineno)d",  # noqa
            color=False,
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        file_handler.setFormatter(file_formatter)
        self.addHandler(file_handler)

    def setLevel(self, level):
        super().setLevel(level)


logger = Logger("TacStats")
