import unittest
from main import text_node_to_html_node
from textnode import TextType, TextNode
from htmlnode import LeafNode


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


if __name__ == "__main__":
    unittest.main()
