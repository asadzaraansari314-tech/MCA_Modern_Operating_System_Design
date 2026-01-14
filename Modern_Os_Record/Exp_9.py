# Page Replacement Algorithms: FIFO and LRU

def fifo(pages, capacity):
    frame = []
    faults = 0

    print("\nFIFO Page Replacement")
    for page in pages:
        if page not in frame:
            faults += 1
            if len(frame) < capacity:
                frame.append(page)
            else:
                frame.pop(0)
                frame.append(page)
        print(f"Page: {page} -> Frames: {frame}")
    print("Total Page Faults (FIFO):", faults)


def lru(pages, capacity):
    frame = []
    faults = 0

    print("\nLRU Page Replacement")
    for page in pages:
        if page not in frame:
            faults += 1
            if len(frame) < capacity:
                frame.append(page)
            else:
                frame.pop(0)
                frame.append(page)
        else:
            frame.remove(page)
            frame.append(page)
        print(f"Page: {page} -> Frames: {frame}")
    print("Total Page Faults (LRU):", faults)


# Input
pages = list(map(int, input("Enter page reference string: ").split()))
capacity = int(input("Enter number of frames: "))

# Run algorithms
fifo(pages, capacity)
lru(pages, capacity)
