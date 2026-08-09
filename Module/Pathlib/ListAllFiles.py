# from pathlib import Path

# path = Path("/home/anik/lab/python/Module")

# for item in path.iterdir():
#     print(item)

from pathlib import Path

# Path to directory
directory = Path("/home/anik/lab/python/Module")

# List only files in the current directory (skips subfolders)
files = [item for item in directory.iterdir() if item.is_file()]

for file in files:
    print(file.name)