class HTMLNode:
    def __init__(self, value=None, tag=None, children=None, props=None):
        self.value = value
        self.tag = tag
        self.children = [] if children is None else children
        self.props = {} if props is None else props

    def to_html(self):
        raise NotImplementedError("to_html() method not implemented")

    def props_to_html(self):
        attributes = ""
        for key, value in self.props.items():
            attributes += " "
            attributes += f'{key}="{value}"'
        return attributes
    
    def __repr__(self):
        return f"HTMLNode\n tag={self.tag}; value={self.value}; children={self.children}; props={self.props}"
    