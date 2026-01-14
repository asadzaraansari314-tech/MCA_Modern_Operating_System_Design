# Disk Scheduling Algorithms: FCFS and SSTF

def fcfs(requests, head):
    total_seek = 0
    current = head

    print("\nFCFS Disk Scheduling")
    print("Seek Sequence:", current, end=" ")

    for req in requests:
        total_seek += abs(req - current)
        current = req
        print("->", current, end=" ")

    print("\nTotal Seek Time (FCFS):", total_seek)


def sstf(requests, head):
    total_seek = 0
    current = head
    pending = requests.copy()

    print("\nSSTF Disk Scheduling")
    print("Seek Sequence:", current, end=" ")

    while pending:
        nearest = min(pending, key=lambda x: abs(x - current))
        total_seek += abs(nearest - current)
        current = nearest
        pending.remove(nearest)
        print("->", current, end=" ")

    print("\nTotal Seek Time (SSTF):", total_seek)


# Input
requests = list(map(int, input("Enter disk request queue: ").split()))
head = int(input("Enter initial head position: "))

# Run algorithms
fcfs(requests, head)
sstf(requests, head)
