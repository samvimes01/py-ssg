import re
import os
from pathlib import Path

from md_to_html import markdown_to_html_node

def extract_title(markdown):
    matches = re.search(r"#\s(?P<head>.+)(\n|$)", markdown)
    if not matches or not "head" in matches.groupdict():
        raise Exception("Invalid markdown: h1 header is required") 
    return matches.groupdict()["head"]

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, 'r') as f:
        markdown = f.read()
    with open(template_path, 'r') as f:
        template = f.read()
    
    root_node = markdown_to_html_node(markdown)
    content = root_node.to_html()
    title = extract_title(markdown)
    html = template.replace("{{ Content }}", content).replace("{{ Title }}", title)

    dest = os.path.dirname(dest_path)
    if dest != "":
        os.makedirs(dest, exist_ok=True)
    
    # dest = dest_path.split("/")
    # f = os.makedirs(name=dest[:-1], exist_ok=True)

    f = open(dest_path, "w")
    f.write(html)
    f.close()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    dir_list = os.listdir(dir_path_content)
    for file_name in dir_list:
        path_from = os.path.join(dir_path_content, file_name)
        path_to = os.path.join(dest_dir_path, file_name)
        if os.path.isfile(path_from):
            path_to = Path(path_to).with_suffix(".html")
            generate_page(path_from, template_path, path_to)
        elif os.path.isdir(path_from):
            generate_pages_recursive(path_from, template_path, path_to)
