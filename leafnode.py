class LeafNode(HTMLNode):

    def __init__(self, value, tag=None, props=None):
        super().__init__(value, tag, None, props)

    # def to_html(self):
    #     if self.value is None:
    #         raise ValueError("value is None")
    #     if self.tag is None:
    #         return self.value
    #     return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"

    def to_html(self):
        return "Test"
        