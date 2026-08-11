import shutil

# # Copy a single file to another file
# shutil.copy2("/home/anik/python/Python_all/Module/Shutil/source.txt", "/home/anik/python/Python_all/Module/Shutil/backup_source.txt")

# # Copy an entire folder and its contents to a new folder
# shutil.copytree("/home/anik/lab/python/Module/Shutil/Test2", "/home/anik/lab/python/Module/Shutil/Test4")

# # Move a file or directory to a new location
# shutil.move("/home/anik/python/Python_all/Module/Shutil/Test/hello.txt", "/home/anik/python/Python_all/Module/Shutil/Test2/")

# # Delete a non-empty directory and all subfiles
# shutil.rmtree("/home/anik/python/Python_all/Module/Shutil/Test")

#Make a folder zip file
# shutil.make_archive("/home/anik/python/Python_all/Module/Shutil/backup", "zip", "/home/anik/python/Python_all/Module/Shutil/Test2")

#extract a zip file to a specified directory
# shutil.unpack_archive("/home/anik/python/Python_all/Module/Shutil/backup.zip", "/home/anik/python/Python_all/Module/Shutil/Test3")


# Check disk space on current drive
# total, used, free = shutil.disk_usage(".")
# print(f"Total free Space: {free}")
# print(f"Free space: {free // (2**30)} GB") # 2**30 means 2 to the power of 30, which is the number of bytes in a gigabyte.
    
# # Find where python or git executable is located
# print(shutil.which("git"))  # e.g., '/usr/bin/git'

#How to copy meta data to another file

shutil.copystat("/home/anik/lab/python/Module/Shutil/source.txt", "/home/anik/lab/python/Module/Shutil/backup_source.txt")  # Copy metadata from source.txt to backup_source.txt