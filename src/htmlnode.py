class HtmlNode:
    def __init__(self, tag=None, value="", children=[], props={}):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props == None:
            return ""
        html = ""
        for key, value in self.props.items():
            if type(value) == str:
                html += f" {key}=\"{value}\""
            elif type(value) == dict:
                html += f" {key}=\""
                for k, v in value.items():
                    html += f"{k}: {v} "
                html = html.strip() + '"'

        return html

    def __repr__(self):
        return f"HtmlNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    
class LeafNode(HtmlNode):
    def __init__(self, tag=None, value="", props={}):
        super().__init__(tag, value, props=props)

    def to_html(self):
        if self.value == "":
            raise ValueError("Invalid HTML: no value")
        if self.tag == None:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
class ParentNode(HtmlNode):
    def __init__(self, tag=None, children=[], props={}):
        super().__init__(tag, children=children, props=props)

    def to_html(self):
        if len(self.children) == 0:
            raise ValueError("Invalid HTML: parent node has no children")
        if self.tag == None:
            raise ValueError("Invalid HTML: parent node has no tag")
        children = ""
        for child in self.children:
            children += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children}</{self.tag}>"


    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"