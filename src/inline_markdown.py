from textnode import TextType, TextNode


def split_nodes_delimiter(old_nodes, delimiter, text_type):
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

            parts = old_node.text.split(delimiter)

            for i, part in enumerate(parts):
                if i % 2 == 0:  # Even indexes are text outside delimiters
                    if part:
                        new_nodes.append(TextNode(part, TextType.TEXT))
                else:  # Odd indexes are text between delimiters
                    if DELIMITER_MAP.get(delimiter) == text_type:
                        new_nodes.append(TextNode(part, text_type))

        return new_nodes

    return splitter(old_nodes)


def extract_markdown_images(text):
    # The text would look like this:
    # This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    # print(extract_markdown_images(text))
    # [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
    #
    # Will use regex to get it.
    # It takes a list and return a list of tuples
    pass


def extract_markdown_links(text):
    # same but with anchor text and links
    pass
