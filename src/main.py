from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from generate_recursive import generate_pages_recursive
import text_to_html
import os
import shutil
import sys

def main():
    if len(sys.argv) == 2:
        basepath = sys.argv[1]
    elif len(sys.argv) == 1:
        basepath = "/"
    workspace_path = "/home/joemi/workspace/github.com/JMitchell159/StaticSiteGen"
    if os.path.exists(f"{workspace_path}/public/docs"):
        shutil.rmtree(f"{workspace_path}/public/docs")
    else:
        os.mkdir(f"{workspace_path}/public")
        os.mkdir(f"{workspace_path}/public/docs")
    shutil.copytree(f"{workspace_path}/static", f"{workspace_path}/public/docs")
    generate_pages_recursive(f"{workspace_path}/content", f"{workspace_path}/template.html", f"{workspace_path}/public/docs", basepath)


if __name__ == "__main__":
    main()