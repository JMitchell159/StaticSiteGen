import re

from textnode import TextType, TextNode

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            if "![" in node.text:
                i = 0
                temp = node.text
                while i != 1:
                    split = re.findall(r"(.*?)!\[(.*?)\]\((.*?)\)(.*)", temp)
                    new_nodes.append(TextNode(split[0][0], TextType.TEXT))
                    new_nodes.append(TextNode(split[0][1], TextType.IMAGE, split[0][2]))
                    if "![" not in split[0][3] and split[0][3] != "":
                        i = 1
                        new_nodes.append(TextNode(split[0][3], TextType.TEXT))
                    elif split[0][3] != "":
                        temp = split[0][3]
                    else:
                        i = 1
            else:
                new_nodes.append(node)
        else:
            new_nodes.append(node)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            if "[" in node.text:
                i = 0
                temp = node.text
                while i != 1:
                    split = re.findall(r"(.*?)\[(.*?)\]\((.*?)\)(.*)", temp)
                    new_nodes.append(TextNode(split[0][0], TextType.TEXT))
                    new_nodes.append(TextNode(split[0][1], TextType.LINK, split[0][2]))
                    if "[" not in split[0][3] and split[0][3] != "":
                        i = 1
                        new_nodes.append(TextNode(split[0][3], TextType.TEXT))
                    elif split[0][3] != "":
                        temp = split[0][3]
                    else:
                        i = 1
            else:
                new_nodes.append(node)
        else:
            new_nodes.append(node)
    return new_nodes
