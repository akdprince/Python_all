import subprocess

# subprocess.run("ls -la", shell=True) #first process
# p1 =  subprocess.run(["ls", "-la"]) #second process
# print(p1)

#below code will create a file output.txt and write the output of the command "ls -la" into that file

with open("/home/anik/lab/python/Module/SubProcess/output.txt", "a") as f:
    p1 = subprocess.run(["ls", "-la"], stdout=f, text=True) #third process

# Show result from the first output file to the second output file and check data with input from the first output file

# p1 = subprocess.run(["cat", "/home/anik/lab/python/Module/SubProcess/output.txt"], capture_output=True, text=True) # Capture output in p1

# print(p1.stdout)  # Print the captured output

# p2 = subprocess.run(["grep", "-n", "anik"], capture_output=True, text=True, input=p1.stdout)  # Use p1's output as input for p2

# print(p2.stdout)  # Print the output of the second process