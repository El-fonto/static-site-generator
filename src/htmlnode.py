class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag  # str
        self.value = value  # text content - str
        self.children = children  # list of children nodes
        self.props = (
            props  # dictionary tags-content / <a> {"href": "https://www.google.com"}
        )

    # child classes override this
    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for tag, attribute in self.props.items():
            props_html += f' {tag}="{attribute}"'
        return props_html

    def __repr__(self) -> str:
        return f"HTMLNode: ({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, children=None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

    def __eq__(self, other):
        return (
            self.tag == other.tag
            and self.value == other.value
            and self.props == other.props
        )


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag is necessary")
        if self.children is None:
            raise ValueError("Parent node needs children nodes")
        if not self.children:
            return f"<{self.tag}{self.props_to_html()}></{self.tag}>"

        children_html = ""
        # base case
        for child in self.children:
            # child needs to be a HTMLNode or a LeafNode object
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def __repr__(self) -> str:
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
