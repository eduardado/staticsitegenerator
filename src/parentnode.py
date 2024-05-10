from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    
    def __init__(self, children, tag=None, props=None):
        super().__init__(None, tag, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Parent nodes need a tag")
        if len(self.children) == 0:
            raise ValueError("Parent nodes need children")
        result = f"<{self.tag}></{self.tag}>"
        return result
        
