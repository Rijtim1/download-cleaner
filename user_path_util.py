import os

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
    # Use default path if no path was provided or found
    if path is None:
        path = None
    return path
