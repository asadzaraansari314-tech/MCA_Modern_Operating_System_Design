# FIFO and LRU Page Replacement in Python

def fifo_page_replacement(pages, frame_size):
    frames = []
    page_faults = 0
    index = 0  # Points to the next frame to replace

    print("FIFO Page Replacement Steps:")
    for page in pages:
        if page not in frames:
            if len(frames) < frame_size:
                frames.append(page)
            else:
                frames[index] = page
                index = (index + 1) % frame_size
            page_faults += 1
            print(f"Page {page} caused a fault. Frames: {frames}")
        else:
            print(f"Page {page} hit. Frames: {frames}")
    print(f"Total Page Faults (FIFO): {page_faults}\n")

def lru_page_replacement(pages, frame_size):
    frames = []
    page_faults = 0
    recent_usage = []  # Keeps track of usage order for LRU

    print("LRU Page Replacement Steps:")
    for page in pages:
        if page not in frames:
            if len(frames) < frame_size:
                frames.append(page)
            else:
                # Find the least recently used page
                lru_page = recent_usage.pop(0)
                lru_index = frames.index(lru_page)
                frames[lru_index] = page
            page_faults += 1
            print(f"Page {page} caused a fault. Frames: {frames}")
        else:
            print(f"Page {page} hit. Frames: {frames}")

        # Update recent usage
        if page in recent_usage:
            recent_usage.remove(page)
        recent_usage.append(page)

    print(f"Total Page Faults (LRU): {page_faults}\n")

# Example usage
page_reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
frame_size = 3

fifo_page_replacement(page_reference_string, frame_size)
lru_page_replacement(page_reference_string, frame_size)
