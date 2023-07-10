from setup.args import parse_args
import sys

if __name__ == "__main__":
    parser = parse_args(sys.argv[1:])
    print(parser.files)
