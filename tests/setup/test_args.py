import unittest

from src.setup.args import parse_args


class TestArgs(unittest.TestCase):
    def test_one_file(self):
        parser = parse_args(["test_file.acmi"])
        self.assertEqual(parser.files, ["test_file.acmi"])

    def test_multiple_files(self):
        parser = parse_args(["test_file.acmi", "test_file2.acmi"])
        self.assertEqual(parser.files, ["test_file.acmi", "test_file2.acmi"])
