import unittest
from markdown_blocks import markdown_to_blocks, BlockType, block_to_block_type


class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""

        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_empty_blocks(self):
        md = ""
        blocks = markdown_to_blocks(md)
        self.assertListEqual(blocks, [])

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_heading_identification(self):
        # Test various heading levels
        self.assertEqual(block_to_block_type("# Heading 1"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("## Heading 2"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("###### Heading 6"), BlockType.HEADING)

    def test_code_block_identification(self):
        # Test code blocks
        self.assertEqual(block_to_block_type("```\ncode block\n```"), BlockType.CODE)
        self.assertEqual(
            block_to_block_type("```python\ndef function():\n    pass\n```"),
            BlockType.CODE,
        )

    def test_quote_identification(self):
        # Test blockquotes
        self.assertEqual(block_to_block_type("> This is a quote"), BlockType.QUOTE)
        self.assertEqual(block_to_block_type("> Multi-line\n> quote"), BlockType.QUOTE)

    def test_unordered_list_identification(self):
        # Test unordered lists
        self.assertEqual(block_to_block_type("- Item 1"), BlockType.ULIST)
        self.assertEqual(block_to_block_type("- Item 1\n- Item 2"), BlockType.ULIST)

    def test_ordered_list_identification(self):
        # Test ordered lists
        self.assertEqual(block_to_block_type("1. First item"), BlockType.OLIST)
        self.assertEqual(
            block_to_block_type("1. First item\n2. Second item"), BlockType.OLIST
        )

    def test_paragraph_identification(self):
        # Test paragraphs (default when no other pattern matches)
        self.assertEqual(
            block_to_block_type("This is a paragraph"), BlockType.PARAGRAPH
        )
        self.assertEqual(
            block_to_block_type("This is a paragraph\nwith multiple lines"),
            BlockType.PARAGRAPH,
        )

    def test_edge_cases(self):
        # Test edge cases
        self.assertEqual(
            block_to_block_type("#Not a heading"), BlockType.PARAGRAPH
        )  # No space after #
        self.assertEqual(
            block_to_block_type("```"), BlockType.PARAGRAPH
        )  # Incomplete code block
        self.assertEqual(block_to_block_type("-Not a list"), BlockType.PARAGRAPH)

    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        block = "- list\n- items"
        self.assertEqual(block_to_block_type(block), BlockType.ULIST)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), BlockType.OLIST)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()
