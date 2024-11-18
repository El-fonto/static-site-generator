import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_normal(self):
        node = TextNode("That is another node", TextType.NORMAL)
        node2 = TextNode("That is another node", TextType.NORMAL)
        self.assertEqual(node, node2)

    def test_urls(self):
        node = TextNode("That is another node", TextType.ITALIC, None)
        node2 = TextNode("That is another node", TextType.ITALIC)
        self.assertEqual(node, node2)

    def test_content_url(self):
        node = TextNode("That is another node", TextType.LINK, "google.com")
        node2 = TextNode("That is another node", TextType.LINK, "google.com")
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
