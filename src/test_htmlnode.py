import unittest
from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    dummy_tag = "p"
    dummy_value = "this is an HTMLNode"
    dummy_children = ["child1", "child2"]
    dummy_props = {
        "href": "https://www.google.com",
        "target": "_blank",
    }

    def test_props_to_html(self):
        node = HTMLNode(props=self.dummy_props)
        test_str = ' href="https://www.google.com" target="_blank"'

        self.assertEqual(node.props_to_html(), test_str)

    # test empty props
    def test_props_to_html_empty(self):
        node = HTMLNode()
        test_str = ""
        self.assertEqual(node.props_to_html(), test_str)

    def test_html_repr(self):
        node = HTMLNode(
            self.dummy_tag, self.dummy_value, self.dummy_children, self.dummy_props
        )
        test_str = """ HTMLNode:
tag: p
value: this is an HTMLNode
children: ['child1', 'child2']
props: {'href': 'https://www.google.com', 'target': '_blank'}"""

        self.assertEqual(node.__repr__(), test_str)

    def test_to_html_some_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://google.com"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://google.com"',
        )


class TestLeafNode(unittest.TestCase):
    def test_leafnode_no_props(self):
        node = LeafNode(
            "div",
            "Hello, world!",
        )
        self.assertEqual(node.to_html(), "<div>Hello, world!</div>")

    def test_leafnode_props(self):
        node = LeafNode(
            "div", "Hello, world!", {"class": "greeting", "href": "https://google.com"}
        )
        self.assertEqual(
            node.to_html(),
            '<div class="greeting" href="https://google.com">Hello, world!</div>',
        )

    def test_leafnode_no_tag(self):
        node = LeafNode(tag=None, value="no tag text")
        self.assertEqual(node.to_html(), "no tag text")

    def test_leafnode_value_error(self):
        node = LeafNode(tag=None, value=None)
        with self.assertRaises(ValueError):
            node.to_html()


if __name__ == "__main__":
    unittest.main()
