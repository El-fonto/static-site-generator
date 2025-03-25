import os
from pathlib import Path
from markdown_blocks import markdown_to_html_node


def extract_title(markdown: str):
    markdown_lines = markdown.split("\n")

    if not markdown_lines:
        raise ValueError("There's no h1 header")

    for line in markdown_lines:
        if line.startswith("# "):
            return line[2:].strip()
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
        os.makedirs(dest_dir, exist_ok=True)

    with open(dest_path, "w") as d:
        d.write(contented_added)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    content_dirs = os.listdir(dir_path_content)
    for file in content_dirs:
        content_full_path = os.path.join(dir_path_content, file)
        destination_full_path = os.path.join(dest_dir_path, file)

        if os.path.isfile(content_full_path):
            content_path = Path(content_full_path)
            if content_path.suffix.lower() == "md":
                dest_path = Path(destination_full_path)
                dest_path = dest_path.with_suffix(".html")
                generate_page(content_full_path, template_path, str(dest_path))
        else:
            generate_pages_recursive(
                content_full_path, template_path, destination_full_path
            )
