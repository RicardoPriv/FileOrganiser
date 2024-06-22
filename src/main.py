import os
import sys
from file import organise_files

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <directory_path> [--overwrite]\n")
        return
    
    directory_path = sys.argv[1]
    overwrite = "--overwrite" in sys.argv

    if not os.path.exists(directory_path):
        print(f"Error: Directory '{directory_path}' does not exist.\n")
        return

    if not os.path.isdir(directory_path):
        print(f"Error: '{directory_path}' is not a valid directory.\n")
        return

    print(f"Organizing files in '{directory_path}'...\n")
    organise_files(directory_path, overwrite)
    print("File organization completed.\n")

if __name__ == "__main__":
    main()
