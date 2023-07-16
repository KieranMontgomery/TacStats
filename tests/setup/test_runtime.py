import unittest
import unittest.mock as mock

from src.setup.runtime import Runtime


class TestRuntime(unittest.TestCase):
    def test_parse_files_acmi(self):
        with mock.patch("os.path.isdir") as mock_isdir, mock.patch(
            "os.path.isfile"
        ) as mock_isfile:
            mock_isdir.return_value = False
            mock_isfile.return_value = True

            Runtime.parse_files(["test.acmi"])
            self.assertEqual(Runtime.files, ["test.acmi"])

    def test_parse_files_dir(self):
        with mock.patch("os.listdir") as mock_listdir, mock.patch(
            "os.path.isdir"
        ) as mock_isdir, mock.patch("os.path.isfile") as mock_isfile:
            mock_isdir.return_value = True
            mock_isfile.return_value = False
            mock_listdir.return_value = ["test.acmi"]

            Runtime.parse_files(["test"])
            self.assertEqual(Runtime.files, ["test/test.acmi"])

    def test_parse_files_invalid(self):
        with mock.patch("os.path.isdir") as mock_isdir, mock.patch(
            "os.path.isfile"
        ) as mock_isfile:
            mock_isdir.return_value = False
            mock_isfile.return_value = False

            with self.assertRaises(ValueError):
                Runtime.parse_files(["test"])

    def test_parse_files_multiple(self):
        with mock.patch("os.listdir") as mock_listdir, mock.patch(
            "os.path.isdir"
        ) as mock_isdir, mock.patch("os.path.isfile") as mock_isfile:
            mock_isdir.return_value = True
            mock_isfile.return_value = False
            mock_listdir.return_value = ["test.acmi", "test2.acmi"]

            Runtime.parse_files(["test"])
            self.assertEqual(Runtime.files, ["test/test.acmi", "test/test2.acmi"])
