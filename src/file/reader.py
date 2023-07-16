import hashlib
import json
import pathlib

from setup.runtime import Runtime
from utils.logger import logger

from .metadata import Metadata


class FileReader:
    def __init__(self, filename):
        logger.debug(f"Creating FileReader for {filename}")
        self.metadata = Metadata(filename)

    def read(self):
        logger.debug(f"Reading {self.metadata.filename}")
        with open(self.metadata.filename, "r", encoding="utf-8-sig") as file:
            file = file.read()
            self.hash = hashlib.sha256(file.encode("utf-8")).hexdigest()

        for line in file.split("\n"):
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
        if line.startswith("0,") or any(
            line.startswith(element) for element in ["FileType", "FileVersion"]
        ):  # Metadata
            self.metadata.add(line)

    def to_dict(self):
        return {
            key: value
            for key, value in self.__dict__.items()
            if key not in ["metadata"]
        }
