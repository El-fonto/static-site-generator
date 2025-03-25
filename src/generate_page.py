import os
from markdown_blocks import markdown_to_html_node


def extract_title(markdown: str):
    markdown_lines = markdown.split("\n")

    if not markdown_lines:
        raise ValueError("There's no h1 header")

    first_line = markdown_lines[0].lstrip()

    if first_line.startswith("# "):
        title = first_line[2:].strip()
        return title
    else:
        raise ValueError("There's no h1 header")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as c, open(template_path, "r") as t:
        markdown = c.read()
        template_html = t.read()

    content_node = markdown_to_html_node(markdown)
    html_content = content_node.to_html()

    title = extract_title(markdown)
    title_added = template_html.replace(r"{{ Title }}", title)
    contented_added = title_added.replace(r"{{ Content }}", html_content)

    dest_dir = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    with open(dest_path, "w") as d:
        d.write(contented_added)
