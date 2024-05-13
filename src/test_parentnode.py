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

        self.assertEqual(parent.to_html(), "<p><b>Bold text</b>Normal text<i>Italic text</i>Normal text</p>")

    def test_parent_without_children(self):
        with self.assertRaisesRegex(ValueError, "Parent nodes need children"):
            parent = ParentNode(None, "p", None)
            parent.to_html()

    def test_parent_without_tag(self):
        with self.assertRaisesRegex(ValueError, "Parent nodes need a tag"):
            bold = LeafNode("Bold text", "b")
            normal = LeafNode("Normal text", None)
            italic = LeafNode("Italic text", "i")
            normal2 = LeafNode("Normal text", None)
            parent = ParentNode([bold, normal, italic, normal2], None, None)
            parent.to_html()

    def test_parent_without_single_leaf_node(self):
        bold = LeafNode("Bold text", "b")
        parent = ParentNode([bold], "p", None)
        self.assertEqual(parent.to_html(), "<p><b>Bold text</b></p>")

    def test_parent_without_single_parent_node(self):
        bold = LeafNode("Bold text", "b")
        bold = ParentNode([bold], "b")
        parent = ParentNode([bold], "p", None)
        self.assertEqual(parent.to_html(), "<p><b><b>Bold text</b></b></p>")

    def test_parent_mix_parent_and_leaf_nodes(self):
        bold = LeafNode("Bold text", "b")
        parent_bold = ParentNode([bold], "b")

        italic = LeafNode("Italic text", "i")
        
        parent = ParentNode([parent_bold, italic], "p", None)
        self.assertEqual(parent.to_html(), "<p><b><b>Bold text</b></b><i>Italic text</i></p>")

    def test_performance_multiple_nested_children(self):
        children = [LeafNode(f"item{i}", "li") for i in range(1, 1000)]
        parent = ParentNode(children, "ul")
        parent.to_html()