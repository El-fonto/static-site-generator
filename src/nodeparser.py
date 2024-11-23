from textnode import TextType, TextNode


def main():
    node = TextNode("Before *bolded text* after", TextType.TEXT)

    old_nodes = [
        node,
        # TextNode("Before **bolded ** after", TextType.TEXT),
        # TextNode("Before `code` after", TextType.TEXT),
    ]

    print(f"giving the old_nodes as: {old_nodes}")
    print("================== I GET =================")
    print(f"{split_node_delimiter(old_nodes, "*", TextType.BOLD)}")


def split_node_delimiter(old_nodes, delimiter, text_type):
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
            new_nodes.append(TextNode(middle, text_type))

            if after:
                new_nodes.extend(splitter([TextNode(after, TextType.TEXT)]))

        return new_nodes

    return splitter(old_nodes)


main()
