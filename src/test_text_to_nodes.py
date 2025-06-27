import unittest

from text_to_nodes import split_nodes_delimiter
from textnode import TextType, TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestTextToNodes(unittest.TestCase):
    def test1(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        result = [TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),]
        self.assertEqual(new_nodes, result)
    
    def test2(self):
        node = TextNode("This is text with a **bolded phrase** in the middle", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        result = [TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded phrase", TextType.BOLD),
                TextNode(" in the middle", TextType.TEXT),]
        self.assertEqual(new_nodes, result)


if __name__ == "__main__":
    unittest.main()
