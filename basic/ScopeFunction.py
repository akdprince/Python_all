# ram_count = 16  # Global variable

# def upgrade_ram():
#     ram_count = 32  # Python thinks this is a NEW local variable!
#     print(f"Inside: {ram_count}") # Output: Inside: 32

# upgrade_ram()
# print(f"Outside: {ram_count}")    # Output: Outside: 16 (Global didn't change!)

def check_disk(path="/"):
    disk_path = path  # Local variable
    return disk_path

print(check_disk())          # Uses default: Checking disk at: /
print(check_disk("/home/anik"))  # Overrides default: Checking disk at: /home/anik