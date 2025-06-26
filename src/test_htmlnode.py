import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq1(self):
        node = HTMLNode()
        node1 = HTMLNode()
        self.assertEqual(node, node1)
    
    def test_eq2(self):
        node = HTMLNode()
        node1 = HTMLNode("<p>")
        self.assertNotEqual(node, node1)
    
    def test_eq3(self):
        node = HTMLNode("<p>")
        node1 = HTMLNode(tag="<p>")
        self.assertEqual(node, node1)
    
    def test_props_to_html(self):
        node2 = HTMLNode(props={"href": "https://www.google.com", "target": "_blank",})
        result = " href=\"https://www.google.com\" target=\"_blank\""
        self.assertEqual(node2.props_to_html(), result)


if __name__ == "__main__":
    unittest.main()