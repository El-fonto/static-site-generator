from textnode import TextType, TextNode


def main():
    bold_node = TextNode("Before **bolded text** after", TextType.TEXT)
    italic_node = TextNode("Before *italized text* after", TextType.TEXT)
    code_node = TextNode("Before `code text` after", TextType.TEXT)

    bold_nodes = [bold_node]
    italic_nodes = [italic_node]
    code_nodes = [code_node]

    print(f"{split_node_delimiter(bold_nodes, "**", TextType.BOLD)}")
    print()
    print(f"{split_node_delimiter(italic_nodes, "*", TextType.ITALIC)}")
    print()
    print(f"{split_node_delimiter(code_nodes, "`", TextType.CODE)}")


def split_node_delimiter(old_nodes, delimiter, text_type):
    DELIMITER_MAP = {
        "**": TextType.BOLD,
        "*": TextType.ITALIC,
        "`": TextType.CODE,
    }

    def splitter(old_nodes):
        new_nodes = []
        for old_node in old_nodes:
            # Base case
            if old_node.text_type != TextType.TEXT:
                new_nodes.append(old_node)
                continue

            if delimiter not in old_node.text:
                new_nodes.append(TextNode(old_node.text, TextType.TEXT))
                continue

            before, rest = old_node.text.split(delimiter, 1)
            new_nodes.append(TextNode(before, TextType.TEXT))

            # closing delimiter check
            if delimiter not in rest:
                raise ValueError("Invalid markdown syntax")

            middle, after = rest.split(delimiter, 1)
            if DELIMITER_MAP.get(delimiter) == text_type:
                new_nodes.append(TextNode(middle, text_type))

            if after:
                new_nodes.extend(splitter([TextNode(after, TextType.TEXT)]))

        return new_nodes

    return splitter(old_nodes)


main()
