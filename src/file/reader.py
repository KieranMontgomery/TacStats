from utils.logger import logger
from setup.runtime import Runtime

import pathlib
import hashlib
import json

from .metadata import Metadata


class FileReader:
    def __init__(self, filename):
        logger.debug(f"Creating FileReader for {filename}")
        self.metadata = Metadata(filename)

    def read(self):
        logger.debug(f"Reading {self.metadata.filename}")
        with open(self.metadata.filename, "r") as file:
            file = file.read()
            self.hash = hashlib.sha256(file.encode("utf-8")).hexdigest()

        lines = file.split("\n")

        # First two lines are always required and contain metadata
        self.metadata.add(lines[:2])

        # Read the rest of the file
        for line in lines[2:]:
            self._read_line(line)

        if Runtime.fixture_insert:
            self._insert_fixture(file)

    def _insert_fixture(self, file):
        logger.debug(f"Inserting fixture for {self.hash}")
        file_path = (
            pathlib.Path(__file__).parent.parent.parent
            / "tests/file/fixtures"
            / (self.hash + ".json")
        )
        content = {
            "input": file,
            "output": {
                "metadata": self.metadata.to_dict(),
            },
        }
        with open(file_path, "w") as file:
            json.dump(content, file, indent=4)

    def _read_line(self, line):
        if line.startswith("0,"):  # Metadata
            self.metadata.add(line)

    def to_dict(self):
        return {
            key: value
            for key, value in self.__dict__.items()
            if key not in ["metadata"]
        }
