from setup.args import parse_args
from setup.runtime import Runtime

import sys

if __name__ == "__main__":
    parser = parse_args(sys.argv[1:])
    Runtime.init(parser)
