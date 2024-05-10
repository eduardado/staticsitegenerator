import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    
    def test_boot_case(self):
        bold = LeafNode("Bold text", "b")
        normal = LeafNode("Normal text", None)
        italic = LeafNode("Italic text", "i")
        normal2 = LeafNode("Normal text", None)
        parent = ParentNode([bold, normal, italic, normal2], "p", None)

        self.assertEqual(parent.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

