def main():
    title = extract_title("# Hello")
    print(f"1: {title}")

    title = extract_title("Hello")
    print(f"1: {title}")


def extract_title(markdown: str):
    try:
        if markdown.startswith("# "):
            title = markdown.strip("#").strip()
            return title
        else:
            raise ValueError("There's no h1 header")
    except ValueError as e:
        print(f"There's no h1 header: {e}")


main()
