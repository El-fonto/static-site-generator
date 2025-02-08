import unittest
from htmlnode import HTMLNode


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


if __name__ == "__main__":
    unittest.main()
