import re
from typing import Union


class Metadata:
    def __init__(self, filename):
        self.filename = filename

    def add(self, lines: Union[str, list[str]]):
        if isinstance(lines, str):
            lines = [lines]

        for line in lines:
            self._read_line(line)

    def _read_line(self, line):
        if line.startswith("FileType"):
            self.file_type = line.split("=")[1].strip()
        elif line.startswith("FileVersion"):
            self.file_version = line.split("=")[1].strip()
        elif line.startswith("0,"):
            key, value = line.split("=")
            key = "_".join([s.lower() for s in re.findall("[A-Z][^A-Z]*", key)])
            if key not in ["authentication_key", "comments"]:
                setattr(self, key, value.strip())

    def __repr__(self) -> str:
        return f"Metadata({self.filename})"

    def to_dict(self):
        return {
            key: value
            for key, value in self.__dict__.items()
            if key not in ["filename"]
        }
