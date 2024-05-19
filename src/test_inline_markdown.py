import unittest
from inline_markdown import split_nodes_delimiter
from textnode import TextNode, text_type_text, text_type_bold, text_type_italic, text_type_code

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

    def test_delimiter_bold_double_multiword(self):
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
