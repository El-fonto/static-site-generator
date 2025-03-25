import os
import shutil
from copystatic import copy_file_recursive
from generate_page import generate_page

PUBLIC_PATH = "./public"
STATIC_PATH = "./static"
CONTENT_INDEX = os.path.join("content", "index.md")
TEMPLATE = os.path.join("template.html")
DESTINATION_FILE = os.path.join("public", "index.html")


def main():
    print("Deleting public directory...")
    if os.path.exists(PUBLIC_PATH):
        shutil.rmtree(PUBLIC_PATH)

    print("Copying static files to public directory")
    copy_file_recursive(STATIC_PATH, PUBLIC_PATH)
    generate_page(CONTENT_INDEX, TEMPLATE, DESTINATION_FILE)


main()
