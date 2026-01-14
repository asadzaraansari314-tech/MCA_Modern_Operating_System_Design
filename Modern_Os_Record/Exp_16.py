def is_safe_state(processes, avail, max_demand, allocation):
    n = len(processes)
    m = len(avail)

    # Calculate remaining need matrix
    need = [[max_demand[i][j] - allocation[i][j] for j in range(m)] for i in range(n)]

    finish = [False] * n
    safe_seq = []

    work = avail.copy()

    while len(safe_seq) < n:
        allocated = False
        for i in range(n):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(m)):
                # Can allocate to process i
                for j in range(m):
                    work[j] += allocation[i][j]
                safe_seq.append(processes[i])
                finish[i] = True
                allocated = True
                break
        if not allocated:
            break

    if len(safe_seq) == n:
        print("System is in a SAFE state.")
        print("Safe sequence:", ' -> '.join(safe_seq))
        return True
    else:
        print("System is NOT in a safe state. Deadlock may occur.")
        return False


# Input
processes = input("Enter process names separated by space: ").split()
n = len(processes)
m = int(input("Enter number of resource types: "))

print("\nEnter Allocation Matrix:")
allocation = []
for i in range(n):
    row = list(map(int, input(f"Allocation for {processes[i]}: ").split()))
    allocation.append(row)

print("\nEnter Maximum Demand Matrix:")
max_demand = []
for i in range(n):
    row = list(map(int, input(f"Max demand for {processes[i]}: ").split()))
    max_demand.append(row)

avail = list(map(int, input("\nEnter Available resources: ").split()))

# Run Banker's Algorithm
is_safe_state(processes, avail, max_demand, allocation)
