import re

from textnode import TextType, TextNode
from image_and_link_handling import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        split = re.findall(r"(.*?)!\[(.*?)\]\((.*?)\)", node.text)
        for s in split:
            new_nodes.append(TextNode(s[0], TextType.TEXT))
            new_nodes.append(TextNode(s[1], TextType.IMAGE, s[2]))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        split = re.findall(r"(.*?)\[(.*?)\]\((.*?)\)", node.text)
        for s in split:
            new_nodes.append(TextNode(s[0], TextType.TEXT))
            new_nodes.append(TextNode(s[1], TextType.LINK, s[2]))
    return new_nodes
