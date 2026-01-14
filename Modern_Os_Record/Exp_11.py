# Memory Allocation Strategies

def first_fit(blocks, processes):
    allocation = [-1] * len(processes)

    for i in range(len(processes)):
        for j in range(len(blocks)):
            if blocks[j] >= processes[i]:
                allocation[i] = j
                blocks[j] -= processes[i]
                break
    return allocation


def best_fit(blocks, processes):
    allocation = [-1] * len(processes)

    for i in range(len(processes)):
        best_index = -1
        for j in range(len(blocks)):
            if blocks[j] >= processes[i]:
                if best_index == -1 or blocks[j] < blocks[best_index]:
                    best_index = j

        if best_index != -1:
            allocation[i] = best_index
            blocks[best_index] -= processes[i]
    return allocation


def worst_fit(blocks, processes):
    allocation = [-1] * len(processes)

    for i in range(len(processes)):
        worst_index = -1
        for j in range(len(blocks)):
            if blocks[j] >= processes[i]:
                if worst_index == -1 or blocks[j] > blocks[worst_index]:
                    worst_index = j

        if worst_index != -1:
            allocation[i] = worst_index
            blocks[worst_index] -= processes[i]
    return allocation


# Input
blocks = list(map(int, input("Enter memory block sizes: ").split()))
processes = list(map(int, input("Enter process sizes: ").split()))

# Copy blocks for each method
ff_blocks = blocks.copy()
bf_blocks = blocks.copy()
wf_blocks = blocks.copy()

ff = first_fit(ff_blocks, processes)
bf = best_fit(bf_blocks, processes)
wf = worst_fit(wf_blocks, processes)

# Display results
print("\nProcess\tSize\tFirst Fit\tBest Fit\tWorst Fit")
for i in range(len(processes)):
    print(f"P{i+1}\t\t{processes[i]}\t\t"
          f"{ff[i] + 1 if ff[i] != -1 else 'Not Allocated'}\t\t"
          f"{bf[i] + 1 if bf[i] != -1 else 'Not Allocated'}\t\t"
          f"{wf[i] + 1 if wf[i] != -1 else 'Not Allocated'}")
