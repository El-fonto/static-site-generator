from enum import Enum
from htmlnode import HTMLNode
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


def markdown_to_html_node(markdown: str) -> HTMLNode:
    # divide document into blocks
    blocks = markdown_to_blocks(markdown)

    # add all nodes to return final product
    children_nodes = []

    # iterate through blocks and classify them
    for block in blocks:
        # get block type
        block_type = block_to_block_type(block)

        if block_type == BlockType.PARAGRAPH:
            paragraph_node = HTMLNode(tag="p", value=None)
            paragraph_node.children = text_to_children(block)
            children_nodes.append(paragraph_node)

        elif block_type == BlockType.HEADING:
            heading_level = len(block) - len(block.lstrip("#"))
            heading_node = HTMLNode(tag=f"h{heading_level}", value=None)
            heading_node.children = text_to_children(block.lstrip("#").strip())
            children_nodes.append(heading_node)

        elif block_type == BlockType.QUOTE:
            quote_node = HTMLNode(tag="blockquote", value=None)
            quote_node.children = text_to_children(block.lstrip(">").strip())
            children_nodes.append(quote_node)

        elif block_type == BlockType.ULIST:
            ul_node = HTMLNode(tag="ul", value=None)
            li_nodes = []
            for line in block.split("\n"):
                if line.strip():
                    list_node = HTMLNode(tag="li", value=None)
                    list_node.children = text_to_children(line.lstrip("- ").strip())
                    li_nodes.append(list_node)
            ul_node.children = li_nodes
            children_nodes.append(ul_node)

        elif block_type == BlockType.OLIST:
            ol_node = HTMLNode(tag="ol", value=None)
            li_nodes = []
            for line in block.split("\n"):
                if line.strip():
                    parts = line.strip().split(". ", 1)
                    if len(parts) > 1 and parts[0].isdigit():
                        content = parts[1]
                        list_node = HTMLNode(tag="li", value=None)
                        list_node.children = text_to_children(content)
                        li_nodes.append(list_node)
            ol_node.children = li_nodes
            children_nodes.append(ol_node)

        elif block_type == BlockType.CODE:
            # outer tag
            pre_node = HTMLNode(tag="pre", value=None)
            # inner tag
            code_node = HTMLNode(tag="code", value=None)
            # manual creation of a node to avoid parsing inline markdown
            text_node = TextNode(block.lstrip("```\n").rstrip("\n```"), TextType.TEXT)
            html_txt = text_node_to_html_node(text_node)
            # assign each layer to the next as children

            # conditional statement to be more explicit and comply with type hints
            if code_node.children is None:
                code_node.children = []
            code_node.children.append(html_txt)

            pre_node.children = [code_node]
            children_nodes.append(pre_node)

    # final node that will be returned
    parent_html = HTMLNode("div", None, children_nodes)

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


"""
def main():
    md = 
> the best of times

```
the best of codes 
```

# h1

## h2

- unordered_list_pattern

1. order things

    blocks = markdown_to_blocks(md)
    print("blocks: ", end="")
    print(blocks)

    for block in blocks:
        block_type = block_to_block_type(block)
        print()
        print("block type: ", end="")
        print(block_type)


main()
"""
