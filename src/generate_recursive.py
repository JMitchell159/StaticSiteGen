from generate_page import generate_page
import os

def list_files_recursive(dir):
    dir_list = os.listdir(dir)
    files = []
    for dorf in dir_list:
        if os.path.isfile(f"{dir}/{dorf}"):
            files.append(dorf)
        else:
            inner_files = list_files_recursive(f"{dir}/{dorf}")
            for f in inner_files:
                files.append(f"{dorf}/{f}")
    return files

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    md_files = list_files_recursive(dir_path_content)
    for md in md_files:
        generate_page(f"{dir_path_content}/{md}", template_path, f"{dest_dir_path}/{md[:-3]}.html", basepath)
