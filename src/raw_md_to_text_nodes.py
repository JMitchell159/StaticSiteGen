from image_and_link_to_node import split_nodes_link, split_nodes_image
from text_to_nodes import split_nodes_delimiter
from textnode import TextType, TextNode

def text_to_textnodes(text):
    delim_type = [("**", TextType.BOLD), ("_", TextType.ITALIC), ("`", TextType.CODE), ("![", TextType.IMAGE), ("[", TextType.LINK)]
    current_nodes = [TextNode(text, TextType.TEXT),]
    for d in delim_type:
        if '[' not in d[0]:
            current_nodes = split_nodes_delimiter(current_nodes, d[0], d[1])
        elif '!' in d[0]:
            current_nodes = split_nodes_image(current_nodes)
        else:
            current_nodes = split_nodes_link(current_nodes)
    return current_nodes
