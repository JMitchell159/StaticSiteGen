class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError()
    
    def __eq__(self, other):
        return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props
    
    def props_to_html(self):
        result = ""
        if self.props != None:
            for p in self.props:
                result += f" {p}=\"{self.props[p]}\""
        return result
    
    def __repr__(self):
        return f"tag: {self.tag}\nvalue: {self.value}\nchildren: {self.children}\nprops: {self.props}"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props=props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf nodes must have a value.")
        elif self.tag == None:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children=children, props=props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("All parent nodes must have a tag")
        elif self.children == None:
            raise ValueError("All parent nodes must have at least one child")
        else:
            result = f"<{self.tag}>"
            for c in self.children:
                result += c.to_html()
            result += f"</{self.tag}>"
            return result