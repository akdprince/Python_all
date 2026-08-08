#This is file handling task
#mode: r - read , w - write , a - append 

#open file
# file = open("test.txt", "r")

#read file
# file = open("test.txt", "r")
# content = file.read()
# print(content)
# file.close() #best practice to close the file after reading

#read first line

# file = open("test.txt", "r")
# content = file.readline() #only print first line
# print(content)
# file.close()


#read all lines in list

# file = open("test.txt", "r")
# content = file.readlines() #read all lines in list
# print(content)
# file.close()

#Write to a file

# file = open("test2.txt", "w") #if file not exist it will create new file
# file.write("Hare Rama Hare Krishna\n")
# file.write("Hare Krishna Hare Rama\n")
# file.close()

#  Append mode trying

# file = open("test2.txt", "a") #if file not exist it will create new file
# file.write("\nRadha Radha Radha\n")
# file.write("Radhe Radhe Radhe\n")
# file.close()

#Close a file using with statement

with open("/home/anik/lab/Files/new.txt", "r") as file:
    content = file.readlines()
    print(content)