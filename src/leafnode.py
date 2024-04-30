from htmlnode import HTMLNode
class LeafNode(HTMLNode):

    def __init__(self, value, tag=None, props=None):
        super().__init__(value, tag, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes require a value")
        if self.tag is None:
            return self.value

        attributes = self.props_to_html()
        return f"<{self.tag}{attributes}>{self.value}</{self.tag}>"
