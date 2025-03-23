import os
import shutil


def copy_file_recursive(origin_path, destination_path):
    # handling destination directory
    if not os.path.exists(destination_path):
        try:
            os.mkdir(destination_path)
            print(f"Directory created: {destination_path}")
        except OSError as e:
            print(f"Error creating directory {destination_path}: {e}")
            return

    if len(os.listdir(origin_path)) == 0:
        print("end of traversing")
        return
    origin_content = os.listdir(origin_path)

    for file in origin_content:
        or_full_path = os.path.join(origin_path, file)
        dest_full_path = os.path.join(destination_path, file)

        if os.path.isfile(or_full_path):
            shutil.copy(or_full_path, dest_full_path)
        elif os.path.isdir(or_full_path):
            try:
                os.mkdir(dest_full_path)
                print(f"Directory created successfully: {dest_full_path}")
                copy_file_recursive(or_full_path, dest_full_path)
            except FileExistsError:
                print(f"Directory already exists: {dest_full_path}")
            except OSError as e:
                print(f"Error creating directory {dest_full_path}: {e}")
