import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


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
        expected_str = "HTMLNode: (p, this is a paragraph inside a tag, children: ['child_node_1', 'child_node_2', 'child_node_3'], {'href': 'https://www.google.com', 'target': '_blank'})"
        self.assertEqual(str(node), expected_str)

    def test_to_html_mthd(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_leaf_render_noprops(self):
        node = LeafNode("p", "This is a paragraph of text.")
        expected_str = "<p>This is a paragraph of text.</p>"
        self.assertEqual(node.to_html(), expected_str)

    def test_leaf_render_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        expected_str = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node.to_html(), expected_str)

    def test_leaf_no_value(self):
        node = LeafNode("a", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_no_tag(self):
        node = LeafNode(None, "I'm a value with no tag")
        expected_str = "I'm a value with no tag"
        self.assertEqual(node.to_html(), expected_str)

    def test_parent_only_leafs(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        expected_str = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), expected_str)

    def test_parent_w_1parent(self):
        node = ParentNode(
            "div",
            [
                ParentNode(
                    tag="b",
                    children=[
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),
                    ],
                ),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        expected_str = "<div><b>Normal text<i>italic text</i>Normal text</b>Normal text<i>italic text</i>Normal text</div>"
        self.assertEqual(node.to_html(), expected_str)

    def test_parent_w_nested_parents(self):
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "b",
                    [
                        ParentNode(
                            "i",
                            [
                                LeafNode(None, "Normal text"),
                                LeafNode("i", "italic text"),
                            ],
                        ),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode("b", "bold text"),
                    ],
                ),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode("b", "bold text"),
            ],
        )
        expected_str = (
            "<div><b><i>Normal text<i>italic text</i></i>"
            "Normal text<i>italic text</i><b>bold text</b></b>"
            "Normal text<i>italic text</i><b>bold text</b></div>"
        )
        self.assertEqual(node.to_html(), expected_str)

    def test_multiple_parents(self):
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode(None, "This is a paragraph."),
                        ParentNode("strong", [LeafNode(None, "With strong emphasis!")]),
                    ],
                ),
                ParentNode(
                    "ul",
                    [
                        ParentNode("li", [LeafNode(None, "Item 1")]),
                        ParentNode("li", [LeafNode(None, "Item 2")]),
                    ],
                ),
            ],
        )
        expected_str = (
            "<div><p>This is a paragraph.<strong>With strong emphasis!</strong></p>"
            "<ul><li>Item 1</li><li>Item 2</li></ul></div>"
        )
        self.assertEqual(node.to_html(), expected_str)

    def test_None_in_children(self):
        node = ParentNode("b", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_no__children(self):
        node = ParentNode("b", [])
        expected_str = "<b></b>"
        self.assertEqual(node.to_html(), expected_str)


if __name__ == "__main__":
    unittest.main()
