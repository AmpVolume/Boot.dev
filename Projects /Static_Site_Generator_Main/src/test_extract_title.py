import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_simple_title(self):
        self.assertEqual(extract_title("# Hello"), "Hello")

    def test_with_whitespace(self):
        self.assertEqual(extract_title("   #   Title Here   "), "Title Here")

    def test_missing_title(self):
        with self.assertRaises(Exception):
            extract_title("## Not an h1\nSome text")

if __name__ == "__main__":
    unittest.main()
