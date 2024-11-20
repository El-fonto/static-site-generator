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

    def test_to_html_parent_child(self):
        child_node = LeafNode("b", "child")
        node = ParentNode("p", [child_node])
        self.assertEqual(node.to_html(), "<p><b>child</b></p>")

    def test_to_html_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("p", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><p><b>grandchild</b></p></div>")

    def test_parent_w_nested_parents(self):
        og_child_node = LeafNode("h1", "the OG")
        grandchild_node = ParentNode("b", [og_child_node])
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(), "<div><span><b><h1>the OG</h1></b></span></div>"
        )

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
