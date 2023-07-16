from src.file.metadata import Metadata
import unittest


class TestMetadata(unittest.TestCase):
    def setUp(self):
        self.filename = "test_file.txt"
        self.metadata = Metadata(self.filename)

    def test_init(self):
        self.assertEqual(self.metadata.filename, self.filename)

    def test_add_string(self):
        self.metadata.add("FileType = TestFile")
        self.metadata.add("FileVersion = 1.0")
        self.assertEqual(self.metadata.file_type, "TestFile")
        self.assertEqual(self.metadata.file_version, "1.0")

    def test_add_list(self):
        self.metadata.add(["FileType = TestFile", "FileVersion = 1.0"])
        self.assertEqual(self.metadata.file_type, "TestFile")
        self.assertEqual(self.metadata.file_version, "1.0")

    def test_repr(self):
        self.assertEqual(repr(self.metadata), "Metadata(test_file.txt)")
