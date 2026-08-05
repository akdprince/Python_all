import os
import platform
import psutil

print("--- WSL Server Information ---")
print(f"System: {platform.system()}")
print(f"Release (Kernel): {platform.release()}")

# Indent all psutil commands inside the true condition block
if True:
    print("\n--- Hardware & Usage ---")
    print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")
    mem = psutil.virtual_memory()
    print(f"Total RAM: {mem.total / (1024**3):.2f} GB")
