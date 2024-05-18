import unittest

from leafnode import LeafNode
from textnode import TextNode
from nodeconverter import NodeConverter
from texttype import TextType
import re

class TestNodeConverter(unittest.TestCase):

    def setUp(self):
        self.nodeconverter = NodeConverter()

    def test_text_leaf_node(self):
        text_node = TextNode("This is a text node without tags", TextType.TEXT)
        leafNode = self.nodeconverter.text_node_to_html_node(text_node)
        self.assertIsInstance(leafNode, LeafNode,"The converted object should be a LeafNode.")
        self.assertEqual(leafNode.value, "This is a text node without tags", "The text content should match the input.")
        if hasattr(leafNode, 'tag'):
            self.assertIsNone(leafNode.tag, "The LeafNode for a TEXT type should not have an HTML tag.")

    def test_bold(self):
        text_node = TextNode("Bold", TextType.BOLD)
        leaf_node = self.nodeconverter.text_node_to_html_node(text_node)
        self.assertIsInstance(leaf_node, LeafNode, "LeafNode object expected")
        self.assertEqual(leaf_node.value, "Bold", "The value content should be 'Bold'.")
        self.assertEqual(leaf_node.tag, "b")

    def test_italic(self):
        text_node = TextNode("Italic", TextType.ITALIC)
        leaf_node = self.nodeconverter.text_node_to_html_node(text_node)
        self.assertIsInstance(leaf_node, LeafNode, "LeafNode object expected")
        self.assertEqual(leaf_node.value, "Italic", "The value content should be 'Italic'.")
        self.assertEqual(leaf_node.tag, "i")

    def test_code(self):
        text_node = TextNode("Code", TextType.CODE)
        leaf_node = self.nodeconverter.text_node_to_html_node(text_node)
        self.assertIsInstance(leaf_node, LeafNode, "LeafNode object expected")
        self.assertEqual(leaf_node.value, "Code", "The value content should be 'Code'.")
        self.assertEqual(leaf_node.tag, "code")

    def test_link(self):
        text_node = TextNode("Link", TextType.LINK, "https://eduardado.github.io/")
        leaf_node = self.nodeconverter.text_node_to_html_node(text_node)
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
        leaf_node = self.nodeconverter.text_node_to_html_node(text_node)
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
            self.nodeconverter.text_node_to_html_node("not a text_node")

    def test_unhandled_text_type(self):
        with self.assertRaisesRegex(ValueError, "Text Type not valid"):
            text_node = TextNode("Link", "blas", "https://eduardado.github.io/")
            leaf_node = self.nodeconverter.text_node_to_html_node(text_node)

    def test_basic_splitting(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = self.nodeconverter.split_nodes_delimiter([node],  TextType.CODE)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "This is text with a ")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text, "code block")
        self.assertEqual(new_nodes[1].text_type, TextType.CODE)
        self.assertEqual(new_nodes[2].text, " word")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)

    def test_no_delimiters_present(self):
        node = TextNode("Plain text", TextType.TEXT)
        new_nodes = self.nodeconverter.split_nodes_delimiter([node],  TextType.CODE)
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0], node)
        self.assertEqual(new_nodes[0].text, "Plain text")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
    
    def test_multiple_same_delimiters(self):
        node = TextNode("This is text with a `code block` word and another `code block` word.", TextType.TEXT)
        new_nodes = self.nodeconverter.split_nodes_delimiter([node],  TextType.CODE)
        self.assertEqual(len(new_nodes), 5)
        self.assertEqual(new_nodes[0].text, "This is text with a ")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text, "code block")
        self.assertEqual(new_nodes[1].text_type, TextType.CODE)
        self.assertEqual(new_nodes[2].text, " word and another ")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[3].text, "code block")
        self.assertEqual(new_nodes[3].text_type, TextType.CODE)
        self.assertEqual(new_nodes[4].text, " word.")
        self.assertEqual(new_nodes[4].text_type, TextType.TEXT)

    def test_multiple_different_delimiters(self):
        node = TextNode("This is text with a `code block` word and a **bold** word and an *italic* word.", TextType.TEXT)
        new_nodes = self.nodeconverter.split_nodes_delimiter([node],  TextType.CODE)
        new_nodes = self.nodeconverter.split_nodes_delimiter(new_nodes,  TextType.BOLD)
        new_nodes = self.nodeconverter.split_nodes_delimiter(new_nodes,  TextType.ITALIC)

        expected_outputs = [
            ("This is text with a ", TextType.TEXT),
            ("code block", TextType.CODE),
            (" word and a ", TextType.TEXT),
            ("bold", TextType.BOLD),
            (" word and an ", TextType.TEXT),
            ("italic", TextType.ITALIC),
            (" word.", TextType.TEXT)
        ]
        self.assertEqual(len(new_nodes), len(expected_outputs), "Incorrect number of nodes expected")

        for i, (expected_text, expected_type) in enumerate(expected_outputs):
            self.assertEqual(new_nodes[i].text, expected_text, f"Node {i} text doesn not match.")
            self.assertEqual(new_nodes[i].text_type, expected_type, f"Node {i} type doesn not match.")

    def test_consecutive_delimiters(self):
        node = TextNode("text**bold******", TextType.TEXT)
        new_nodes = self.nodeconverter.split_nodes_delimiter([node],  TextType.BOLD)

        expected_outputs = [
            ("text", TextType.TEXT),
            ("bold", TextType.BOLD)
        ]

        for i ,(expected_text, expected_type) in enumerate(expected_outputs):
            self.assertEqual(new_nodes[i].text, expected_text, f"Node {i} text doesn not match.")
            self.assertEqual(new_nodes[i].text_type, expected_type, f"Node {i} type doesn not match.")

    def test_delimiter_at_end(self):
        node = TextNode("delimiter at end**", TextType.TEXT)
        new_nodes = self.nodeconverter.split_nodes_delimiter([node],  TextType.BOLD)
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0].text, "delimiter at end")

    def test_delimiter_at_start(self):
        node = TextNode("**delimiter at start", TextType.TEXT)
        new_nodes = self.nodeconverter.split_nodes_delimiter([node],  TextType.BOLD)
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0].text, "delimiter at start")

    def test_non_process_of_non_text_nodes(self):
        node = TextNode("*italic* but bold", TextType.BOLD)
        new_nodes = self.nodeconverter.split_nodes_delimiter([node],  TextType.BOLD)
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(node, new_nodes[0])

    def test_invalid_input_split_nodes_delimiter(self):
        with self.assertRaises(ValueError, msg="text_type cannot be None"):
            node = TextNode("This is text with a `code block` word and a **bold** word and an *italic* word.", TextType.TEXT)
            self.nodeconverter.split_nodes_delimiter([node], None)

        with self.assertRaises(ValueError, msg="old_nodes cannot be None"):
            self.nodeconverter.split_nodes_delimiter(None, TextType.BOLD)

        new_nodes = self.nodeconverter.split_nodes_delimiter([], TextType.BOLD)
        self.assertEqual(new_nodes, [], "The function should return and empty list if given and empty list of nodes")
        
    def test_nested_markdown(self):
        with self.assertRaises(ValueError, msg="The application does not support nested Markdown"):
            node = TextNode("*Italic **and bold** text*", TextType.TEXT)
            old_nodes = [node]
            new_nodes = self.nodeconverter.split_nodes_delimiter(old_nodes, TextType.ITALIC)

    def test_images_extraction(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        images = self.nodeconverter.extract_markdown_images(text)
        self.assertEqual(images, [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")])

    def test_links_extraction(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        links = self.nodeconverter.extract_markdown_links(text)
        self.assertEqual(links, [("link", "https://www.example.com"), ("another", "https://www.example.com/another")])


