def markdown_to_blocks(markdown):
    lines = markdown.split("\n")
    blocks = []
    block = ""
    block_number = 0
    for line in lines:
        stripped_line = line.strip()
        if len (stripped_line) == 0:
            if len(block) != 0:
                blocks.append(block.rstrip())
            block = ""
        else:
            block += stripped_line + "\n"

    return blocks
