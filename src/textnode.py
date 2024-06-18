from htmlnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, node):
        return (self.text == node.text and self.text_type == node.text_type and self.url == node.url)
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node):
    if text_node.text_type == text_type_text:
        node = LeafNode(None, text_node.text)
        return node.to_html()
    elif text_node.text_type == text_type_bold:
        node = LeafNode("b", text_node.text)
        return node.to_html()
    elif text_node.text_type == text_type_italic:
        node = LeafNode("i", text_node.text)
        return node.to_html()
    elif text_node.text_type == text_type_code:
            node = LeafNode("code", text_node.text)
            return node.to_html()
    elif text_node.text_type == text_type_link:
            node = LeafNode("a", text_node.text, {'href': text_node.url})
            return node.to_html()
    elif text_node.text_type == text_type_image:
            node = LeafNode("img", "", {"src": text_node.url, "alt": text_node.text}) # Potential bug with no "-wrapping on the alt text 
            return node.to_html()
    else:
          raise Exception(f"Invalid text type: {text_node.text_type}")

