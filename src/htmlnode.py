class HTMLNode:
    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        children: list["HTMLNode"] | None = None,
        props: dict[str, str] | None = None,
    ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self) -> str:
        if self.props is None:
            return ""
        props_html = ""
        for key, value in self.props.items():
            props_html += f' {key}="{value}"'
        return props_html

    def __repr__(self) -> str:
        return f""" HTMLNode:
tag: {self.tag}
value: {self.value}
children: {self.children}
props: {self.props}"""


class LeafNode(HTMLNode):
    def __init__(
        self,
        tag: str | None,
        value: str,
        props: dict[str, str] | None = None,
    ):
        super().__init__(tag, value, None, props=props)

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("invalid HTML: no value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
        return f""" LeafNode:
tag: {self.tag}
value: {self.value}
props: {self.props}"""


class ParentNode(HTMLNode):
    def __init__(
        self,
        tag: str,
        children: list[HTMLNode],
        props: dict[str, str] | None = None,
    ):
        super().__init__(tag, children=children, props=props)

    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError("invalid ParentNode: needs tag")

        if self.children is None:
            raise ValueError("ParentNode missing children")

        # parent's tag
        opening_tag = f"<{self.tag}{self.props_to_html()}>"
        closing_tag = f"</{self.tag}>"

        # concatenating string
        children_html = ""

        for child in self.children:
            children_html += child.to_html()

        return opening_tag + children_html + closing_tag

    def __repr__(self) -> str:
        return f""" ParentNode:
tag: {self.tag}
children: {self.children}
props: {self.props}"""


"""
def main():
    dummy_tag = "a"
    dummy_value = "dummy text"
    dummy_props = {
        "href": "https://www.google.com",
        "target": "_blank",
    }

    # htmlnode = HTMLNode(props=dummy_props)
    leafnode = LeafNode(dummy_tag, dummy_value, props=dummy_props)
    normalleaf = LeafNode(None, "normal")
    parentnode1 = ParentNode(
        "p",
        [
            leafnode,
            leafnode,
            normalleaf,
        ],
    )

    parentnode = ParentNode(
        "span",
        [
            leafnode,
            parentnode1,
            leafnode,
            parentnode1,
        ],
    )
    print("ParentNode: ", end="")
    print(parentnode.to_html())


main()
"""
