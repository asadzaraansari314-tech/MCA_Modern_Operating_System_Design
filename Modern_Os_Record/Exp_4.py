import psutil

print("Top 5 Running Processes:\n")

count = 0
for process in psutil.process_iter(['pid', 'name']):
    try:
        print("Process Name:", process.info['name'], "| PID:", process.info['pid'])
        count += 1
        if count == 5:
            break
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        pass
