from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode


def main():
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)


def text_node_to_html_node(text_node):
    if text_node is not TextType:
        raise ValueError("invalid text type")


main()
