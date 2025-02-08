import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode(
            "This is an image node", TextType.BOLD_TEXT, "https://boot.dev"
        )
        self.assertNotEqual(node, node2)

    def test_no_url(self):
        node = TextNode("URL thing", TextType.LINK_TEXT, "https://boot.dev")
        node2 = TextNode("no url", TextType.LINK_TEXT, None)

        self.assertNotEqual(node, node2)

    def test_diff_types(self):
        node = TextNode("URL thing", TextType.LINK_TEXT, "https://boot.dev")
        node2 = TextNode("no url", TextType.BOLD_TEXT)

        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
