from textnode import TextNode, TextType
from htmlnode import LeafNode


def main():
    node = TextNode("normal text", TextType.TEXT, "https://www.boot.dev")
    html_node = text_node_to_html_node(node)
    print(html_node)


def text_node_to_html_node(text_node):
    # Error checking done
    if not isinstance(text_node.text_type, TextType):
        raise ValueError("invalid text_type")

    # TODO:
    # Check with if statements using method notation
    #
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)

    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)

    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)

    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)

    elif text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})

    elif text_node.text_type == TextType.IMAGE:
        return LeafNode("img", {"src": text_node.url, "alt": text_node.text})


if __name__ == "__main__":
    main()
