import psutil

# Get virtual memory details
memory = psutil.virtual_memory()

# Display memory information
print("Memory Information:\n")
print("Total Memory     :", memory.total // (1024**3), "GB")
print("Used Memory      :", memory.used // (1024**3), "GB")
print("Available Memory :", memory.available // (1024**3), "GB")
