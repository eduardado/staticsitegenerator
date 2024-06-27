from textnode import TextNode
from copystatic import copy_files_recursively
import os
import shutil

# variables to store the relative path of static and public directories from the main directory of the project
dir_path_static = "./static"
dir_path_public = "./public"

def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursively(dir_path_static, dir_path_public)

main()
