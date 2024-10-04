import random


class Process:
    def __init__(self, pid, priority):
        self.pid = pid
        self.state = 'ready'
        self.priority = priority

    def __repr__(self):
        return f"PID: {self.pid}, State: {self.state}, Priority: {self.priority}"


class ProcessManager:
    def __init__(self):
        self.process_list = []
        self.next_pid = 1

    def create_process(self, priority=None):
        if priority is None:
            priority = random.randint(1, 10)  # Assign a random priority if not given
        new_process = Process(self.next_pid, priority)
        self.process_list.append(new_process)
        print(f"Process {self.next_pid} created with priority {priority}.")
        self.next_pid += 1

    def display_processes(self):
        for process in self.process_list:
            print(process)


# Simulate process creation
manager = ProcessManager()
manager.create_process()
manager.create_process(5)
manager.create_process()
manager.display_processes()
def terminate_process(self, pid):
    for process in self.process_list:
        if process.pid == pid:
            process.state = 'terminated'
            print(f"Process {pid} terminated.")
            self.process_list.remove(process)
            return
    print(f"Process {pid} not found.")

print('\n','-'*50)
# Add the method to ProcessManager and simulate process termination
ProcessManager.terminate_process = terminate_process

# Terminating a process
manager.terminate_process(2)
manager.display_processes()
def context_switch(self, scheduling_algorithm='priority'):
    if not self.process_list:
        print("No processes to switch.")
        return

    # Simulate switching based on priority scheduling
    if scheduling_algorithm == 'priority':
        # Find the process with the highest priority
        self.process_list.sort(key=lambda p: p.priority, reverse=True)
        current_process = self.process_list[0]
        current_process.state = 'running'
        print(f"Process {current_process.pid} is now running.")

    # You can extend this with other algorithms like Round Robin or FIFO
print('\n','-'*50)
# Add the method to ProcessManager
ProcessManager.context_switch = context_switch

# Perform context switching
manager.context_switch()
manager.display_processes()
def system_call(self, operation, *args):
    if operation == 'create':
        self.create_process(*args)
    elif operation == 'terminate':
        self.terminate_process(*args)
    elif operation == 'switch':
        self.context_switch(*args)
    else:
        print("Invalid operation")
print('\n','-'*50)
# Add system call to ProcessManager
ProcessManager.system_call = system_call

# Simulate system calls
manager.system_call('create', 7)  # Create process with priority 7
manager.system_call('switch')  # Perform context switch
manager.system_call('terminate', 1)  # Terminate process with PID 1
manager.display_processes()
