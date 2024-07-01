from textnode import TextNode, text_type_text, text_type_bold, text_type_italic, text_type_code, text_type_link, text_type_image
import re

# Currently I don't think this should work if the text starts or ends with a markdown element, but it does
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if type(old_node) != TextNode:
            new_nodes.append(old_node)
            continue
        
        split_nodes = []
        sections = old_node.text.split(delimiter)

        if len(sections) % 2 == 0:
            raise ValueError(f"Invalid Markdown: {delimiter} element not closed")

        #if text.count(delimiter) % 2:
        #    raise Exception(f"Invalid Markdown: {delimiter} element not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))

        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if type(old_node) != TextNode:
            new_nodes.append(old_node)
            continue
        sections = old_node.text.split("![image]")

def split_nodes_link(old_nodes):
    pass