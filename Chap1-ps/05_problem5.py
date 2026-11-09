#Write program 4 with comments
import os

# Enter the path of the folder youn want the contents of.
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