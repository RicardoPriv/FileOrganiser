import os
import shutil

#Retrieve list of file names in a directory.
def get_file_names(directory: str) -> list:
    return [file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]

#Extract unique file extensions from a list of file names.
def get_file_extensions(file_names: list) -> list:
    file_extensions = set()  # Using a set to automatically handle duplicates
    for file in file_names:
        extension = os.path.splitext(file)[1]
        if extension:
            file_extensions.add(extension[1:])  # Remove the leading period
    return list(file_extensions)

#Create folders for each unique file extension.
def create_folders(folder_names: list, directory: str) -> list:
    new_directories = []
    for folder_name in folder_names:
        new_folder = os.path.join(directory, folder_name)
        os.makedirs(new_folder, exist_ok=True)
        new_directories.append(new_folder)
    return new_directories

#Move files to their respective folders based on file extension.
def move_files(file_names: list, current_directory: str, new_directories: list, overwrite: bool):
    for file_name in file_names:
        if file_has_extension(file_name):
            extension = file_name.split('.')[-1]  # Get the last part after the last dot
            for directory in new_directories:
                folder = os.path.basename(directory.strip())
                if folder == extension:
                    source_file = os.path.join(current_directory, file_name.strip())
                    destination_file = os.path.join(directory, file_name.strip())
                    if overwrite and os.path.exists(destination_file):
                        print(f"Moving '{source_file}' to '{directory}'")
                        try:
                            os.remove(destination_file)  # Remove existing file before moving
                            shutil.move(source_file, destination_file)
                        except Exception as e:
                            print(f"Error moving file '{source_file}' to '{destination_file}': {e}")
                        print("")
                    else:
                        print(f"Moving '{source_file}' to '{directory}'")
                        try:
                            shutil.move(source_file, directory)
                        except shutil.Error as e:
                            print(f"Error: {e}")
                        print("")
                    break
        else:
            print(f"File '{file_name}' has no extension or is a hidden file. Skipping.\n")

    return

#Check if a file has an extension.
def file_has_extension(file: str) -> bool:
    return '.' in file and not file.startswith('.')

#Organize files in a directory based on their extensions.
def organise_files(directory: str, overwrite: bool):
    file_names = get_file_names(directory)
    file_extensions = get_file_extensions(file_names)
    folder_names = create_folders(file_extensions, directory)
    move_files(file_names, directory, folder_names, overwrite)
    return