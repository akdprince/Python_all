import subprocess
from datetime import datetime

# System_Up_time = subprocess.run(['uptime'], capture_output=True, text=True)
# Current_date = subprocess.run(["date"], capture_output=True, text=True)

# print(f"{System_Up_time} \n {Current_date}")

# print(System_Up_time.stdout.strip())
# print(Current_date.stdout.strip())

#---------Below Three command for system time with report , Disk free with report and Memory free with report ---------

# with open("/home/anik/lab/python/Module/SubProcess/SysTime.txt", "a") as f:
#     p1 = subprocess.run(["uptime"], stdout=f, text=True)

# with open("/home/anik/lab/python/Module/SubProcess/DiskFree.txt", "a") as f1:
#     p2 = subprocess.run(["df" , "-h"], stdout=f1, text=True)


# with open("/home/anik/lab/python/Module/SubProcess/MemoryFree.txt", "a") as f2:
#     p3 = subprocess.run(["free" , "-h"], stdout=f2, text=True )
    




#====== With date time and after run once line break for every check below=====

file_path = "/home/anik/lab/python/Module/SubProcess/MemoryFree.txt"
file_path2 = "/home/anik/lab/python/Module/SubProcess/SysTime.txt"
file_path3 = "/home/anik/lab/python/Module/SubProcess/DiskFree.txt"

# Get current timestamp in a readable format
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
crt_time = datetime.now().strftime("%Y_%m_%d %H_%M_%S")

#== Run the process before process the context manager

p1 = subprocess.run(["free", "-h"], capture_output=True, text=True)
p2 = subprocess.run(["uptime"], capture_output=True, text=True)
p3 = subprocess.run(["df", "-h"], capture_output=True, text=True)

with open(file_path, "a") as f:
    # 1. Write the dynamic timestamp header
    f.write(f"=== Memory Report: {current_time} ===\n")
    
    # 2. Append the memory check output
    f.write(p1.stdout)
    
    # 3. Add blank lines for clean separation between log entries
    f.write("\n\n")

with open(file_path2, "a") as f2:
    f2.write(f"=== System Uptime Report: {current_time} === \n")

    f2.write(p2.stdout)

    f2.write("\n\n")


with open(file_path3, "a") as f3:
    f3.write(f"=== Disk Free: {crt_time} === \n")

    f3.write(p3.stdout)

    f3.write("\n\n")
