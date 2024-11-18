from textnode import TextNode
from htmlnode import HTMLNode


def main():
    # Test Values

    # TextNode
    text = "This is a text node"
    text_type = "bold"
    url = "https://www.boot.dev"
    text_type2 = "italic"

    # HTMLNode
    tag = "p"
    value = "this is a paragraph inside a tag"
    children = ["child_node_1", "child_node_2", "child_node_3"]
    props = {"href": "https://www.google.com", "target": "_blank"}

    test_node_2 = TextNode(text, text_type2, url)
    test_node_1 = TextNode(text, text_type, url)

    full_html = HTMLNode(tag, value, children, props)
    partial_html = HTMLNode(children=children, props=props)
    only_props_test = full_html.props_to_html()

    # prints
    print(f"html child-props test: {partial_html}")
    print(f"html props test: {only_props_test}")
    print(f"html test: {full_html}")

    print(f"text test 1: {test_node_1}")
    print(f"text test 2: {test_node_2}")


main()
