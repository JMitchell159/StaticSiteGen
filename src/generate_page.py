from raw_md_to_htmlnodes import markdown_to_html_node
from htmlnode import HTMLNode, ParentNode, LeafNode
from extract_title import extract_title
import os
import shutil

def generate_page(from_path, template_path, dest_path, basepath):
    from_file = open(from_path, "r")
    from_content = from_file.read()

    template_file = open(template_path, "r")
    template_content = template_file.read()

    title = extract_title(from_content)
    content = markdown_to_html_node(from_content).to_html()

    template_content = template_content.replace("{{ Title }}", title).replace("{{ Content }}", content).replace("href=\"/", f"href=\"{basepath}").replace("src=\"/", f"src=\"{basepath}")

    temp_list = dest_path.split("/")
    removed = []
    while not os.path.exists("/".join(temp_list)):
        removed.append(temp_list[-1])
        temp_list = temp_list[:-1]
    
    temp_path = "/".join(temp_list)
    
    if len(removed) > 0:
        for r in reversed(removed):
            temp_path += f"/{r}"
            if r == removed[0]:
                dest_file = open(temp_path, "x")
            else:
                os.mkdir(temp_path)
    else:
        dest_file = open(temp_path, "w")
    
    dest_file.write(template_content)
    
    dest_file.close()
    from_file.close()
    template_file.close()
