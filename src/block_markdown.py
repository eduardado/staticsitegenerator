from block import block_type_paragraph, block_type_heading, block_type_code, block_type_quote, block_type_unordered_list, block_type_ordered_list, block_type_normal_text

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

def block_to_block_type(block):
    if is_heading(block):
        return block_type_heading
    if block.startswith("```") and block.endswith("```"):
        return block_type_code
    if block.startswith(">"):
        return block_type_quote
    if block.startswith("* ") or block.startswith("- "):
        return block_type_unordered_list
    if isOrderedList(block):
        return block_type_ordered_list
    return block_type_normal_text

def isOrderedList(block):
    block_lines = block.split("\n")
    count = 1
    for block_line in block_lines:
        block_line_chars = list(block_line)

        if not block_line_chars[0].isdigit():
            return False

        if not int(block_line_chars[0]) == count:
            return False
        else:
            count += 1
            
        if not block_line_chars[1] == ".":
            return False
        if not block_line_chars[2] == " ":
            return False

    return True

def is_heading(block):
    if not block.startswith("#"):
        return False
        # print(f"starts with #")

    hash_count = 0
    for char in block:
        if char == "#":
            hash_count += 1
    if hash_count < 1 or hash_count > 6:
        return False
    for split in block.split("#"):
        if not split:
            continue
        if not split.startswith(" "):
            return False

    return True
        

        
        # print(f"block_line:{block_line}")
        # print(f"first char:{list(block_line)[0]}")
        # print(f"second char:{list(block_line)[1]}")
        # print(f"third char:{list(block_line)[2]}")
        # if list(block_line)[0].isdigit() and list(block_line)[1] == "." and list(block_line)[2] == " " and list(block_line)[2] == 1:
        #     print(f"conditions = True")
        #     count += 1
        #     print(f"count = {count}")
        #     continue
        # else:
        #     return False
        # return True


