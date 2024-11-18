from enum import Enum


class TextType(Enum):
    """
    NORMAL = "normal"
    BOLD = "**bold**"
    ITALIC = "*italic*"
    CODE = "```\ncode\n```"
    LINK = "[link text](link)"
    IMAGE = "![alt text](url)"
    """

    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = TextType(text_type)
        self.url = url

    def __eq__(self, TextNode):
        return (
            self.text == TextNode.text
            and self.text_type == TextNode.text_type
            and self.url == TextNode.url
        )

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
