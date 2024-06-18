import unittest

from textnode import TextNode, split_nodes_delimiter

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_diff_text(self):
        node = TextNode("This is a text node", "italic", "boot.dev")
        node2 = TextNode("This is a different text node", "italic", "boot.dev")
        self.assertNotEqual(node, node2)

    def test_diff_type(self):
        node = TextNode("This is a text node", "bold", "boot.dev")
        node2 = TextNode("This is a text node", "italic", "boot.dev")
        self.assertNotEqual(node, node2)


    def test_diff_url(self):
        node = TextNode("This is a text node", "bold", "boot.dev")
        node2 = TextNode("This is a text node", "italic", "boot.dev")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", "bold", "boot.dev")
        expected_repr = "TextNode(This is a text node, bold, boot.dev)"
        self.assertEqual(repr(node), expected_repr)
        
    # Add tests for text_node_to_html_node()

