import time
from collections import defaultdict, deque

class FileAccessMonitor:
    def __init__(self):
        self.access_count = defaultdict(int)  # Frequency of access
        self.recent_access = deque(maxlen=10)  # Last 10 accesses

    def access_file(self, filename):
        self.access_count[filename] += 1
        self.recent_access.append(filename)
        print(f"File accessed: {filename}")
        self.suggest_cache_strategy(filename)

    def suggest_cache_strategy(self, filename):
        freq = self.access_count[filename]
        recency_rank = list(self.recent_access).count(filename)

        # Decision heuristic
        if freq > 3 and recency_rank > 1:
            strategy = "LRU or LFU cache recommended (frequent and recent)"
        elif freq > 3:
            strategy = "LFU cache recommended (frequent access)"
        elif recency_rank > 1:
            strategy = "LRU cache recommended (recently used)"
        else:
            strategy = "No caching required yet"

        print(f"Suggested caching strategy for '{filename}': {strategy}\n")


# Simulation
monitor = FileAccessMonitor()

# Simulate file accesses
files = ["file1.txt", "file2.txt", "file3.txt", "file1.txt", "file2.txt",
         "file1.txt", "file4.txt", "file1.txt", "file3.txt"]

for f in files:
    monitor.access_file(f)
    time.sleep(0.5)
