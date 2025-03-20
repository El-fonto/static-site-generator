import os
import shutil

# TODO: recursive functions that.

# check if path exists
#
#


def main():
    path = "~/workspace/github.com/El-fonto/static-site-generator/public/"

    print(os.path.isfile(path))
    # first: delete contents of public
    check = os.path.exists(path)
    print(check)

    if check:
        shutil.rmtree(path)
        print(check)
    # new things


main()
