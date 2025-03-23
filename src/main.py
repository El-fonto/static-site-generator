import os
from copystatic import copy_file_recursive


def main():
    PUBLIC_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "public")
    STATIC_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static")

    # traverse directory
    copy_file_recursive(STATIC_PATH, PUBLIC_PATH)


main()
