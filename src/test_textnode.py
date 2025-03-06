import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is an image node", TextType.BOLD, "https://boot.dev")
        self.assertNotEqual(node, node2)

    def test_no_url(self):
        node = TextNode("URL thing", TextType.LINK, "https://boot.dev")
        node2 = TextNode("no url", TextType.LINK, None)

        self.assertNotEqual(node, node2)

    def test_diff_types(self):
        node = TextNode("URL thing", TextType.LINK, "https://boot.dev")
        node2 = TextNode("no url", TextType.BOLD)

        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
