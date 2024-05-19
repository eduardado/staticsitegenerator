from textnode import TextNode, text_type_text, text_type_bold, text_type_italic, text_type_code, text_type_image, text_type_link
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node) 
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    pattern = r"\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        matches = extract_markdown_images(old_node.text)
        if len(matches) == 0:
            new_nodes.append(old_node)
            continue
        else:
            tail = ""
            for match in matches:
                if tail:
                    sections = tail.split(f"![{match[0]}]({match[1]})")
                else:
                    sections = old_node.text.split(f"![{match[0]}]({match[1]})")
                new_nodes.append(TextNode(sections.pop(0), text_type_text))
                new_nodes.append(TextNode(match[0], text_type_image, match[1]))
                tail += sections[-1]
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        matches = extract_markdown_links(old_node.text)
        if len(matches) == 0:
            new_nodes.append(old_node)
            continue
        else:
            tail = ""
            for match in matches:
                if tail:
                    sections = tail.split(f"[{match[0]}]({match[1]})")
                else:
                    sections = old_node.text.split(f"[{match[0]}]({match[1]})")
                new_nodes.append(TextNode(sections.pop(0), text_type_text))
                new_nodes.append(TextNode(match[0], text_type_link, match[1]))
                tail += sections[-1]
    return new_nodes
