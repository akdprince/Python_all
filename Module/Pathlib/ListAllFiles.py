from pathlib import Path

# List all files in a directory using pathlib

# dir = Path("/home/anik/lab/python/Module")

# for item in dir.iterdir():
#     print(item)

# List only files in the current directory (skips subfolders)

directory = Path("/home/anik/lab/python/Module")


files = [item for item in directory.iterdir() if item.is_file()]

for file in files:
    print(file.name)