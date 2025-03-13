def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = markdown.split(sep="\n\n")
    filtered_blocks = []
    for block in blocks:
        block = block.strip()
        if block != "":
            filtered_blocks.append(block)
    return filtered_blocks
