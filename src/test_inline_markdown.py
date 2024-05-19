import unittest
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links
from textnode import TextNode, text_type_text, text_type_bold, text_type_italic, text_type_code
import re

class TestInlineMarkdown(unittest.TestCase):
    def test_delimiter_bold(self):
        node = TextNode("I **love** ramen.", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("I ", text_type_text),
                TextNode("love", text_type_bold),
                TextNode(" ramen.", text_type_text),
            ],
            new_nodes
        )

    def test_delimiter_bold_double(self):
        node = TextNode("I **love** ramen. **Especially** if I contribute on the making.", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("I ", text_type_text),
                TextNode("love", text_type_bold),
                TextNode(" ramen. ", text_type_text),
                TextNode("Especially", text_type_bold),
                TextNode(" if I contribute on the making.", text_type_text),
            ],
            new_nodes
        )

    def test_delimiter_bold_double_multiword(self):
        node = TextNode("I **really love** ramen. **Especially if** I contribute on the making.", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("I ", text_type_text),
                TextNode("really love", text_type_bold),
                TextNode(" ramen. ", text_type_text),
                TextNode("Especially if", text_type_bold),
                TextNode(" I contribute on the making.", text_type_text),
            ],
            new_nodes
        )

    def test_delimiter_bold_double_multiword_italic(self):
        node = TextNode("I *really love* ramen. *Especially if* I contribute on the making.", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("I ", text_type_text),
                TextNode("really love", text_type_italic),
                TextNode(" ramen. ", text_type_text),
                TextNode("Especially if", text_type_italic),
                TextNode(" I contribute on the making.", text_type_text),
            ],
            new_nodes
        )

    def test_extract_markdown_images(self):
        matches = extract_markdown_images("This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)")
        self.assertListEqual(matches, [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")])

    def test_extract_markdown_links(self):
        matches = extract_markdown_links("This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)")
        self.assertListEqual(matches, [("link", "https://www.example.com"), ("another", "https://www.example.com/another")])