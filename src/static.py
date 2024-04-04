import os
import shutil

BASE_DIR = os.getcwd()
PUBLIC_DIR = os.path.join(BASE_DIR, 'public')

def copy_static():
    if os.path.exists(PUBLIC_DIR):
        shutil.rmtree(PUBLIC_DIR)
    os.mkdir(PUBLIC_DIR)

    copy_dir("static")

def copy_dir(path_to_dir):
    sub_path = "" if path_to_dir == "static" else path_to_dir
    full_path_to_dir = os.path.join(BASE_DIR, "static", sub_path)
    
    dir_list = os.listdir(full_path_to_dir)
    for name in dir_list:
        path_from = os.path.join(full_path_to_dir, name)
        path_to = os.path.join(PUBLIC_DIR, sub_path, name)
        if os.path.isfile(path_from):
            shutil.copyfile(path_from, path_to)
        elif os.path.isdir(path_from):
            if not os.path.exists(path_to):
                os.mkdir(path_to)
            copy_dir(os.path.join(sub_path, name))