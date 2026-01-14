# Disk Scheduling: FCFS and SSTF

def fcfs_disk_scheduling(requests, head):
    """
    FCFS (First-Come-First-Serve) Disk Scheduling
    """
    seek_sequence = [head]
    seek_count = 0

    print("FCFS Disk Scheduling Steps:")
    for req in requests:
        seek_count += abs(head - req)
        head = req
        seek_sequence.append(req)
        print(f"Move to {req}, Seek so far: {seek_count}")

    print(f"\nTotal Seek Operations (FCFS): {seek_count}")
    print(f"Seek Sequence (FCFS): {seek_sequence}\n")
    return seek_count, seek_sequence

def sstf_disk_scheduling(requests, head):
    """
    SSTF (Shortest Seek Time First) Disk Scheduling
    """
    requests = requests.copy()
    seek_sequence = [head]
    seek_count = 0

    print("SSTF Disk Scheduling Steps:")
    while requests:
        # Find the request closest to current head
        distances = [abs(head - req) for req in requests]
        min_distance = min(distances)
        index = distances.index(min_distance)
        nearest_request = requests.pop(index)

        seek_count += min_distance
        head = nearest_request
        seek_sequence.append(nearest_request)
        print(f"Move to {nearest_request}, Seek so far: {seek_count}")

    print(f"\nTotal Seek Operations (SSTF): {seek_count}")
    print(f"Seek Sequence (SSTF): {seek_sequence}\n")
    return seek_count, seek_sequence

# Example usage
disk_requests = [82, 170, 43, 140, 24, 16, 190]
initial_head = 50

fcfs_disk_scheduling(disk_requests, initial_head)
sstf_disk_scheduling(disk_requests, initial_head)
