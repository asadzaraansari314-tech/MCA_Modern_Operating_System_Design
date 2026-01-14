# CPU Scheduling Algorithms in Python

def fcfs_scheduling(processes, burst_time):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    # Calculate waiting time
    for i in range(1, n):
        waiting_time[i] = waiting_time[i-1] + burst_time[i-1]

    # Calculate turnaround time
    for i in range(n):
        turnaround_time[i] = burst_time[i] + waiting_time[i]

    print("FCFS Scheduling:")
    print_schedule(processes, burst_time, waiting_time, turnaround_time)


def sjf_scheduling(processes, burst_time):
    n = len(processes)
    processes_bt = list(zip(processes, burst_time))
    # Sort processes by burst time (SJF)
    processes_bt.sort(key=lambda x: x[1])
    sorted_processes = [p[0] for p in processes_bt]
    sorted_burst_time = [p[1] for p in processes_bt]

    waiting_time = [0] * n
    turnaround_time = [0] * n

    # Calculate waiting time
    for i in range(1, n):
        waiting_time[i] = waiting_time[i-1] + sorted_burst_time[i-1]

    # Calculate turnaround time
    for i in range(n):
        turnaround_time[i] = sorted_burst_time[i] + waiting_time[i]

    print("SJF Scheduling:")
    print_schedule(sorted_processes, sorted_burst_time, waiting_time, turnaround_time)


def priority_scheduling(processes, burst_time, priority):
    n = len(processes)
    processes_bt_pr = list(zip(processes, burst_time, priority))
    # Sort processes by priority (lower number = higher priority)
    processes_bt_pr.sort(key=lambda x: x[2])
    sorted_processes = [p[0] for p in processes_bt_pr]
    sorted_burst_time = [p[1] for p in processes_bt_pr]

    waiting_time = [0] * n
    turnaround_time = [0] * n

    # Calculate waiting time
    for i in range(1, n):
        waiting_time[i] = waiting_time[i-1] + sorted_burst_time[i-1]

    # Calculate turnaround time
    for i in range(n):
        turnaround_time[i] = sorted_burst_time[i] + waiting_time[i]

    print("Priority Scheduling:")
    print_schedule(sorted_processes, sorted_burst_time, waiting_time, turnaround_time)


def print_schedule(processes, burst_time, waiting_time, turnaround_time):
    print("Process\tBurst Time\tWaiting Time\tTurnaround Time")
    total_wt = 0
    total_tat = 0
    for i in range(len(processes)):
        total_wt += waiting_time[i]
        total_tat += turnaround_time[i]
        print(f"{processes[i]}\t{burst_time[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")
    print(f"Average Waiting Time: {total_wt / len(processes):.2f}")
    print(f"Average Turnaround Time: {total_tat / len(processes):.2f}\n")


# Example usage
processes = ["P1", "P2", "P3", "P4"]
burst_time = [6, 8, 7, 3]
priority = [2, 1, 4, 3]  # Lower number means higher priority

fcfs_scheduling(processes, burst_time)
sjf_scheduling(processes, burst_time)
priority_scheduling(processes, burst_time, priority)
