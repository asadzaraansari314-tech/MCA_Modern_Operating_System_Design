import platform
import os
import sys
import psutil  # Optional: for more detailed info like memory and CPU usage

def display_system_info():
    print("===== Basic System Information =====\n")
    
    # OS and Platform info
    print(f"System: {platform.system()}")
    print(f"Node Name: {platform.node()}")
    print(f"Release: {platform.release()}")
    print(f"Version: {platform.version()}")
    print(f"Machine: {platform.machine()}")
    print(f"Processor: {platform.processor()}")
    print(f"Platform: {platform.platform()}\n")
    
    # Python info
    print("===== Python Information =====\n")
    print(f"Python Version: {platform.python_version()}")
    print(f"Python Compiler: {platform.python_compiler()}")
    print(f"Python Build: {platform.python_build()}\n")
    
    # CPU and memory info (optional)
    print("===== CPU & Memory Information =====\n")
    print(f"Number of CPUs: {psutil.cpu_count(logical=True)}")
    print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")
    memory = psutil.virtual_memory()
    print(f"Total Memory: {round(memory.total / (1024**3), 2)} GB")
    print(f"Available Memory: {round(memory.available / (1024**3), 2)} GB")
    print(f"Memory Usage: {memory.percent}%")

# Run the function
display_system_info()
