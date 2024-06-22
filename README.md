# File Organizer

This project organizes files within a specified directory based on their file extensions. It creates sub-folders corresponding to each unique file extension found in the directory.

## Features

- **Organization by Extension:** Files like `ReadMe.txt` are moved to a `txt` folder, while `main.py` would go to a `.py` folder.
- **Folder Creation:** Sub-folders are automatically created for each extension found in the directory.
- **Overwrite Option:** Users can choose to overwrite existing files with the same name within a sub-folder (`yes`), or skip moving them (`no`).
- **Terminal Messages:** Detailed messages are printed to the terminal to indicate the actions taken, including file movements and any encountered errors.

## Usage

```bash
make ARGS='/path/to/directory yes'


- Made primarily for and test on Linux, Ubuntu. Unaware of functionality on other OS
