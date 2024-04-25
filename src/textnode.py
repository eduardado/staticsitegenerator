from texttype import TextType

class TextNode:

    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (self.text == other.text and
                self.text_type == other.text_type and
                self.url == other.url)
    
    def __repr__(self):
        text_type_str = self.text_type.name.lower() if self.text_type else 'None'
        return f"TextNode({self.text}, {text_type_str}, {self.url})"