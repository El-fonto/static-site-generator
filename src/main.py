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
            # shutil.copy(STATIC_PATH, PUBLIC_PATH)
        if os.path.isdir(f"{STATIC_PATH}{file}"):
            # recursion needs work
            print(f"this is a directory: {file}")


def copy_file(origin_path, destination_path):
    if len(os.listdir(origin_path)) == 0:
        return
    origin_content = os.listdir(origin_path)

    for file in origin_content:
        origin_file_path = f"{origin_path}{file}"
        destination_file_path = f"{destination_path}{file}"

        if os.path.isfile(origin_file_path):
            shutil.copy(origin_file_path, destination_file_path)
        elif os.path.isdir(origin_path):
            os.mkdir(file)
            copy_file(origin_file_path, destination_file_path)


main()
