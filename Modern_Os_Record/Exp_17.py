class Process:
    def __init__(self, name, max_resources):
        self.name = name
        self.max_resources = max_resources  # Total resources required
        self.allocated = 0  # Resources currently allocated

class DeadlockPrevention:
    def __init__(self, total_resources):
        self.total_resources = total_resources
        self.available = total_resources
        self.processes = []

    def add_process(self, process):
        self.processes.append(process)

    def request_resources(self, process_name, request):
        process = next((p for p in self.processes if p.name == process_name), None)
        if not process:
            print(f"Process {process_name} not found.")
            return False

        print(f"\nProcess {process.name} requests {request} resources.")

        # Deadlock prevention: Hold and Wait Prevention
        if process.allocated > 0 and request > 0:
            print("Hold and Wait prevention: Cannot allocate while holding resources.")
            return False

        # Check if request is within max requirement
        if request + process.allocated > process.max_resources:
            print("Request exceeds process's maximum resources. Denied.")
            return False

        # Check availability
        if request <= self.available:
            self.available -= request
            process.allocated += request
            print(f"Resources allocated to {process.name}. Available: {self.available}")
            return True
        else:
            print("Not enough resources available. Request denied.")
            return False

    def release_resources(self, process_name):
        process = next((p for p in self.processes if p.name == process_name), None)
        if process and process.allocated > 0:
            print(f"\nProcess {process.name} releases {process.allocated} resources.")
            self.available += process.allocated
            process.allocated = 0
            print(f"Available resources: {self.available}")
        else:
            print(f"No resources to release for {process_name}.")


# Simulation
total_resources = int(input("Enter total system resources: "))
dp = DeadlockPrevention(total_resources)

# Add processes
num_processes = int(input("Enter number of processes: "))
for i in range(num_processes):
    name = input(f"Enter name for Process {i+1}: ")
    max_res = int(input(f"Enter maximum resources needed for {name}: "))
    dp.add_process(Process(name, max_res))

# Simulate resource requests
while True:
    action = input("\nEnter action (request/release/exit): ").lower()
    if action == 'request':
        pname = input("Enter process name: ")
        req = int(input("Enter resources to request: "))
        dp.request_resources(pname, req)
    elif action == 'release':
        pname = input("Enter process name: ")
        dp.release_resources(pname)
    elif action == 'exit':
        break
    else:
        print("Invalid action. Choose request/release/exit.")
