import psutil

# Get disk partitions
partitions = psutil.disk_partitions()

print("Disk Partitions and Usage Information:\n")

for partition in partitions:
    print("Device:", partition.device)
    print("Mount Point:", partition.mountpoint)
    print("File System Type:", partition.fstype)
    
    try:
        usage = psutil.disk_usage(partition.mountpoint)
        print("Total Size:", usage.total // (1024**3), "GB")
        print("Used:", usage.used // (1024**3), "GB")
        print("Free:", usage.free // (1024**3), "GB")
        print("Usage Percentage:", usage.percent, "%")
    except PermissionError:
        print("Permission Denied")
    
    print("-" * 40)
