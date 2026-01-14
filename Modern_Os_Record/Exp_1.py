import platform

# Get OS details
os_name = platform.system()
os_version = platform.version()
os_architecture = platform.architecture()[0]

# Display the information
print("Operating System Name :", os_name)
print("Operating System Version :", os_version)
print("System Architecture :", os_architecture)
