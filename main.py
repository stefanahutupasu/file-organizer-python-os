import os
import shutil


def organize_files(root_dir):
    # Traverse through the directory and its subdirectories
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for file in filenames:
            file_path = os.path.join(dirpath, file)

            # Check if the file_path is a valid file
            if os.path.isfile(file_path):
                # Get the file extension
                extension = file.split('.')[-1]

                # Create destination directory based on the file extension
                dest_dir = os.path.join(root_dir, extension.capitalize() + " Files")

                # Create the destination directory if it doesn't exist
                os.makedirs(dest_dir, exist_ok=True)

                # Move the file to the destination directory
                shutil.move(file_path, os.path.join(dest_dir, file))


if __name__ == "__main__":
    # Prompt user for the directory they want to organize
    root_dir = input("Enter the path of the directory you want to organize: ")

    # Check if the entered directory path exists
    if os.path.exists(root_dir):
        # Call the organize_files function
        organize_files(root_dir)
        print("Files organized successfully!")
    else:
        print("Invalid directory path.")
