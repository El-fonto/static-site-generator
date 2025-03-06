from textnode import TextNode, TextType


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: TextType
) -> list[TextNode] | None:
    new_nodes = []

    for old_node in old_nodes:
        # only split TextType.TEXT
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)

        if delimiter == "**" and text_type is TextType.BOLD:
            splitted = old_node.text.split(delimiter)

            new_nodes.append(splitted)

    return new_nodes


def main():
    node = TextNode("text with **bold block** word", TextType.TEXT)

    test_nodes = [node]
    new_nodes = split_nodes_delimiter(test_nodes, "**", TextType.BOLD)

    resulted_nodes = [
        TextNode("text with ", TextType.TEXT),
        TextNode("bold block", TextType.BOLD),
        TextNode(" word", TextType.TEXT),
    ]

    print("new_nodes: ", end="")
    print(new_nodes)

    print("result was: ", end="")
    print(resulted_nodes == new_nodes)


main()
