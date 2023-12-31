import sys
import time

from file.reader import FileReader
from setup.args import parse_args
from setup.runtime import Runtime
from utils.logger import logger

if __name__ == "__main__":
    t0 = time.perf_counter()
    parser = parse_args(sys.argv[1:])
    Runtime.init(parser)

    logger.debug(f"Files: {Runtime.files}")

    file_readers = [FileReader(file) for file in Runtime.files]

    for file_reader in file_readers:
        file_reader.read()

    t1 = time.perf_counter()
    logger.info(f"Finished in {t1 - t0:0.5f} seconds")
