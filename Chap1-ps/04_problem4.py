#WAP to print the contents od a directory using the os module.Search online for the function that does that
import os

# Specify the directory path (use '.' for the current working directory)
dir_path = '/'

try:
    # Get the list of all files and directories in the specified path
    contents = os.listdir(dir_path)
    
    print(f"Contents of '{dir_path}':")
    for item in contents:
        print(item)
        
except FileNotFoundError:
    print(f"The directory '{dir_path}' does not exist.")
except PermissionError:
    print(f"Permission denied to access '{dir_path}'.")