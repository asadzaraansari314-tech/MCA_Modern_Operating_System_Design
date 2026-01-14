# Banker's Algorithm in Python

def is_safe_state(processes, avail, max_demand, allocation):
    n = len(processes)  # Number of processes
    m = len(avail)      # Number of resources

    # Calculate the Need matrix
    need = [[max_demand[i][j] - allocation[i][j] for j in range(m)] for i in range(n)]

    # Initialize work and finish
    work = avail.copy()
    finish = [False] * n
    safe_sequence = []

    while len(safe_sequence) < n:
        allocated_in_this_round = False
        for i in range(n):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(m)):
                # Process can be executed
                for j in range(m):
                    work[j] += allocation[i][j]  # Release resources
                finish[i] = True
                safe_sequence.append(processes[i])
                allocated_in_this_round = True

        if not allocated_in_this_round:
            # No process could be allocated safely => unsafe state
            return False, []

    return True, safe_sequence

# Example Input
processes = ["P0", "P1", "P2", "P3", "P4"]
avail = [3, 3, 2]  # Available instances of resources
max_demand = [
    [7, 5, 3],
    [3, 2, 2],
    [9, 0, 2],
    [2, 2, 2],
    [4, 3, 3]
]
allocation = [
    [0, 1, 0],
    [2, 0, 0],
    [3, 0, 2],
    [2, 1, 1],
    [0, 0, 2]
]

# Run Banker's Algorithm
safe, sequence = is_safe_state(processes, avail, max_demand, allocation)

if safe:
    print("System is in a SAFE state.")
    print("Safe sequence is:", " -> ".join(sequence))
else:
    print("System is in an UNSAFE state. No safe sequence exists.")
