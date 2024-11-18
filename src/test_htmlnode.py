import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_mthd(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(
            node.props_to_html(), ' href="https://www.google.com" target="_blank"'
        )

    def test_full_html(self):
        tag = "p"
        value = "this is a paragraph inside a tag"
        children = ["child_node_1", "child_node_2", "child_node_3"]
        props = {"href": "https://www.google.com", "target": "_blank"}

        node = HTMLNode(tag, value, children, props)
        expected_str = "HTMLNode: (p, this is a paragraph inside a tag, ['child_node_1', 'child_node_2', 'child_node_3'], {'href': 'https://www.google.com', 'target': '_blank'})"

        self.assertEqual(str(node), expected_str)

    def test_to_html_mthd(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        with self.assertRaises(NotImplementedError):
            node.to_html()


if __name__ == "__main__":
    unittest.main()
