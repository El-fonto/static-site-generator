import re
from enum import Enum
from htmlnode import HTMLNode


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

    # iterate through blocks and classify them
    for block in blocks:
        # get block type
        block_type = block_to_block_type(block)

    return HTMLNode()


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
