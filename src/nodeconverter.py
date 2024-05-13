from textnode import TextNode
from texttype import TextType
from leafnode import LeafNode


class NodeConverter:

    text_type_to_tag = {
        TextType.TEXT: None,
        TextType.BOLD: "b",
        TextType.ITALIC: "i",
        TextType.CODE: "code",
        TextType.LINK: "a",
        TextType.IMAGE: "img"
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
        
