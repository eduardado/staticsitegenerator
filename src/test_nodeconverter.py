import unittest

from leafnode import LeafNode
from textnode import TextNode
from nodeconverter import NodeConverter
from texttype import TextType

class TestNodeConverter(unittest.TestCase):

    def test_text_leaf_node(self):
        text_node = TextNode("This is a text node without tags", TextType.TEXT)
        node_converter = NodeConverter()
        leafNode = node_converter.text_node_to_html_node(text_node)
        self.assertIsInstance(leafNode, LeafNode,"The converted object should be a LeafNode.")
        self.assertEqual(leafNode.value, "This is a text node without tags", "The text content should match the input.")
        if hasattr(leafNode, 'tag'):
            self.assertIsNone(leafNode.tag, "The LeafNode for a TEXT type should not have an HTML tag.")

    def test_bold(self):
        text_node = TextNode("Bold", TextType.BOLD)
        converter = NodeConverter()
        leaf_node = converter.text_node_to_html_node(text_node)
        self.assertIsInstance(leaf_node, LeafNode, "LeafNode object expected")
        self.assertEqual(leaf_node.value, "Bold", "The value content should be 'Bold'.")
        self.assertEqual(leaf_node.tag, "b")

    def test_italic(self):
        text_node = TextNode("Italic", TextType.ITALIC)
        converter = NodeConverter()
        leaf_node = converter.text_node_to_html_node(text_node)
        self.assertIsInstance(leaf_node, LeafNode, "LeafNode object expected")
        self.assertEqual(leaf_node.value, "Italic", "The value content should be 'Italic'.")
        self.assertEqual(leaf_node.tag, "i")

    def test_code(self):
        text_node = TextNode("Code", TextType.CODE)
        converter = NodeConverter()
        leaf_node = converter.text_node_to_html_node(text_node)
        self.assertIsInstance(leaf_node, LeafNode, "LeafNode object expected")
        self.assertEqual(leaf_node.value, "Code", "The value content should be 'Code'.")
        self.assertEqual(leaf_node.tag, "code")

    def test_link(self):
        text_node = TextNode("Link", TextType.LINK, "https://eduardado.github.io/")
        converter = NodeConverter()
        leaf_node = converter.text_node_to_html_node(text_node)
        self.assertIsInstance(leaf_node, LeafNode, "LeafNode object expected")
        self.assertEqual(leaf_node.value, "Link", "The value content should be 'Link'.")
        self.assertEqual(leaf_node.tag, "a")
        self.assertIn('href', leaf_node.props, "'href' should be a key in the leafNode's props")
        expected_href_value = "https://eduardado.github.io/"
        self.assertEqual(leaf_node.props['href'], expected_href_value, f"The 'href' value should be {expected_href_value}")
        self.assertEqual(leaf_node.tag, "a")

    def test_image(self):
        image_source = "https://eduardado.github.io/image"
        text_node = TextNode("Image", TextType.IMAGE, image_source)
        converter = NodeConverter()
        leaf_node = converter.text_node_to_html_node(text_node)
        self.assertIsInstance(leaf_node, LeafNode, "LeafNode object expected")
        self.assertEqual(leaf_node.value, "", "The value content should be an empty string.")
        self.assertEqual(leaf_node.tag, "img")
        self.assertIn('alt', leaf_node.props, "'alt' should be a key in the leafNode's props when it is an image node")
        generic_alt_attribute = "Image description not available"
        self.assertEqual(leaf_node.props['alt'], generic_alt_attribute, f"The 'href' value should be {generic_alt_attribute}")
        self.assertIn('src', leaf_node.props, "'src' should be a key in the leafNode's props when it is an image node")
        self.assertEqual(leaf_node.props['src'], image_source, f"The 'src' value should be {image_source}")

    def test_type_validation(self):
        with self.assertRaisesRegex(TypeError, "Expected a TextNode object"):
            converter = NodeConverter()
            converter.text_node_to_html_node("not a text_node")

    def test_unhandled_text_type(self):
        with self.assertRaisesRegex(ValueError, "Text Type not valid"):
            text_node = TextNode("Link", "blas", "https://eduardado.github.io/")
            converter = NodeConverter()
            leaf_node = converter.text_node_to_html_node(text_node)



