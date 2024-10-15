import os
import shutil

def copy_and_sort_files(src_dir, dest_dir):
    try:
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        for item in os.listdir(src_dir):
            item_path = os.path.join(src_dir, item)

            if os.path.isdir(item_path):
                copy_and_sort_files(item_path, dest_dir)
            else:
                file_extension = os.path.splitext(item)[1][1:]  
                if not file_extension:
                    file_extension = "no_extension"

                extension_dir = os.path.join(dest_dir, file_extension)
                if not os.path.exists(extension_dir):
                    os.makedirs(extension_dir)

                shutil.copy2(item_path, extension_dir)

    except Exception as e:
        print(f"Error occurred while processing {src_dir}: {e}")

def main():
    src_dir = input("Please provide the source directory path: ")
    dest_dir = input("Please provide the destination directory path (default is 'dist'): ")

    if not dest_dir:
        dest_dir = "dist"

    if not os.path.exists(src_dir):
        print(f"Source directory '{src_dir}' does not exist.")
        return

    if not os.path.isdir(src_dir):
        print(f"Source path '{src_dir}' is not a directory.")
        return

    copy_and_sort_files(src_dir, dest_dir)
    print(f"Files have been copied and sorted in '{dest_dir}'.")

if __name__ == "__main__":
    main()