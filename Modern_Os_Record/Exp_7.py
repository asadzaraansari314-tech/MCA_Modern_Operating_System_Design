# Round Robin CPU Scheduling Program

n = int(input("Enter number of processes: "))

processes = []
burst_time = []
remaining_time = []

for i in range(n):
    bt = int(input(f"Enter Burst Time for Process P{i+1}: "))
    processes.append(f"P{i+1}")
    burst_time.append(bt)
    remaining_time.append(bt)

time_quantum = int(input("Enter Time Quantum: "))

waiting_time = [0] * n
turnaround_time = [0] * n

time = 0

# Round Robin Scheduling Logic
while True:
    done = True
    for i in range(n):
        if remaining_time[i] > 0:
            done = False
            if remaining_time[i] > time_quantum:
                time += time_quantum
                remaining_time[i] -= time_quantum
            else:
                time += remaining_time[i]
                waiting_time[i] = time - burst_time[i]
                remaining_time[i] = 0
    if done:
        break

# Calculate Turnaround Time
for i in range(n):
    turnaround_time[i] = burst_time[i] + waiting_time[i]

# Display Results
print("\nProcess\tBurst Time\tWaiting Time\tTurnaround Time")
for i in range(n):
    print(f"{processes[i]}\t\t{burst_time[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

print("\nAverage Waiting Time =", sum(waiting_time) / n)
print("Average Turnaround Time =", sum(turnaround_time) / n)
