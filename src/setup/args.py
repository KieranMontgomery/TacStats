import argparse


def parse_args(args):
    parser = argparse.ArgumentParser(
        prog="TacStats",
        description="A tool for analyzing TacView files",
        epilog="Made by: Kieran Montgomery",
    )

    parser.add_argument(
        "files",
        nargs="+",
        help="The TacView file(s) to analyze. Can be a single file, multiple files, or a directory of files.",  # noqa
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="Enable verbose logging. Can be used multiple times (up to 3x) to increase verbosity.",  # noqa
    )

    return parser.parse_args(args)
