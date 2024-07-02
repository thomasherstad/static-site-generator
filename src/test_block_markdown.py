import unittest
from block_markdown import markdown_to_block

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_block(self):
        input_text = '''This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items'''
        output = markdown_to_block(input_text)
        expected = ['This is **bolded** paragraph', 'This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line', '* This is a list\n* with items']
        self.assertEqual(output, expected)

    def test_markdown_to_block2(self):
        input_text = '''This is **bolded** paragraph



This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items'''
        output = markdown_to_block(input_text)
        expected = ['This is **bolded** paragraph', 'This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line', '* This is a list\n* with items']
        self.assertEqual(output, expected)
