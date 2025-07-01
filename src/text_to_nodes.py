from textnode import TextType, TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            split = node.text.split(delimiter)
            for i in range(len(split)):
                if i % 2 == 1:
                    new_nodes.append(TextNode(split[i], text_type))
                elif split[i] != "":
                    new_nodes.append(TextNode(split[i], TextType.TEXT))
        else:
            new_nodes.append(node)
    return new_nodes