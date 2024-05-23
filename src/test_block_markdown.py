import unittest
from block_markdown import markdown_to_blocks, block_to_block_type
from block import block_type_paragraph, block_type_heading, block_type_code, block_type_quote, block_type_unordered_list, block_type_ordered_list, block_type_normal_text

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
        # print(blocks)
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

        # block = "```CODE```"
        # block_type = block_to_block_type(block)
        # self.assertEqual(block_type, block_type_code)

        # block = "```CODE"
        # block_type = block_to_block_type(block)
        # self.assertNotEqual(block_type, block_type_code, "a code block must start and end with 3 backsticks")

        # block = ">Quote"
        # block_type = block_to_block_type(block)
        # self.assertEqual(block_type, block_type_quote)

        # block = "* potatoes\n* spiders"
        # block_type = block_to_block_type(block)
        # self.assertEqual(block_type, block_type_unordered_list)

        # block = "- potatoes\n- spiders"
        # block_type = block_to_block_type(block)
        # self.assertEqual(block_type, block_type_unordered_list)

        # block = "1. One\n2. Two"
        # block_type = block_to_block_type(block)
        # self.assertEqual(block_type, block_type_ordered_list)

        # block = "1 One\n2. Two"
        # block_type = block_to_block_type(block)
        # self.assertNotEqual(block_type, block_type_ordered_list)

        # block = "1. One\n3. Two"
        # block_type = block_to_block_type(block)
        # self.assertNotEqual(block_type, block_type_ordered_list)

        # block = "1. One\n2 Two"
        # block_type = block_to_block_type(block)
        # self.assertNotEqual(block_type, block_type_ordered_list)