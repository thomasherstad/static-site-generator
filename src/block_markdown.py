from textnode import TextNode

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered list"
block_type_ordered_list = "ordered list"


def markdown_to_block(markdown):
    blocks = markdown.split("\n\n")
    filtered = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered.append(block)
    return filtered

def block_to_blocktype(block):
    if block[0] == "#":
        sections = block.split("# ", maxsplit=1)
        print(sections)
        if len(sections) != 2:
            return block_type_paragraph
        heading_number = len(sections[0]) + 1
        if heading_number > 6:
            return block_type_paragraph
        heading = sections[1]
        return block_type_heading
    elif block[0] == "`":
        sections = block.split("```")
        if sections[0] != "" or sections[2] != "":
            return block_type_paragraph
        return block_type_code
    elif block[0] == ">":
        lines = block.split("\n")
        for line in lines:
            if line[0] == ">" and line[1] == " ":
                continue
            else:
                return block_type_paragraph
        return block_type_quote
    elif (block[0] == "*" or block[0] == "-") and block[1] == " ":
        lines = block.split("\n")
        for line in lines:
            if line[0] == "-" and line[1] == " ":
                continue
            elif line[0] == "*" and line[1] == " ":
                continue
            else:
                return block_type_paragraph
        return block_type_unordered_list
    elif block[0] == "1":
        lines = block.split("\n")
        for i in range(1, len(lines)+1):
            valid = f"{i}. "
            if lines[i-1].startswith(valid):
                continue
            else:
                return block_type_paragraph
        return block_type_ordered_list
    else:
        return block_type_paragraph
    
#Block to HTML functions
def block_to_HTML_paragraph(markdown):
    pass