import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_paragraph(self):
        leaf = LeafNode("Blas", "p")
        self.assertEqual(leaf.to_html(), "<p>Blas</p>")

    def test_no_tag(self):
        leaf = LeafNode("No tag test")
        self.assertEqual(leaf.to_html(), "No tag test")

    def test_no_value(self):
        with self.assertRaises(ValueError):
            leaf = LeafNode(None)
            leaf.to_html()

    def test_link(self):
        leaf = LeafNode("Click me!", "a", {"href": "https://www.google.com"})
        self.assertEqual(leaf.to_html(),'<a href="https://www.google.com">Click me!</a>')

    def test_link_multiple_attributes(self):
        leaf = LeafNode("Click me!", "a", {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(leaf.to_html(),'<a href="https://www.google.com" target="_blank">Click me!</a>')
