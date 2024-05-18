import unittest

from textnode import TextNode
from texttype import TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_link_with_url(self):
        node = TextNode("Responsive web design portfolio", TextType.LINK, "https://eduardado.github.io/")
        self.assertEqual(node.text, "Responsive web design portfolio")
        self.assertEqual(node.text_type, TextType.LINK)
        self.assertEqual(node.url, "https://eduardado.github.io/")

    def test_link_type_without_url(self):
        node = TextNode("Responsive web design portfolio", TextType.LINK)
        self.assertEqual(node.text, "Responsive web design portfolio")
        self.assertEqual(node.text_type, TextType.LINK)
        self.assertIsNone(node.url)

    def test_text_type_different(self):
        node = TextNode("Responsive web design portfolio", TextType.LINK)
        node2 = TextNode("Responsive web design portfolio", TextType.ITALIC)
        self.assertNotEqual(node, node2)



if __name__ == "__main__":
    unittest.main()
