import os
import shutil

def copy_static_to_public():
    src_path = "static"
    dst_path = "public"
    
    print(f"copy_static_to_public_to_public_to_public() - Copying the content from:{src_path} to:{dst_path}")

    if not os.path.exists(src_path):
        raise ValueError(f"The directory: {src_path} does not exists")
    if not os.path.isdir(src_path):
        raise ValueError(f"The path specified{src_path} must be a directory")
    if len(os.listdir(src_path)) == 0:
        raise ValueError(f"The directory{src_path} has no content")
    
    # 1 Making the operation idempotent
    print(f"copy_static_to_public_to_public_to_public() - Deleting the directory {dst_path}")
    if os.path.exists(dst_path):
        shutil.rmtree(dst_path)

    copy_content(src_path, dst_path)
    
def copy_content(src, dst):
    if os.path.isfile(src):
        print(f"copy_content() - Copying file into: {dst}")
        shutil.copy(src, dst)
    if os.path.isdir(src):
        print(f"copy_content() - Creating directory: {dst}")
        os.mkdir(dst)
        content_list = os.listdir(src)
        if len(content_list) > 0 :
            for content in content_list:
                content_src_path = os.path.join(src, content)
                content_dst_path = os.path.join(dst, content)
                copy_content(content_src_path, content_dst_path)