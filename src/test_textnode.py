import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq1(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node1 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node1)
    
    def test_eq2(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node1 = TextNode("funny haha", TextType.ITALIC, "https://www.youtube.com")
        self.assertNotEqual(node, node1)
    
    def test_eq3(self):
        node = TextNode("funny haha", TextType.ITALIC, "https://www.youtube.com")
        node1 = TextNode("funny haha", TextType.ITALIC, url="https://www.youtube.com")
        self.assertEqual(node, node1)

if __name__ == "__main__":
    unittest.main()