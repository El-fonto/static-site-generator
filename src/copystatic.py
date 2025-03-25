import os
import shutil


def copy_file_recursive(from_path, dest_path):
    # handling destination directory
    if not os.path.exists(dest_path):
        try:
            os.mkdir(dest_path)
            print(f"Directory created: {dest_path}")
        except OSError as e:
            print(f"Error creating directory {dest_path}: {e}")
            return

    if len(os.listdir(from_path)) == 0:
        print("end of traversing")
        return
    origin_content = os.listdir(from_path)

    for file in origin_content:
        from_full_path = os.path.join(from_path, file)
        dest_full_path = os.path.join(dest_path, file)

        if os.path.isfile(from_full_path):
            shutil.copy(from_full_path, dest_full_path)
        else:
            copy_file_recursive(from_full_path, dest_full_path)
