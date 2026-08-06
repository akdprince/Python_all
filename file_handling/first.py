#This is file handling task
#mode: r - read , w - write , a - append 

#open file
from os import read


# file = open("/home/anik/python/Python_all/file_handling/test.txt", "r")

# read file
# file = open("/home/anik/python/Python_all/file_handling/test.txt", "r")
# content = file.read()
# print(content)
# file.close() #best practice to close the file after reading

#read first line

# file = open("/home/anik/python/Python_all/file_handling/test.txt", "r")
# content = file.readline() #only print first line
# print(content)
# file.close()


#read all lines in list

# file = open("/home/anik/python/Python_all/file_handling/test.txt", "r")
# content = file.readlines() #read all lines in list
# print(content)
# file.close()

#Write to a file

# file = open("/home/anik/python/Python_all/file_handling/test2.txt", "w") #if file not exist it will create new file
# file.write("Hare Rama Hare Krishna\n")
# file.write("Hare Krishna Hare Rama\n")
# print("Writing to a file is done")
# file.close()

# print("-----After Writing to a File-----")

# #after writing to a file we can read the file using with statement
# print("Reading the file after writing to it")
# with open("/home/anik/python/Python_all/file_handling/test2.txt", "r") as file:
#     content = file.read()
#     print(content)

#  Append mode trying

file = open("/home/anik/python/Python_all/file_handling/test2.txt", "a") #if file not exist it will create new file with existing data
file.write("\nRadha Radha Radha\n")
file.write("Radhe Radhe Radhe\n")
file.close()

#After Appeding to a file showing result

with open("/home/anik/python/Python_all/file_handling/test2.txt", "r") as file:
    content = file.read()
    print(content)

#Close a file using with statement

# with open("/home/anik/lab/Files/new.txt", "r") as file:
#     content = file.readlines()
#     print(content)