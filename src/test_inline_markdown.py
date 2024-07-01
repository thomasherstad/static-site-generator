import unittest
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links
from textnode import TextNode, text_type_text, text_type_bold, text_type_italic, text_type_code, text_type_link, text_type_image


class TextInlineMarkdown(unittest.TestCase):
    # Add tests for split_nodes_delimiter()
    def test_split_nodes_simple_bold(self):
        node = TextNode("This is text with a **bold** word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        expected = [
            TextNode("This is text with a ", text_type_text),
            TextNode("bold", text_type_bold),
            TextNode(" word", text_type_text),
        ]
        self.assertEqual(new_nodes, expected)

    # multiple bolds in one sentence
    def test_split_nodes_multiple_bolds(self):
        node = TextNode("This is a **text** with multiple **bold** words **within** it", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        expected = [
            TextNode("This is a ", text_type_text),
            TextNode("text", text_type_bold),
            TextNode(" with multiple ", text_type_text),
            TextNode("bold", text_type_bold),
            TextNode(" words ", text_type_text),
            TextNode("within", text_type_bold),
            TextNode(" it", text_type_text),
        ]
        self.assertEqual(new_nodes, expected)
    

    # starting with bold
    def test_split_nodes_starting_bold(self):
        node = TextNode("**Bold** is the first word here", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        expected = [
            TextNode("Bold", text_type_bold),
            TextNode(" is the first word here", text_type_text),
        ]
        self.assertEqual(new_nodes, expected)
        
    # italic
    def test_split_nodes_simple_italic(self):
        node = TextNode("This is text with an *italic* word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        expected = [
            TextNode("This is text with an ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" word", text_type_text),
        ]
        self.assertEqual(new_nodes, expected)
    
    # code
    def test_split_nodes_simple_code(self):
        node = TextNode("This is text with `a section of code` in it", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        expected = [
            TextNode("This is text with ", text_type_text),
            TextNode("a section of code", text_type_code),
            TextNode(" in it", text_type_text),
        ]
        self.assertEqual(new_nodes, expected)

    # all three in one sentence 

    # test if markdown element is not closed
    def test_split_nodes_non_closed(self):
        node = TextNode("This is text with a **bold** word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        expected = ValueError("Invalid Markdown: ** element not closed")
    # test if text is not a TextNode object


    def test_extract_markdown_images(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        expected = [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), 
                    ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")]
        text_extracted = extract_markdown_images(text)
        self.assertEqual(text_extracted, expected)


    def test_extract_markdown_links(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        expected = [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]
        text_extracted = extract_markdown_links(text)
        self.assertEqual(text_extracted, expected)

    def test_split_nodes_image(self):
        input_text = "not"
        text_split = "done"
        self.assertEqual()

if __name__ == "__main__":
    unittest.main()