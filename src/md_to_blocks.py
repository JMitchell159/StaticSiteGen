def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    stripped_blocks = []
    for block in blocks:
        stripped_blocks.append(block.strip())
    return stripped_blocks