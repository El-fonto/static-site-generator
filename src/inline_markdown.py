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
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        # extract list of tuples
        link_tups = extract_markdown_links(old_node.text)

        # base case: don't process if no links/images in node
        if not link_tups:
            new_nodes.append(old_node)
            continue

        # original text
        remaining_text = old_node.text

        # iterate over list, assigning tuple values to variables
        for link_text, link_url in link_tups:
            # find the markdown link and split at the first ocurrence for each element
            parts = remaining_text.split(f"[{link_text}]({link_url})", 1)

            if len(parts) != 2:
                raise ValueError("invalid markdown, link section not closed")

            # append what's before the link
            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.TEXT))

            new_nodes.append(
                TextNode(text=link_text, text_type=TextType.LINK, url=link_url)
            )

            # reprocess remaining_text after the link
            if len(parts) > 1:
                remaining_text = parts[1]
            else:
                remaining_text = ""

        # add remaining text after links are processed
        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return new_nodes


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        images = extract_markdown_images(old_node.text)
        if not images:
            new_nodes.append(old_node)
            continue
        remaining_text = old_node.text

        for image_alt, image_link in images:
            parts = remaining_text.split(f"![{image_alt}]({image_link})", 1)

            if len(parts) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.TEXT))

            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
            if len(parts) > 1:
                remaining_text = parts[1]
            else:
                remaining_text = ""
        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes
