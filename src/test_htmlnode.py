import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_eq1(self):
        node = HTMLNode()
        node1 = HTMLNode()
        self.assertEqual(node, node1)
    
    def test_eq2(self):
        node = HTMLNode()
        node1 = HTMLNode("p")
        self.assertNotEqual(node, node1)
    
    def test_eq3(self):
        node = HTMLNode("p")
        node1 = HTMLNode(tag="p")
        self.assertEqual(node, node1)
    
    def test_props_to_html1(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank",})
        result = " href=\"https://www.google.com\" target=\"_blank\""
        self.assertEqual(node.props_to_html(), result)
    
    def test_props_to_html2(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")
    
    def test_to_html1(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")
    
    def test_to_html2(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")
    
    def test_to_html3(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")


if __name__ == "__main__":
    unittest.main()