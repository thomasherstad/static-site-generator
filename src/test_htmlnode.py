import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("p", "Hello World!", None, {"href": "https://www.google.com", "target": "_blank"})
        expected_html = " href=https://www.google.com target=_blank"
        self.assertEqual(node.props_to_html(), expected_html)

    def test_repr(self):
        node = HTMLNode("p", "Hello World!", None, {'href': 'https://www.google.com', 'target': '_blank'})
        expected = "HTMLNode(p, Hello World!, None, {'href': 'https://www.google.com', 'target': '_blank'})"
        self.assertEqual(node.__repr__(), expected) 


    def test_to_html_leaf_simple(self):
        node = LeafNode("p", "This is a paragraph of text.")
        html = node.to_html()
        expected = "<p>This is a paragraph of text.</p>"
        self.assertEqual(html, expected)

    def test_to_html_leaf_complex(self):
        node = LeafNode("a", "Click me!", {'href': 'https://www.google.com'})
        html = node.to_html()
        expected = "<a href=https://www.google.com>Click me!</a>"
        self.assertEqual(html, expected)
    
    def test_no_tag_leaf(self):
        node = LeafNode(None, "Click me!", {'href': 'https://www.google.com'})
        self.assertEqual(node.to_html(), "Click me!")
    
    def test_parent(self):
        node = ParentNode("p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text")
            ])

        html = node.to_html()
        expected = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(html, expected)

    def test_parent_complex(self):
        node = ParentNode("div", [
            LeafNode("h1", "Hello world"),
            ParentNode("div",
                       [ParentNode("div",
                                          [LeafNode("p", "Hello world again!")],
                                          )])
        ])
        html = node.to_html()
        expected = "<div><h1>Hello world</h1><div><div><p>Hello world again!</p></div></div></div>"
        self.assertEqual(html, expected)

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )


if __name__ == "__main__":
    unittest.main()

