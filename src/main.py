import os
import sys
import shutil
from copystatic import copy_file_recursive
from generate_page import generate_pages_recursive


DOCS_PATH = "./docs"
STATIC_PATH = "./static"
CONTENT_PATH = "./content"
TEMPLATE_PATH = "./template.html"


def main():
    if len(sys.argv) > 1:
        BASE_PATH = sys.argv[1]
    else:
        BASE_PATH = "/"

    print("Deleting docs directory...")
    if os.path.exists(DOCS_PATH):
        shutil.rmtree(DOCS_PATH)

    print("Copying static files to docs directory")
    copy_file_recursive(STATIC_PATH, DOCS_PATH)

    print("Generating pages...")
    generate_pages_recursive(CONTENT_PATH, TEMPLATE_PATH, DOCS_PATH, BASE_PATH)


main()
