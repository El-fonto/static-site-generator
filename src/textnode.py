from enum import Enum
from htmlnode import LeafNode


class TextType(Enum):
    TEXT = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str | None = None):
        self.text = text
        self.text_type = TextType(text_type)
        self.url = url

    def __eq__(self, other) -> bool:
        return (
            (self.text == other.text)
            and (self.text_type == other.text_type)
            and (self.url == other.url)
        )

    def __repr__(self) -> str:
        if self.url is None:
            return f"TextNode({self.text}, {self.text_type.value})"
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(textnode: TextNode) -> LeafNode:
    if textnode.text_type == TextType.TEXT:
        return LeafNode(None, textnode.text)
    elif textnode.text_type == TextType.BOLD:
        return LeafNode("b", textnode.text)
    elif textnode.text_type == TextType.ITALIC:
        return LeafNode("i", textnode.text)
    elif textnode.text_type == TextType.CODE:
        return LeafNode("code", textnode.text)
    elif textnode.text_type == TextType.LINK:
        return LeafNode("a", textnode.text, {"href": f"{textnode.url}"})
    elif textnode.text_type == TextType.IMAGE:
        return LeafNode(
            "img", "", {"href": f"{textnode.url}", "alt": f"{textnode.text}"}
        )
    else:
        raise ValueError(f"Invalid TextType: {textnode.text_type}")
