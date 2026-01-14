import time
from collections import deque

class Task:
    def __init__(self, name, burst_time, priority=0):
        self.name = name
        self.burst_time = burst_time
        self.priority = priority

class ContainerScheduler:
    def __init__(self, scheduling='FCFS'):
        self.queue = deque()
        self.scheduling = scheduling

    def submit_task(self, task):
        print(f"Task submitted: {task.name} | Burst Time: {task.burst_time} | Priority: {task.priority}")
        self.queue.append(task)

    def schedule(self):
        print(f"\nContainer scheduling tasks using {self.scheduling}...\n")
        if self.scheduling == 'Priority':
            # Sort queue by priority (lower number = higher priority)
            self.queue = deque(sorted(self.queue, key=lambda x: x.priority))

        current_time = 0
        for task in self.queue:
            print(f"Running Task: {task.name} | Burst Time: {task.burst_time} | Current Time: {current_time}")
            time.sleep(0.5)  # Simulate task running
            current_time += task.burst_time
            print(f"Completed Task: {task.name} | Time Finished: {current_time}\n")

        print("All tasks completed.\n")


# Simulation
container = ContainerScheduler(scheduling='Priority')

# Submit tasks to the container
tasks = [
    Task("Task1", 4, priority=2),
    Task("Task2", 2, priority=1),
    Task("Task3", 6, priority=3),
    Task("Task4", 3, priority=2)
]

for t in tasks:
    container.submit_task(t)

# Run container scheduler
container.schedule()
