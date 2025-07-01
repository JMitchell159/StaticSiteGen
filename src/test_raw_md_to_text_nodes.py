import unittest

from raw_md_to_text_nodes import text_to_textnodes
from textnode import TextType, TextNode

class TestRawMDToTextNodes(unittest.TestCase):
    def test1(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        result = [TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),]
        self.assertListEqual(result, nodes)
    
    def test2(self):
        text = "This is `code` with **text** and an _italic_ word and a [link](https://boot.dev) and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)"
        nodes = text_to_textnodes(text)
        result = [TextNode("This is ", TextType.TEXT),
                  TextNode("code", TextType.CODE),
                  TextNode(" with ", TextType.TEXT),
                  TextNode("text", TextType.BOLD),
                  TextNode(" and an ", TextType.TEXT),
                  TextNode("italic", TextType.ITALIC),
                  TextNode(" word and a ", TextType.TEXT),
                  TextNode("link", TextType.LINK, "https://boot.dev"),
                  TextNode(" and an ", TextType.TEXT),
                  TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),]
        self.assertListEqual(result, nodes)


if __name__ == "__main__":
    unittest.main()