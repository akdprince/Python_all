# def greet(name):
#     print(f"Hello {name}")

# greet("Anik")

# def user_info(name, age):
#     print(f"{name} is {age} years old.")

# user_info("Anik", 25)  # Output: Anik is 25 years old.
# user_info(25, "Anik")  # Output: 25 is Anik years old. (Wrong order!)

# 'path' has a default value of "/"
# def check_disk(path="/"):
#     print(f"Checking disk at: {path}")

# check_disk()          # Uses default: Checking disk at: /
# check_disk("/home/anik")  # Overrides default: Checking disk at: /mnt/c

def sum_disk_sizes(*sizes):
    total = sum(sizes)
    print(f"Total: {total} GB")

sum_disk_sizes(10, 20, 50, 5)  # Output: Total: 85 GB