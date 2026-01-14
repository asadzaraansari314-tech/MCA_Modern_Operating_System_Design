import time
from collections import deque

class Container:
    def __init__(self, name, cpu_limit, mem_limit):
        self.name = name
        self.cpu_limit = cpu_limit  # max CPU units
        self.mem_limit = mem_limit  # max Memory units
        self.cpu_used = 0
        self.mem_used = 0
        self.task_queue = deque()

    def submit_task(self, task):
        # Check if resources available
        if task['cpu'] > self.cpu_limit or task['mem'] > self.mem_limit:
            print(f"Task {task['name']} exceeds container {self.name} resource limits. Rejected.")
            return False
        self.task_queue.append(task)
        print(f"Task {task['name']} submitted to container {self.name}")
        return True

    def schedule_tasks(self):
        print(f"\nScheduling tasks in container {self.name}...\n")
        while self.task_queue:
            task = self.task_queue.popleft()
            # Check if resources available for this task
            if task['cpu'] + self.cpu_used <= self.cpu_limit and task['mem'] + self.mem_used <= self.mem_limit:
                print(f"Running Task {task['name']} | CPU: {task['cpu']} | MEM: {task['mem']}")
                self.cpu_used += task['cpu']
                self.mem_used += task['mem']
                time.sleep(0.5)  # Simulate task running
                print(f"Completed Task {task['name']}")
                self.cpu_used -= task['cpu']
                self.mem_used -= task['mem']
            else:
                print(f"Task {task['name']} waiting due to insufficient resources.")
                self.task_queue.append(task)  # Retry later
                time.sleep(0.5)

# Simulation
containers = [
    Container("Container1", cpu_limit=4, mem_limit=8),
    Container("Container2", cpu_limit=2, mem_limit=4)
]

tasks = [
    {'name': 'Task1', 'cpu': 2, 'mem': 3},
    {'name': 'Task2', 'cpu': 1, 'mem': 2},
    {'name': 'Task3', 'cpu': 3, 'mem': 5},
    {'name': 'Task4', 'cpu': 2, 'mem': 1},
]

# Assign tasks to containers based on resource availability
for task in tasks:
    assigned = False
    for container in containers:
        if container.submit_task(task):
            assigned = True
            break
    if not assigned:
        print(f"Task {task['name']} could not be assigned to any container.\n")

# Schedule tasks in all containers
for container in containers:
    container.schedule_tasks()
