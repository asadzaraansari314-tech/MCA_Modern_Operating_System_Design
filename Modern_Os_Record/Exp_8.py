# Priority Scheduling (Non-Preemptive)

n = int(input("Enter number of processes: "))

processes = []
burst_time = []
priority = []

for i in range(n):
    bt = int(input(f"Enter Burst Time for Process P{i+1}: "))
    pr = int(input(f"Enter Priority for Process P{i+1} (lower number = higher priority): "))
    processes.append(f"P{i+1}")
    burst_time.append(bt)
    priority.append(pr)

# Combine and sort by priority
data = list(zip(processes, burst_time, priority))
data.sort(key=lambda x: x[2])  # sort by priority

waiting_time = [0] * n
turnaround_time = [0] * n

# Calculate Waiting Time
for i in range(1, n):
    waiting_time[i] = waiting_time[i-1] + data[i-1][1]

# Calculate Turnaround Time
for i in range(n):
    turnaround_time[i] = waiting_time[i] + data[i][1]

# Display results
print("\nProcess\tPriority\tBurst Time\tWaiting Time\tTurnaround Time")
for i in range(n):
    print(f"{data[i][0]}\t\t{data[i][2]}\t\t{data[i][1]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

print("\nAverage Waiting Time =", sum(waiting_time) / n)
print("Average Turnaround Time =", sum(turnaround_time) / n)
