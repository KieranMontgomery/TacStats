import json
import os
import pathlib
import unittest
import unittest.mock as mock
from unittest.mock import patch

from src.file.reader import FileReader


class TestFileReader(unittest.TestCase):
    def setUp(self):
        self.filename = "test_file.txt"
        self.file_contents = "This is a test file.\nIt has multiple lines.\n"
        self.reader = FileReader(self.filename)

    def test_init(self):
        self.assertEqual(self.reader.metadata.filename, self.filename)

    def test_read(self):
        with patch(
            "builtins.open", mock.mock_open(read_data=self.file_contents)
        ) as mock_file:
            self.reader.read()
            mock_file.assert_called_once_with(self.filename, "r", encoding="utf-8-sig")

    def test_fixtures(self):
        for os_file in os.listdir("tests/file/fixtures"):
            fixture_path = (
                pathlib.Path(__file__).parent.parent.parent
                / "tests/file/fixtures/"
                / os_file
            )

            with open(fixture_path, "r") as file:
                fixture = json.load(file)

            with patch("builtins.open", mock.mock_open(read_data=fixture["input"])):
                reader = FileReader(fixture_path)
                reader.read()

                # Check metadata
                self.assertIsNotNone(reader.metadata)
                self.assertIsNotNone(
                    reader.metadata.file_type
                )  # All files have a file type
                self.assertIsNotNone(
                    reader.metadata.file_version
                )  # All files have a file version

                for key, value in reader.metadata.to_dict().items():
                    expected = fixture["output"]["metadata"][key]
                    self.assertEqual(
                        value,
                        expected,
                        msg=f"\nKey: {key}\nActual: {value}\nExpected: {expected}\n",
                    )
