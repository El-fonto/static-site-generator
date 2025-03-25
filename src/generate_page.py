import os
from pathlib import Path
from markdown_blocks import markdown_to_html_node


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for file in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, file)
        dest_path = os.path.join(dest_dir_path, file)

        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, str(dest_path), basepath)
        else:
            generate_pages_recursive(from_path, template_path, dest_path, basepath)


def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as c, open(template_path, "r") as t:
        markdown = c.read()
        template_html = t.read()

    content_node = markdown_to_html_node(markdown)
    html_content = content_node.to_html()

    title = extract_title(markdown)
    template = template_html.replace(r"{{ Title }}", title)
    template = template.replace(r"{{ Content }}", html_content)

    basepath = basepath.rstrip("/") + "/"
    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')

    dest_dir = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir, exist_ok=True)

    with open(dest_path, "w") as d:
        d.write(template)


def extract_title(markdown: str):
    markdown_lines = markdown.split("\n")

    if not markdown_lines:
        raise ValueError("There's no h1 header")

    for line in markdown_lines:
        line = line.lstrip()
        if line.startswith("# "):
            return line[2:].strip()
    raise ValueError("There's no h1 header")
