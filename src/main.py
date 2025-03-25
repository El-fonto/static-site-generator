import os
import sys
import shutil
from copystatic import copy_file_recursive
from generate_page import generate_pages_recursive


PUBLIC_PATH = "./public"
STATIC_PATH = "./static"
CONTENT_PATH = "./content"
TEMPLATE_PATH = "./template.html"


def main():
    if len(sys.argv) > 1:
        BASE_PATH = sys.argv[1]
    else:
        BASE_PATH = "/"

    print("Deleting public directory...")
    if os.path.exists(PUBLIC_PATH):
        shutil.rmtree(PUBLIC_PATH)

    print("Copying static files to public directory")
    copy_file_recursive(STATIC_PATH, PUBLIC_PATH)

    print("Generating pages...")
    generate_pages_recursive(CONTENT_PATH, TEMPLATE_PATH, PUBLIC_PATH, BASE_PATH)


main()
