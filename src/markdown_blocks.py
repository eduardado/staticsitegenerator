from parentnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_ulist = "unordered_list"
block_type_olist = "ordered_list"
block_type_normal_text = "normal_text"

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
    lines = block.split("\n")

    if(
        block.startswith("# ")
        or block.startswith("## ")
        or block.startswith("### ")
        or block.startswith("#### ")
        or block.startswith("##### ")
        or block.startswith("###### ")
    ):
        return block_type_heading
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return block_type_code
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return block_type_paragraph
            return block_type_quote
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return block_type_paragraph
        return block_type_ulist
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return block_type_paragraph
        return block_type_ulist
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}."):
                return block_type_paragraph
            i += 1
        return block_type_olist
    return block_type_paragraph
            
def markdown_to_html_node(markdown):
    # divides markdown plain text into blocks with a previous function
    blocks = markdown_to_blocks(markdown)
    # creates an empty list for the children of the top hiearchy div block
    children = []
    # For each block
    for block in block:
        # creates an html node using a new function
        html_node = block_to_html_node(block)
        # add the html node in the list
        children.append(html_node)
        # creates a ParentNode with the tag div. Its children are the html nodes we createad from each block in the markdown
    return ParentNode(children, "div", None)

# The differences between an HTMLNode object and a ParentNode object are:
# - An HTMLNode has value and a ParentNode doesn't
# - A ParentNode knows implements to_html() while HTMLNode doesn't
# - HTMLNode doesn't implement to_html(), its either LeafNode and ParentNode, who extend HTMLNode, the ones who know how to represent a Node with tags
# - ParentNode: to_html() build the tags and its children trags inside. I wonder, if the children are HTMLNode instead of LeafNode, will they know how to to_html() themselves? is that part of the code correct?

def block_to_html_node(block):
    # identifies the block type and invoques the right function to transform the block into its correct html node
    block_type = block_to_block_type(block)
    if block_type == block_type_paragraph:
        return paragraph_to_html_node(block):
    if block_type == block_type_heading:
        return heading_to_html_node(block)
    if block_type == block_type_code:
        return code_to_html_node(block)
    if block_type == block_type_olist:
        return olist_to_html_node(block)
    if block_type == block_type_ulist:
        return ulist_to_html_node(block)
    if block_type == block_type_quote(block):
        return quote_to_html_node(block)
    raise ValueError("Invalid block type")

# this function extract pieace of text into text nodes and return them as a list
def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def paragraph_to_html_node(block):
    # divides the block into lines by next line
    lines = block.split("\n")
    # merge the lines, represented en the list, eliminated the next line symbol and join the with a space. Why doing that?
    paragraph = " ".join(lines)
    # scans the paragraph for different types of in line text
    children = text_to_children(paragraph)
    return ParentNode(children, "p")

def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#"
            level += 1
        else:
            break
    # if the length of the heading is greater than the level... wrong
    if level + 1 >= len(block):
        raise ValueError(f"Invalid heading level: {level}")
    # the text is the level ###... + space until the end
    text = block[level + 1 :]
    # evaluates for chunks of text with other inline types
    children = text_to_children(text)
    return ParentNode(children, f"h{level}")

def code_to_html_node(block):
    if not block startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    # text between backticks and next line
    text = block[4:-3]
    children = text_to_children(text)
    # <pre><code></code></pre>
    # we create the ParentNode code with its children
    code = ParentNode(children, "code")
    # we surround the ParentNode with another ParentNode and introduce de code ParentNode as a nested children
    return ParentNode([code], "pre")

def olist_to_html_node(block):
    # items separated by next line
    items = block.split("\n")
    html_items = []
    for item in items:
        #1. 3 chars before text
        text = item[3:]
        children = text_to_children(text)
        # each item <li>
        html_items.append(ParentNode(children, "li"))
    return ParentNode(html_items, "ol")

def ulist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        # * 
        text = items[2:]
        children = text_to_children(text)
        html_items.append(ParentNode(children, "li"))
    return ParentNode(html_items, "ul")

def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())
        content = " ".join(new_lines)
        children = text_to_children(content)
        return ParentNode(children, "blockquote")





