import shutil

total , free , used = shutil.disk_usage("/")

print("WSL disk usage with shutil")
print(f"Total Space: {total / (1024**3):.2f} GB")
print(f"Total Usage: {used / (1024**3):.2f} GB")
print(f"Total Free: {free / (1024**3):.2f} GB")

Disk_usage = (used / total)* 100

# print(Disk_usage)

if(Disk_usage >= 80):
    print(f"Warning your disk usage is so high {(Disk_usage):.1f} %")
else:
    print("Healthy")