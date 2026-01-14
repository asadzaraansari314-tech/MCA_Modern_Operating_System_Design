def optimal_page_replacement(pages, capacity):
    frames = []
    page_faults = 0

    print("\nOptimal Page Replacement\n")

    for i in range(len(pages)):
        page = pages[i]

        # Page hit
        if page in frames:
            print(f"Page: {page} -> Frames: {frames}")
            continue

        # Page fault
        page_faults += 1

        # If space available
        if len(frames) < capacity:
            frames.append(page)
        else:
            future = pages[i+1:]
            farthest_index = -1
            page_to_remove = None

            for f in frames:
                if f not in future:
                    page_to_remove = f
                    break
                else:
                    idx = future.index(f)
                    if idx > farthest_index:
                        farthest_index = idx
                        page_to_remove = f

            frames.remove(page_to_remove)
            frames.append(page)

        print(f"Page: {page} -> Frames: {frames}")

    print("\nTotal Page Faults (Optimal):", page_faults)


# Input
pages = list(map(int, input("Enter page reference string: ").split()))
capacity = int(input("Enter number of frames: "))

optimal_page_replacement(pages, capacity)
