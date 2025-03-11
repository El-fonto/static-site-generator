import re
from textnode import TextNode, TextType


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: TextType
) -> list[TextNode]:
    new_nodes = []

    for old_node in old_nodes:
        # only split TextType.TEXT
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        if delimiter not in old_node.text:
            new_nodes.append(old_node)
            continue

        split_nodes = []
        sections = old_node.text.split(delimiter)

        # that meant that there is one section before the delimiter and one after
        if len(sections) % 2 == 0:
            raise ValueError("ivnalid Markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        # extract the list of tuples
        link_node_tup = extract_markdown_links(old_node.text)

        # base case to exit if no links/images in node
        if len(link_node_tup) == 0:
            new_nodes.append([old_node])

        # need to count how many links are there
        #
        # probably, tup indexes will be a variable; i.e. `i` and `i+1`, to account the number of links

        if len(link_node_tup) != 0:
            new_nodes.append(
                TextNode(
                    text=link_node_tup[0][0],
                    text_type=TextType.LINK,
                    url=link_node_tup[0][1],
                )
            )

    return new_nodes


def main():
    node = TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
        TextType.TEXT,
    )
    node_no_links = TextNode("text with no links", TextType.TEXT)

    new_nodes = split_nodes_link([node, node_no_links])

    print("EXTRACTED: ", end="")
    print(extract_markdown_links(node.text))
    print("SPLITTED: ", end="")
    print(new_nodes)


main()
# def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
#    new_nodes = []
#    for old_node in old_nodes:
#        # if old_node.text_type !=
#        if extract_markdown_images(old_node.text):
#            new_nodes.append(old_node)
#    return new_nodes
