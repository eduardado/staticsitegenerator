import unittest

from textnode import TextNode
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("This is a text node", text_type_bold)
        self.assertEqual(node, node2)

    def test_link_with_url(self):
        node = TextNode("Responsive web design portfolio", text_type_link, "https://eduardado.github.io/")
        self.assertEqual(node.text, "Responsive web design portfolio")
        self.assertEqual(node.text_type, text_type_link)
        self.assertEqual(node.url, "https://eduardado.github.io/")

    def test_link_type_without_url(self):
        node = TextNode("Responsive web design portfolio", text_type_link)
        self.assertEqual(node.text, "Responsive web design portfolio")
        self.assertEqual(node.text_type, text_type_link)
        self.assertIsNone(node.url)

    def test_text_type_different(self):
        node = TextNode("Responsive web design portfolio", text_type_link)
        node2 = TextNode("Responsive web design portfolio", text_type_italic)
        self.assertNotEqual(node, node2)



if __name__ == "__main__":
    unittest.main()
