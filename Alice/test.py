import os
import shutil

def organize_md_files():
    # Get the current directory
    current_dir = os.getcwd()

    # Iterate over all files in the current directory
    for filename in os.listdir(current_dir):
        # Check if the file is a Markdown file and not a directory
        if filename.endswith(".md") and os.path.isfile(filename):
            # Extract the file name without the extension
            folder_name = os.path.splitext(filename)[0]
            # Create a folder with the same name if it doesn't exist
            folder_path = os.path.join(current_dir, folder_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            # Move the Markdown file to the created folder
            shutil.move(filename, folder_path)

if __name__ == "__main__":
    organize_md_files()
