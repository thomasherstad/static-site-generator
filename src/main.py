from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode


def main():
    a = TextNode("This is an image node", "image", "https://boot.dev")
    b = a.__repr__    
    print(a)

main()