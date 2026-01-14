# FCFS CPU Scheduling Program

n = int(input("Enter number of processes: "))

processes = []
burst_time = []

for i in range(n):
    bt = int(input(f"Enter Burst Time for Process P{i+1}: "))
    processes.append(f"P{i+1}")
    burst_time.append(bt)

waiting_time = [0] * n
turnaround_time = [0] * n

# Calculate Waiting Time
for i in range(1, n):
    waiting_time[i] = waiting_time[i-1] + burst_time[i-1]

# Calculate Turnaround Time
for i in range(n):
    turnaround_time[i] = waiting_time[i] + burst_time[i]

# Display results
print("\nProcess\tBurst Time\tWaiting Time\tTurnaround Time")
for i in range(n):
    print(f"{processes[i]}\t\t{burst_time[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

avg_waiting_time = sum(waiting_time) / n
avg_turnaround_time = sum(turnaround_time) / n

print("\nAverage Waiting Time =", avg_waiting_time)
print("Average Turnaround Time =", avg_turnaround_time)
