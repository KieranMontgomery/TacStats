import argparse

parser = argparse.ArgumentParser(
    prog="TacStats",
    description="A tool for analyzing TacView files",
    epilog="Made by: Kieran Montgomery",
)

parser.add_argument(
    "file(s)",
    nargs="+",
    help="The TacView file(s) to analyze. Can be a single file, multiple files, or a directory of files.",  # noqa
)
