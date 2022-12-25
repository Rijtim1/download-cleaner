import os

# Default path to the folder to be organized
DEFAULT_PATH = "C:\\Users\\Username\\Downloads"

def get_path():
    """Prompt the user for the path to the folder to be organized,
    or read the path from a file if it exists.
    """
    # Check if path.txt exists
    if os.path.exists("path.txt"):
        # Read path from file
        try:
            with open("path.txt", "r") as f:
                path = f.read()
        except FileNotFoundError:
            print("Error: path.txt not found.")
            path = None
    else:
        # Prompt user for path
        path = input("Enter the path to the folder you want to organize: ")
        # Check if user wants to save the path
        save = input("Do you want to save this path? (y/n): ")
        if save == "y":
            # Write path to file
            try:
                with open("path.txt", "w") as f:
                    f.write(path)
            except FileNotFoundError:
                print("Error: unable to save path to path.txt.")
    return path

def change_path_():
    """Prompt the user for the path to the folder to be organized,
    and give them the option to save it to the path.txt file.
    """
    path = input("Enter the path to the folder you want to organize: ")
    save = input("Do you want to save this path? (y/n): ")
    if save == "y":
        try:
            with open("path.txt", "w") as f:
                f.write(path)
        except FileNotFoundError:
            print("Error: unable to save path to path.txt.")
    return path

# def main():
#     # Ask user if they want to change the path
#     change_path = input("Do you want to change the path? (y/n): ")
#     if change_path == "y":
#         path = change_path_()
#     else:
#         path = get_path()
#     # Check if the path is valid
#     if os.path.exists(path):
#         # Organize the folder at the specified path
#         # organize_folder(path)
#         print(f"Organizing folder at {path}")
#     else:
#         print(f"Error: path {path} does not exist.")

# if __name__ == "__main__":
#     main()
