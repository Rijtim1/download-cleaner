import os

class FileOrganizer:
    def __init__(self):
        self.default_path = "C:\\Users\\Username\\Downloads"
        self.path = None
    
    def get_path(self):
        """Prompt the user for the path to the folder to be organized,
        or read the path from a file if it exists.
        """
        # Check if path.txt exists
        if os.path.exists("path.txt"):
            # Read path from file
            try:
                with open("path.txt", "r") as f:
                    self.path = f.read()
            except FileNotFoundError:
                print("Error: path.txt not found.")
                self.path = None
        else:
            # Prompt user for path
            self.path = input("Enter the path to the folder you want to organize: ")
            # Check if user wants to save the path
            save = input("Do you want to save this path? (y/n): ")
            if save == "y":
                # Write path to file
                try:
                    with open("path.txt", "w") as f:
                        f.write(self.path)
                except FileNotFoundError:
                    print("Error: unable to save path to path.txt.")
    
    def change_path(self):
        """Prompt the user for the path to the folder to be organized,
        and give them the option to save it to the path.txt file.
        """
        self.path = input("Enter the path to the folder you want to organize: ")
        save = input("Do you want to save this path? (y/n): ")
        if save == "y":
            try:
                with open("path.txt", "w") as f:
                    f.write(self.path)
            except FileNotFoundError:
                print("Error: unable to save path to path.txt.")
