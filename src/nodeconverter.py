from textnode import TextNode
from texttype import TextType
from leafnode import LeafNode
import re


class NodeConverter:

    text_type_to_tag = {
        TextType.TEXT: None,
        TextType.BOLD: "b",
        TextType.ITALIC: "i",
        TextType.CODE: "code",
        TextType.LINK: "a",
        TextType.IMAGE: "img"
    }

    text_type_delimiters = {
        TextType.ITALIC : "*",
        TextType.BOLD : "**",
        TextType.CODE : "`"
    }

    def text_node_to_html_node(self, text_node):
        if not isinstance(text_node, TextNode):
            raise TypeError("Expected a TextNode object")

        html_tag = self.text_type_to_tag.get(text_node.text_type)
        
        if html_tag is None and text_node.text_type == TextType.TEXT:
            return LeafNode(text_node.text)
        elif html_tag is not None:
            if text_node.text_type == TextType.LINK:
                return LeafNode(text_node.text, html_tag, {"href": text_node.url})
            elif text_node.text_type == TextType.IMAGE:
                return LeafNode("", html_tag, {"src": text_node.url, "alt": "Image description not available"})
            else:
                return LeafNode(text_node.text, html_tag)

        raise ValueError("Text Type not valid")

    def split_nodes_delimiter(self, old_nodes, text_type):

        if old_nodes is None:
            raise ValueError("old_nodes cannot be None")
        if text_type is None:
            raise ValueError("text_type cannot be None")

        if not isinstance(text_type, TextType):
            raise ValueError("Invalid text_type, it must coincide with TextType Enum")
        if text_type not in self.text_type_delimiters:
            raise ValueError("TextType not supported. Does not have delimiters")

        for node in old_nodes:
            if self.has_nested_markdown(node.text):
                raise ValueError("The application does not support nested Markdown", f"{node.text}")

        delimiter = self.text_type_delimiters[text_type]
        new_nodes = []
        for node in old_nodes:
            if node.text_type == TextType.TEXT:
                chunks = node.text.split(delimiter)
                is_styled = False
                for chunk in chunks:
                    if is_styled and delimiter in chunk:
                        raise ValueError(f"Nested delimiter '{delimiter}' found in chunk {chunk}")
                    node_type = text_type if is_styled else TextType.TEXT
                    if chunk: #ignore empty styled chunks
                        new_nodes.append(TextNode(chunk, node_type))
                    is_styled = not is_styled
            else:
                new_nodes.append(node)

        return new_nodes

    import re

    def has_nested_markdown(self, text): # distinguishes consecutive empty markdown from nested
        patterns = [
            r'\*[^*]+\*\*[^*]+\*\*[^*]+\*',  # Italic and bold
            r'\`[^*]+\*[^*]+\*[^*]+\`',      # Code and italic
            r'\`[^*]+\*\*[^*]+\*\*[^*]+\`'   # Code and bold
        ]
        matches = []
        for pattern in patterns:
            matches.extend(re.findall(pattern, text))
        return len(matches) > 0

    def extract_markdown_images(self, text):
        return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

    def extract_markdown_links(self, text):
        return re.findall(r"\[(.*?)\]\((.*?)\)", text)