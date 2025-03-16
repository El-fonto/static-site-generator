import unittest
from markdown_blocks import (
    markdown_to_blocks,
    BlockType,
    block_to_block_type,
    markdown_to_html_node,
)


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


class TestMarkdownToHTML(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_basic_paragraph(self):
        md = "This is a simple paragraph."
        node = markdown_to_html_node(md)
        expected_html = "<div><p>This is a simple paragraph.</p></div>"
        self.assertEqual(node.to_html(), expected_html)

    def test_multiple_paragraphs(self):
        md = """First paragraph.

Second paragraph."""
        node = markdown_to_html_node(md)
        expected_html = "<div><p>First paragraph.</p><p>Second paragraph.</p></div>"
        self.assertEqual(node.to_html(), expected_html)

    def test_heading_conversion(self):
        md = """# Heading 1

## Heading 2

### Heading 3"""
        node = markdown_to_html_node(md)
        expected_html = (
            "<div><h1>Heading 1</h1><h2>Heading 2</h2><h3>Heading 3</h3></div>"
        )
        self.assertEqual(node.to_html(), expected_html)

    def test_code_blocks(self):
        md = """```
def hello():
    print("Hello, world!")
```"""
        node = markdown_to_html_node(md)
        expected_html = '<div><pre><code>def hello():\n    print("Hello, world!")\n</code></pre></div>'
        self.assertEqual(node.to_html(), expected_html)

    def test_blockquotes(self):
        md = "> This is a quote\n> Continued quote"
        node = markdown_to_html_node(md)
        expected_html = (
            "<div><blockquote>This is a quote Continued quote</blockquote></div>"
        )
        self.assertEqual(node.to_html(), expected_html)

    def test_unordered_lists(self):
        md = """- Item 1
- Item 2
- Item 3"""
        node = markdown_to_html_node(md)
        expected_html = (
            "<div><ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul></div>"
        )
        self.assertEqual(node.to_html(), expected_html)

    def test_ordered_lists(self):
        md = """1. First
2. Second
3. Third"""
        node = markdown_to_html_node(md)
        expected_html = (
            "<div><ol><li>First</li><li>Second</li><li>Third</li></ol></div>"
        )
        self.assertEqual(node.to_html(), expected_html)

    def test_mixed_content(self):
        md = """# Heading

This is a paragraph with **bold** text.

- List item 1
- List item 2

> A quote block

```
code block
```"""
        node = markdown_to_html_node(md)
        expected_html = "<div><h1>Heading</h1><p>This is a paragraph with <b>bold</b> text.</p><ul><li>List item 1</li><li>List item 2</li></ul><blockquote>A quote block</blockquote><pre><code>code block\n</code></pre></div>"
        self.assertEqual(node.to_html(), expected_html)

    def test_nested_formatting(self):
        md = "This has **bold with normal inside**."
        node = markdown_to_html_node(md)
        expected_html = "<div><p>This has <b>bold with normal inside</b>.</p></div>"
        self.assertEqual(node.to_html(), expected_html)

    def test_empty_input(self):
        md = ""
        node = markdown_to_html_node(md)
        expected_html = "<div></div>"
        self.assertEqual(node.to_html(), expected_html)

    def test_whitespace_handling(self):
        md = "   Paragraph with spaces   "
        node = markdown_to_html_node(md)
        expected_html = "<div><p>Paragraph with spaces</p></div>"
        self.assertEqual(node.to_html(), expected_html)


if __name__ == "__main__":
    unittest.main()
