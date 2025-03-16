from enum import Enum
from htmlnode import HTMLNode, ParentNode
from inline_markdown import text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html_node


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"


def block_to_block_type(block: str) -> BlockType:
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.ULIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.OLIST
    return BlockType.PARAGRAPH


def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = markdown.split(sep="\n\n")
    filtered_blocks = []
    for block in blocks:
        block = block.strip()
        if block != "":
            filtered_blocks.append(block)
    return filtered_blocks


def markdown_to_html_node(markdown: str) -> ParentNode:
    # divide document into blocks
    blocks = markdown_to_blocks(markdown)

    # add all nodes to return final product
    children_nodes = []

    # iterate through blocks and classify them
    for block in blocks:
        # get block type
        block_type = block_to_block_type(block)

        if block_type == BlockType.PARAGRAPH:
            paragraph_node = ParentNode(tag="p", children=[])
            paragraph_text = block.replace("\n", " ").strip()
            paragraph_node.children = text_to_children(paragraph_text)
            children_nodes.append(paragraph_node)

        elif block_type == BlockType.HEADING:
            heading_level = len(block) - len(block.lstrip("#"))
            heading_node = ParentNode(tag=f"h{heading_level}", children=[])
            heading_node.children = text_to_children(block.lstrip("#").strip())
            children_nodes.append(heading_node)

        elif block_type == BlockType.QUOTE:
            quote_node = ParentNode(tag="blockquote", children=[])
            quote_lines = []
            for line in block.split("\n"):
                if line.startswith(">"):
                    quote_line = line[1:].strip()
                    quote_lines.append(quote_line)
            quote_content = " ".join(quote_lines)
            quote_node.children = text_to_children(quote_content)
            children_nodes.append(quote_node)

        elif block_type == BlockType.ULIST:
            ul_node = ParentNode(tag="ul", children=[])
            li_nodes = []
            for line in block.split("\n"):
                if line.strip():
                    list_node = ParentNode(tag="li", children=[])
                    list_node.children = text_to_children(line.lstrip("- ").strip())
                    li_nodes.append(list_node)
            ul_node.children = li_nodes
            children_nodes.append(ul_node)

        elif block_type == BlockType.OLIST:
            ol_node = ParentNode(tag="ol", children=[])
            li_nodes = []
            for line in block.split("\n"):
                if line.strip():
                    parts = line.strip().split(". ", 1)
                    if len(parts) > 1 and parts[0].isdigit():
                        content = parts[1]
                        list_node = ParentNode(tag="li", children=[])
                        list_node.children = text_to_children(content)
                        li_nodes.append(list_node)
            ol_node.children = li_nodes
            children_nodes.append(ol_node)

        elif block_type == BlockType.CODE:
            # outer tag
            pre_node = ParentNode(tag="pre", children=[])
            # inner tag
            code_node = ParentNode(tag="code", children=[])
            # manual creation of a node to avoid parsing inline markdown
            text_node = TextNode(block.lstrip("```\n").rstrip("```"), TextType.TEXT)
            html_txt = text_node_to_html_node(text_node)
            # assign each layer to the next as children

            # conditional statement to be more explicit and comply with type hints
            code_node.children.append(html_txt)

            pre_node.children.append(code_node)
            children_nodes.append(pre_node)

    # final node that will be returned
    parent_html = ParentNode("div", children_nodes)

    return parent_html


def text_to_children(text: str) -> list[HTMLNode]:
    """make a list of children"""
    html_nodes = []
    # from a str -> a list[TextNode]
    text_nodes = text_to_textnodes(text)
    for text_node in text_nodes:
        # convert TextNode to html and append it
        child = text_node_to_html_node(text_node)
        html_nodes.append(child)
    return html_nodes
