import os

# path is not correct yet
# template path and dest path are not done yet either
CONTENT = os.path.join("content", "index.md")


def main():
    extracted = extract_title("# hello")
    print(extracted)


def extract_title(markdown: str):
    markdown = markdown.lstrip()
    if markdown.startswith("# "):
        title = markdown[2:].strip()
        return title
    else:
        raise ValueError("There's no h1 header")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")


main()
