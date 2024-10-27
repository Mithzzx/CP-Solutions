class FileSystemSimulator:
    def __init__(self):
        # Initialize file system as an empty dictionary
        self.file_system = {}

    def create_file(self, filename):
        if filename in self.file_system:
            return f"Error: File '{filename}' already exists."
        else:
            self.file_system[filename] = ""
            return f"File '{filename}' created successfully."

    def delete_file(self, filename):
        if filename in self.file_system:
            del self.file_system[filename]
            return f"File '{filename}' deleted successfully."
        else:
            return f"Error: File '{filename}' does not exist."

    def read_file(self, filename):
        if filename in self.file_system:
            return f"Content of '{filename}': {self.file_system[filename]}"
        else:
            return f"Error: File '{filename}' does not exist."

    def write_file(self, filename, content):
        if filename in self.file_system:
            self.file_system[filename] += content
            return f"Content written to '{filename}' successfully."
        else:
            return f"Error: File '{filename}' does not exist."

    def show_file_system(self):
        if self.file_system:
            return f"File System State: {self.file_system}"
        else:
            return "File System is empty."


# Command-line interface to interact with the file system
def command_line_interface():
    fs = FileSystemSimulator()

    while True:
        command = input("Enter a command (create, delete, read, write, show, exit): ").strip().split()

        if not command:
            print("Invalid command. Please try again.")
            continue

        action = command[0].lower()

        if action == "create" and len(command) == 2:
            print(fs.create_file(command[1]))

        elif action == "delete" and len(command) == 2:
            print(fs.delete_file(command[1]))

        elif action == "read" and len(command) == 2:
            print(fs.read_file(command[1]))

        elif action == "write" and len(command) >= 3:
            filename = command[1]
            content = " ".join(command[2:])
            print(fs.write_file(filename, content))

        elif action == "show":
            print(fs.show_file_system())

        elif action == "exit":
            print("Exiting the file system simulator.")
            break

        else:
            print("Invalid command or syntax. Please try again.")

# Uncomment the line below to run the simulator
# command_line_interface()
