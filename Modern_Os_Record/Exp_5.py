import psutil

# Get network I/O statistics
net_stats = psutil.net_io_counters()

# Display network statistics
print("Network Statistics:\n")
print("Bytes Sent     :", net_stats.bytes_sent)
print("Bytes Received :", net_stats.bytes_recv)
