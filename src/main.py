from textnode import TextNode
from texttype import TextType

def main():
    textNode = TextNode("This is a text node", TextType.BOLD, "http://www.boot.dev")
    textNode2 = TextNode("This is another text node", TextType.CODE)
    print(textNode.__repr__())
    print(textNode2.__repr__())

    print("__eq__() method test:")
    textNode3 = TextNode("This is another text node", TextType.CODE)
    print(f"textNode2 is equal to textNode3: {textNode3.__eq__(textNode2)}")
main()
