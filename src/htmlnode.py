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
        if not isinstance(self.props, dict):
            raise TypeError("props must be a dictionary")

        html = " "
        for tag, attribute in self.props.items():
            html += f'{tag}="{attribute}" '
        return html

    def __repr__(self) -> str:
        return f"HTMLNode: ({self.tag}, {self.value}, {self.children}, {self.props})"
