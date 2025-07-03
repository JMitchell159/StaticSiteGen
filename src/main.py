from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
import text_to_html
import os
import shutil

def main():
    workspace_path = "/home/joemi/workspace/github.com/JMitchell159/StaticSiteGen"
    shutil.rmtree(f"{workspace_path}/public")
    shutil.copytree(f"{workspace_path}/static", f"{workspace_path}/public")


if __name__ == "__main__":
    main()