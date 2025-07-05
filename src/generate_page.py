from raw_md_to_htmlnodes import markdown_to_html_node
from htmlnode import HTMLNode, ParentNode, LeafNode
from extract_title import extract_title
import os

def generate_page(from_path, template_path, dest_path):
    from_file = open(from_path, "r")
    from_content = from_file.read()

    template_file = open(template_path, "r")
    template_content = template_file.read()

    title = extract_title(from_content)
    content = markdown_to_html_node(from_content).to_html()

    template_content = template_content.replace("{{ Title }}", title).replace("{{ Content }}", content)

    if os.path.exists(dest_path):
        dest_file = open(dest_path, "w")
    else:
        dest_file = open(dest_path, "x")
    dest_file.write(template_content)
    
    dest_file.close()
    from_file.close()
    template_file.close()
