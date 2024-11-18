from textnode import TextNode
from htmlnode import HTMLNode


def main():
    # Test Values
    text = "This is a text node"
    text_type = "bold"
    url = "https://www.boot.dev"
    text_type2 = "italic"
    test_node_1 = TextNode(text, text_type, url)
    test_node_2 = TextNode(text, text_type2, url)

    html = HTMLNode(props={"href": "https://www.google.com"})
    print(html.props_to_html)
    print(html)

    # print(test_node_1 == test_node_2)
    # print(test_node_1)


main()
