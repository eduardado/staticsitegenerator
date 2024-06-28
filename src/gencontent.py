from markdown_blocks import markdown_to_html_node
import os

def generate_page(from_path, template_path, dest_path):
    print(f" * {from_path} {dest_path} -> {template_path}")

    from_file  = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path)
    template = template_file.read()
    template_file.close

    html_node = markdown_to_html_node(markdown_content)
    html = html_node.to_html()

    title = extract_title(markdown_content)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)

    to_file = open(dest_path, "w")
    to_file.write(template)
    to_file.close()

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        stripped_line = line.strip()
        if stripped_line.startswith("# "):
            return stripped_line[2:]
    raise ValueError("Not title found")


