import unittest

from image_and_link_to_node import split_nodes_image, split_nodes_link
from textnode import TextType, TextNode

class TestImageAndLinkToNode(unittest.TestCase):
    def test1(self):
        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT,)
        new_nodes = split_nodes_link([node])
        result = [TextNode("This is text with a link ", TextType.TEXT),
                  TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                  TextNode(" and ", TextType.TEXT),
                  TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),]
        self.assertListEqual(new_nodes, result)
    
    def test2(self):
        node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)", TextType.TEXT,)
        new_nodes = split_nodes_image([node])
        result = [TextNode("This is text with an ", TextType.TEXT),
                  TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                  TextNode(" and another ", TextType.TEXT),
                  TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),]
        self.assertListEqual(new_nodes, result)


if __name__ == "__main__":
    unittest.main()