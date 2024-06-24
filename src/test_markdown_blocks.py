import unittest
from markdown_blocks import markdown_to_blocks, block_to_block_type, markdown_to_html_node
from markdown_blocks import block_type_paragraph, block_type_heading, block_type_code, block_type_quote, block_type_ulist, block_type_olist, block_type_normal_text

class TestBlockMarkdown(unittest.TestCase):

    def test_markdown_to_blocks(self):
        markdown = """
        This is **bolded** paragraph

        This is another paragraph with *italic* text and `code` here
        This is the same paragraph on a new line

        * This is a list
        * with items
        """

        blocks = markdown_to_blocks(markdown)
        expected_blocks = [
            "This is **bolded** paragraph",
            """This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line""",
            """* This is a list\n* with items""",
            ]
        self.assertListEqual(expected_blocks, blocks)

    def test_block_to_block_type(self):
        block = "# HEADING"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, block_type_heading)

        block = "## HEADING"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, block_type_heading)

        block = "### HEADING"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, block_type_heading)

        block = "#### HEADING"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, block_type_heading)

        block = "##### HEADING"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, block_type_heading)

        block = "###### HEADING"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, block_type_heading)

        block = "####### HEADING"
        block_type = block_to_block_type(block)
        self.assertNotEqual(block_type, block_type_heading)

        block = "#######HEADING"
        block_type = block_to_block_type(block)
        self.assertNotEqual(block_type, block_type_heading)

        block = "####### HEADING"
        block_type = block_to_block_type(block)
        self.assertNotEqual(block_type, block_type_heading)

        block = "```\nCODE\n```"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, block_type_code)

        block = "```CODE"
        block_type = block_to_block_type(block)
        self.assertNotEqual(block_type, block_type_code, "a code block must start and end with 3 backsticks")

        block = ">Quote"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, block_type_quote)

        block = "* potatoes\n* spiders"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, block_type_ulist)

        block = "- potatoes\n- spiders"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, block_type_ulist)

        block = "1. One\n2. Two"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, block_type_olist)

        block = "1 One\n2. Two"
        block_type = block_to_block_type(block)
        self.assertNotEqual(block_type, block_type_olist)

        block = "1. One\n3. Two"
        block_type = block_to_block_type(block)
        self.assertNotEqual(block_type, block_type_olist)

        block = "1. One\n2 Two"
        block_type = block_to_block_type(block)
        self.assertNotEqual(block_type, block_type_olist)

    def test_block_to_block_type_extra(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), block_type_code)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), block_type_quote)
        block = "* list\n* items"
        self.assertEqual(block_to_block_type(block), block_type_ulist)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), block_type_olist)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)
    
    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>")

    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>")

    def test_lists(self):
        md = """
- This is a list
- with items
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><ul><li>This is a list</li><li>with items</li></ul></div>")

    def test_lists(self):
        md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>")

    def test_lists(self):
        md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )
