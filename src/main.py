from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
import text_to_html

def main():
    text_node = TextNode("funny haha", TextType.PLAIN_TEXT.value)
    print(text_node)

main()