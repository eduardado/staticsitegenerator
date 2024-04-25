class HTMLNode:
    def __init__(self=None, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        attributes = ""
        for key, value in self.props.items():
            attributes += " "
            attributes += f'{key}="{value}"'
        return attributes
    
    def __repr__(self):
        return f"HTMLNode\n tag={self.tag}; value={self.value}; children={self.children}; props={self.props}"
    