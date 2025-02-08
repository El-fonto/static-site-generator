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


# def main():
# dummy_props = { "href": "https://www.google.com", "target": "_blank", }

# node = HTMLNode(props=dummy_props)

# print(node.props_to_html())
