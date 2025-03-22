import os
import shutil

# TODO: recursive functions that.

# check if path exists
#
#


def main():
    PUBLIC_PATH = (
        "/home/fonto/workspace/github.com/El-fonto/static-site-generator/public/"
    )
    STATIC_PATH = (
        "/home/fonto/workspace/github.com/El-fonto/static-site-generator/static/"
    )

    # handling destination directory
    public_exists = os.path.exists(PUBLIC_PATH)
    if not public_exists:
        print(f"=== {PUBLIC_PATH} === didn't exist")
        os.mkdir(PUBLIC_PATH)
        print("path made")
    if public_exists:
        print(f"=== {PUBLIC_PATH} === DELETED")
        # delete contents of path
        shutil.rmtree(PUBLIC_PATH)
    #
    # traverse directory
    static_content = os.listdir(STATIC_PATH)

    print(static_content)
    for file in static_content:
        if os.path.isfile(f"{STATIC_PATH}{file}"):
            print(f"match {file}")
            shutil.copy(STATIC_PATH, PUBLIC_PATH)
        if os.path.isdir(f"{STATIC_PATH}{file}"):
            # recursion needs work
            print(f"this is a directory: {file}")


main()
