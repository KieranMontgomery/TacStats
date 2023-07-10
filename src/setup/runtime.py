import os
import argparse


class Runtime:
    """
    Runtime is a static class that holds the runtime state of the program.
    """

    @staticmethod
    def init(parsed_args: argparse.ArgumentParser):
        Runtime.parse_files(parsed_args.files)

    @staticmethod
    def parse_files(parsed_files: list):
        Runtime.files = []

        for file in parsed_files:
            if os.path.isdir(file):
                Runtime.files.extend(Runtime.get_files_in_dir(file))
            elif not os.path.isfile(file):
                raise ValueError(f"File {file} does not exist")
            elif file.endswith(".acmi"):
                Runtime.files.append(file)

    @staticmethod
    def get_files_in_dir(dir: str):
        files = []

        for file in os.listdir(dir):
            if file.endswith(".acmi"):
                files.append(os.path.join(dir, file))
        return files
