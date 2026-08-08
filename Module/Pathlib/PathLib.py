from pathlib import Path

# #Showing the current working directory
current_dir = Path.cwd()
# print(f"Current Working Directory: {current_dir}")

# #Showing the Home Directory
# home_dir = Path.home()
# print(f"Home Directory: {home_dir}")


# Join paths using the / operator
# config_path = current_dir / "settings" / "config.json" / "anik"
# print(config_path)

#Checking if a path exists or not
# path_to_check = Path("/home/anik/python/test.py")
# print(path_to_check.exists())  # True if the path exists, False otherwise
# print(path_to_check.is_file())  # True if it's a file
# print(path_to_check.name) # Get the name of the file or directory
# print(path_to_check.suffix) # Get the file extension
# print(path_to_check.parent) # Get the parent directories

project_dir = Path(".")

# Find all Python files in the current folder
for py_file in project_dir.glob("*.py"):
    print(py_file.name) #Showing only file name with extension

# Recursively find all text files in current directory + subdirectories
for txt_file in project_dir.rglob("*.txt"):
    print(txt_file) #Showing parent folder + file name with extension