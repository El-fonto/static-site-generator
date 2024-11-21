from textnode import TextType, TextNode


def main():
    old_nodes = [
        TextNode("italic", TextType.ITALIC),
        TextNode("bold", TextType.BOLD),
        TextNode("This is text with a **bolded phrase** in the middle", TextType.TEXT),
    ]

    print(split_node_delimiter(old_nodes, "**", TextType.BOLD))


def split_node_delimiter(old_nodes, delimiter, text_type):
    def splitter(old_nodes):
        new_nodes = []
        for old_node in old_nodes:
            # Base case
            if not hasattr(old_node, "text_type"):
                new_nodes.append(old_node)
                continue

            if old_node.text_type != TextType.TEXT:
                new_nodes.append(old_node)
                continue

            if delimiter not in old_node.text:
                new_nodes.append(TextNode(old_node.text, TextType.TEXT))
                continue

            before, rest = old_node.text.split(delimiter, 1)
            new_nodes.append(TextNode(before, TextType.TEXT))

            if delimiter not in rest:
                raise ValueError("Invalid markdown syntax")

            middle, after = rest.split(delimiter, 1)
            if delimiter == "**":
                new_nodes.append(TextNode(middle, TextType.BOLD))
            if delimiter == "*":
                new_nodes.append(TextNode(middle, TextType.ITALIC))
            if delimiter == "`":
                new_nodes.append((TextNode(middle, TextType.CODE)))

            if after:
                new_nodes.extend(splitter([TextNode(after, TextType.TEXT)]))

            new_nodes.extend(splitter([after]))

        return new_nodes

    return splitter(old_nodes)


main()
