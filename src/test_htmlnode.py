import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType, text_node_to_html_node
import textnode


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


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_multiple_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node_1 = ParentNode("div", [child_node, child_node])
        parent_node_2 = ParentNode("html", [parent_node_1])
        self.assertEqual(
            parent_node_2.to_html(),
            "<html><div><span><b>grandchild</b></span><span><b>grandchild</b></span></div></html>",
        )

    def test_parent_tag_error(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_parent_children_error(self):
        parent_node = ParentNode("a", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )


class TestConversionNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_single_tag(self):
        bold_node = TextNode("bold text", TextType.BOLD)
        bold_html_node = text_node_to_html_node(bold_node)

        italic_node = TextNode("italic text", TextType.ITALIC)
        italic_html_node = text_node_to_html_node(italic_node)

        code_node = TextNode("code text", TextType.CODE)
        code_html_node = text_node_to_html_node(code_node)

        # bold
        self.assertEqual(bold_html_node.tag, "b")
        self.assertEqual(bold_html_node.value, "bold text")

        # italic
        self.assertEqual(italic_html_node.tag, "i")
        self.assertEqual(italic_html_node.value, "italic text")

        # code
        self.assertEqual(code_html_node.tag, "code")
        self.assertEqual(code_html_node.value, "code text")

    def test_link(self):
        link_node = TextNode("My Google page", TextType.LINK, "google.com")
        html_node = text_node_to_html_node(link_node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "My Google page")
        self.assertEqual(html_node.props, {"href": "google.com"})

    def test_image(self):
        node = TextNode("alt text", TextType.IMAGE, "google.com/image.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props, {"href": "google.com/image.jpg", "alt": "alt text"}
        )


if __name__ == "__main__":
    unittest.main()
