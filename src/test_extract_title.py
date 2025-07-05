import unittest

from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test1(self):
        title = extract_title("# Hello")
        self.assertEqual("Hello", title)
    
    def test2(self):
        self.assertRaises(Exception, extract_title, "## Hello")
    
    def test3(self):
        self.assertRaises(Exception, extract_title, "Hello")
    
    def test4(self):
        self.assertRaises(Exception, extract_title, "#Hello")
    
    def test5(self):
        title = extract_title("""# Tolkien Fan Club

![JRR Tolkien sitting](/images/tolkien.png)

Here's the deal, **I like Tolkien**.""")
        self.assertEqual(title, "Tolkien Fan Club")


if __name__ == "__main__":
    unittest.main()