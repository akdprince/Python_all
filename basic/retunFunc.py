# def calculate_mb(gb_value):
#     result = gb_value * 1024
#     return result  # This sends the number back to the program

# # You can now save that returned answer into a new variable
# my_ram_mb = calculate_mb(16)

# print(f"I have {my_ram_mb} MB of RAM.")  # Output: I have 16384 MB of RAM.

# def say_hello():
#     print("Hello!")

# result = say_hello()
# print(result)  # Output: None (because nothing was explicitly returned)


server_ip = "192.168.1.1"  # Global variable

def print_ip():
    print(server_ip)       # Works! The function can read global variables

print_ip()  # Output:

print(f"My server ip: ",server_ip)  # Works! The global variable is still accessible outside the function``