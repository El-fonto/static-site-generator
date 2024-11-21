from textnode import TextNode, TextType


def main():
    node = TextNode("normal text", TextType.TEXT, "https://www.boot.dev")
    print(node)


if __name__ == "__main__":
    main()
