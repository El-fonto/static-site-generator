import unittest
from generate_page import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_extract_single_line(self):
        title = "# Hello"
        extracted = extract_title(title)
        self.assertEqual(extracted, "Hello")

    def test_extract_no_title(self):
        title = "Hello"
        with self.assertRaises(ValueError):
            extract_title(title)

    def test_extract_line_spaces(self):
        title = "    # Hello              "
        extracted = extract_title(title)
        self.assertEqual(extracted, "Hello")
