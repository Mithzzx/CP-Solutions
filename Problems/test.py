import os

def list_directory(path='.'):
    try:
        # List all files and directories in the current directory (or provided path)
        for item in os.listdir(path):
            print(item)
    except FileNotFoundError:
        print(f"Error: The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied for directory '{path}'.")

if __name__ == "__main__":
    directory = input("Enter the directory path (or leave blank for current directory): ") or '.'
    list_directory(directory)

