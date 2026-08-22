#=== This is our first project to get server inventory ===
import subprocess

host_name = subprocess.run(['hostname'], capture_output=True, text=True)

print(f"Hostname: {host_name.stdout}")

host_ip_address = subprocess.run(["hostname", "-I"], capture_output=True, text=True)

print(f"Host Ip Address: {host_ip_address.stdout}")

Full_cpu = subprocess.run(["lscpu"], capture_output=True, text=True)
find_model = subprocess.run(["grep", "Model name"], input=Full_cpu.stdout, capture_output=True, text=True)

CPU_Model = find_model.stdout.strip()
print(CPU_Model)

mem_path = "free -h | awk '/Mem:/ {print $7}'"

result = subprocess.run(mem_path, shell=True, capture_output=True, text=True)

availave_memory = result.stdout.strip()
print(f"Availave Memory: {availave_memory}")

disk_path = "df -h /"

disk_result = subprocess.run(disk_path, shell=True, capture_output=True, text=True)

print(f"Full Storage: \n{disk_result.stdout}")


