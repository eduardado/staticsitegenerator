import unittest
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_textnodes
from textnode import TextNode, text_type_text, text_type_bold, text_type_italic, text_type_code, text_type_image, text_type_link
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

    def test_split_node_images(self):
        node = TextNode(
            "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
            text_type_text,
                        )   
        new_nodes = split_nodes_image([node])

        self.assertListEqual([
            TextNode("This is text with an ", text_type_text),
            TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and another ", text_type_text),
            TextNode(
                "second image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"
            ),
        ], new_nodes)

    def test_split_node_links(self):
        node = TextNode(
            "This is text with a [link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another [second link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
            text_type_text,
                        )   
        new_nodes = split_nodes_link([node])

        self.assertListEqual([
            TextNode("This is text with a ", text_type_text),
            TextNode("link", text_type_link, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and another ", text_type_text),
            TextNode(
                "second link", text_type_link, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"
            ),
        ], new_nodes)

    def test_text_to_text_nodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertListEqual(nodes, [
            TextNode("This is ", text_type_text),
            TextNode("text", text_type_bold),
            TextNode(" with an ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" word and a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" and an ", text_type_text),
            TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and a ", text_type_text),
            TextNode("link", text_type_link, "https://boot.dev"),
        ])
