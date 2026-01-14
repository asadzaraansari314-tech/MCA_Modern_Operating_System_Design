def predictive_lru(pages, capacity):
    frames = []
    page_faults = 0

    # Store frequency of page usage (prediction model)
    frequency = {}

    print("\nPredictive LRU Page Replacement\n")

    for page in pages:
        # Update frequency
        frequency[page] = frequency.get(page, 0) + 1

        if page in frames:
            # Page hit → move to most recent position
            frames.remove(page)
            frames.append(page)
        else:
            page_faults += 1
            if len(frames) < capacity:
                frames.append(page)
            else:
                # Predict which page is least likely to be used
                # Choose page with lowest frequency
                least_used = min(frames, key=lambda x: frequency.get(x, 0))
                frames.remove(least_used)
                frames.append(page)

        print(f"Page: {page} -> Frames: {frames}")

    print("\nTotal Page Faults (Predictive LRU):", page_faults)


# Input
pages = list(map(int, input("Enter page reference string: ").split()))
capacity = int(input("Enter number of frames: "))

predictive_lru(pages, capacity)
