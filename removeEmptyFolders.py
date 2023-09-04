import os

def remove_empty_folders(directory):
    problematic_folders = []  # List to store names of problematic folders

    for root, dirs, files in os.walk(directory, topdown=False):
        for dir_name in dirs:
            folder_path = os.path.join(root, dir_name)
            if not os.listdir(folder_path):
                # If the folder is empty, remove it
                try:
                    os.rmdir(folder_path)
                    print(f"Removed empty folder: {folder_path}")
                except Exception as e:
                    print(f"Error removing folder {folder_path}: {str(e)}")
            else:
                # If the folder is not empty, add its name to the list of problematic folders
                problematic_folders.append(folder_path)

    if problematic_folders:
        print("\nProblematic folders (non-empty):")
        for folder in problematic_folders:
            print(folder)

if __name__ == "__main__":
    directory_path = input("Enter the path of the directory to remove empty folders from: ")
    remove_empty_folders(directory_path)
