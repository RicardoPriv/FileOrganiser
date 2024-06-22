Note: This is a self project that was done for and tested on Linux, Ubuntu. Unaware if it functions on other OS.


Given a directory and a yes/no option, this project will organise all files with an extension into sub-folders marked with said extension
  eg: ReadMe.txt will be placed within the txt folder, main.py will be placed within the .py folder and so on.

All sub-folders are created within the directory to be organised.
The option for yes or no allows for overwriting files with the same name already within a sub-folder
So if say you already ran this program, root/txt/ReadMe.txt exists and now you've created a new root/ReadMe.txt
  -> yes will move root/ReadMe.txt into root/txt and overwrite the ReadMe in said file
  -> no will not move root/ReadMe.txt and leave it be
Messages are printed to terminal for identifying what is happening eg: moving and errors

Usage:
  make ARGS='/path/to/directory/to/organise yes'
