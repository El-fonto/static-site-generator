from textnode import TextNode, TextType


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: TextType
) -> list[TextNode] | None:
    new_nodes = []

    for old_node in old_nodes:
        # only split TextType.TEXT
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)

        text = old_node.text

        if delimiter in text:
            # splitted = text.split(delimiter)

            i = 0
            current_text = ""
            is_formatted = False
            delimiter_length = len(delimiter)

            while i < len(text):
                if (
                    i <= len(text) - delimiter_length
                    and text[i : i + delimiter_length] == delimiter
                ):
                    if current_text:
                        if is_formatted:
                            new_nodes.append(TextNode(current_text, text_type))
                        else:
                            new_nodes.append(TextNode(current_text, TextType.TEXT))

                    is_formatted = False

                    i += delimiter_length
                else:
                    current_text += text[i]
                    i += 1

            if current_text:
                new_nodes.append(TextNode(current_text, TextType.TEXT))

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
