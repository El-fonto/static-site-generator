class HTMLNode:
    def __init__(
        self,
        tag: str = None,
        value: str = None,
        children: list[str] = None,
        props: dict[str, str] = None,
    ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return ""
        html_string = ""
        for key, value in self.props.items():
            html_string += f' {key}="{value}"'
        return html_string

    def __repr__(self):
        return f""" HTMLNode:
tag: {self.tag}
value: {self.value}
children: {self.children}
props: {self.props}"""


class LeafNode(HTMLNode):
    def __init__(
        self,
        tag: str,
        value: str,
        props: dict[str, str] = None,
    ):
        super().__init__(tag, value, children=None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("invalid HTML: no value")
        elif self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f""" LeafNode:
tag: {self.tag}
value: {self.value}
props: {self.props}"""


class ParentNode(HTMLNode):
    def __init__(
        self,
        tag: str,
        children: list[str],
        props: dict[str, str] = None,
    ):
        super().__init__(tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode needs tag")
        elif len(self.children) == 0:
            raise ValueError("ParentNode needs to have children")
        return f""


"""
def main():
    dummy_tag = "a"
    dummy_value = "dummy text"
    dummy_props = {
        "href": "https://www.google.com",
        "target": "_blank",
    }

    htmlnode = HTMLNode(props=dummy_props)

    leafnode = LeafNode(dummy_tag, dummy_value, props=dummy_props)

    print("HTMLNode: ", end="")
    print(htmlnode.props_to_html())

    print("LeafNode: ", end="")
    print(leafnode.to_html())


main()
"""
