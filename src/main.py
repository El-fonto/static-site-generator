from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode


def main():
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    html_node = text_node_to_html_node(node)
    print(node)
    print(html_node)


def text_node_to_html_node(text_node):
    # Error checking done
    #
    if not isinstance(text_node.text_type, TextType):
        raise ValueError("invalid text_type")

    # TODO:
    # Check with if statements using method notation
    #
    if text_node.text_type.TEXT:
        return LeafNode(None, text_node.text)

    if text_node.text_type.BOLD:
        return LeafNode("b", text_node.text)

    if text_node.text_type.ITALIC:
        return LeafNode("i", text_node.text)

    if text_node.text_type.CODE:
        return LeafNode("code", text_node.text)

    if text_node.text_type.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})

    if text_node.text_type.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})


main()
