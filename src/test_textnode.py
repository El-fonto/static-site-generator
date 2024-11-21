import unittest

from nodeparser import split_node_delimiter
from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_normal(self):
        node = TextNode("That is another node", TextType.TEXT)
        node2 = TextNode("That is another node", TextType.TEXT)
        self.assertEqual(node, node2)

    def test_urls(self):
        node = TextNode("That is another node", TextType.ITALIC, None)
        node2 = TextNode("That is another node", TextType.ITALIC)
        self.assertEqual(node, node2)

    def test_content_url(self):
        node = TextNode("That is another node", TextType.LINK, "google.com")
        node2 = TextNode("That is another node", TextType.LINK, "google.com")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "google.com")
        self.assertEqual("TextNode(This is a text node, text, google.com)", repr(node))


class TestConversion(unittest.TestCase):
    def test_text_conversion(self):
        node = TextNode("normal text", TextType.TEXT, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node, LeafNode(None, "normal text", None))

    def test_bold_conversion(self):
        node = TextNode("bold text", TextType.BOLD, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node, LeafNode("b", "bold text", None))

    def test_italic_conversion(self):
        node = TextNode("italic text", TextType.ITALIC, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node, LeafNode("i", "italic text", None))

    def test_code_conversion(self):
        node = TextNode("code text", TextType.CODE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node, LeafNode("code", "code text", None))

    def test_link_conversion(self):
        node = TextNode("linked text", TextType.LINK, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node, LeafNode("a", node.text, {"href": node.url}))

    def test_image_conversion(self):
        node = TextNode("alt text", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(
            html_node, LeafNode("img", {"src": node.url, "alt": node.text})
        )


class TestSplitNodeDelimiter(unittest.TestCase):
    def test_basic_bold_split(self):
        nodes = [TextNode("This is **bold** text", TextType.TEXT)]
        result = [split_node_delimiter(nodes, "**", TextType.BOLD)]
        pass


if __name__ == "__main__":
    unittest.main()
