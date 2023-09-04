# Python script to sort files in a directory by their extensions
import os
import shutil

def sort_files(directory_path):
    if not os.path.exists(directory_path) or not os.path.isdir(directory_path):
        print(f"Directory '{directory_path}' does not exist.")
        return

    problematic_files = []  # List to store problematic file names

    for filename in os.listdir(directory_path):
        # Get the extension of the file
        file_path = os.path.join(directory_path, filename)
        if os.path.isfile(file_path):
            extension = filename.split(".")[-1]
            # Create a directory with the name of the extension if it doesn't exist
            destination_directory = os.path.join(directory_path, extension)
            if not os.path.exists(destination_directory):
                os.mkdir(destination_directory)
            # Move the file to the directory with the name of the extension
            destination_file = os.path.join(destination_directory, filename)

            try:
                shutil.move(file_path, destination_file)
                print(f"Moved {filename} to {destination_directory}")
            except Exception as e:
                print(f"Error moving {filename}: {str(e)}")
                problematic_files.append(filename)  # Add the problematic file to the list

    if problematic_files:
        print("\nProblematic files:")
        for file in problematic_files:
            print(file)
        # Optionally, you can save the list of problematic files to a file
        # with open("problematic_files.txt", "w") as file:
        #     file.write("\n".join(problematic_files))

if __name__ == "__main__":
    directory_path = input("Enter the path of the directory: ")
    sort_files(directory_path)

    