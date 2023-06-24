# File Organization Script Documentation

The file organization script is a Python script that helps you organize files in a specified folder based on their file extensions. It categorizes files into different directories based on their extensions and moves them accordingly.

## Prerequisites

To run the script, you need the following:

- Python 3.x installed on your system
- The `os` and `shutil` modules, which are part of the Python Standard Library

## Usage

1. Save the script code in a Python file (e.g., `file_organization.py`).
1. Open a terminal or command prompt.
1. Navigate to the directory where the script file is located.
1. Run the script using the following command: python file_organization.py.

## Script Explanation

The script consists of the following components:

1. File Categories: The `file_categories` dictionary defines different categories of files based on their extensions. Each category is associated with a list of file extensions. You can modify this dictionary according to your preferences.

1. `Clean Class`: The Clean class encapsulates the file organization process.

    - `__init__(self, path)`: Initializes the `Clean` object with the specified `path` parameter, representing the folder path to organize.

    - `list_files(self)`: Retrieves all the `files` in the specified folder and stores them in the files attribute.

    - `get_file_extension(self)`: Extracts the unique file extensions from the `files` list and stores them in the extensions attribute.

    - `setup(self)`: Creates the necessary directories for each file category and extension.

    - `move_files(self)`: Moves the files to their respective directories based on their extensions and categories. Duplicate files are handled by appending a count number to the file name.

1. `get_downloads_path()`: Returns the path to the user's downloads folder. This function is used to get the default folder to organize.

1. `organize_folder(path)`: Performs the file organization process for the specified `path` folder. It creates an instance of the `Clean` class and calls the necessary methods to organize the files.

1. `main()`: The main function of the script. It retrieves the downloads folder path and calls the `organize_folder` function to organize the files in the downloads folder.

1. Execution: The script checks if the downloads folder exists and executes the `main` function if it does.

## Customization

To customize the file categories or add new ones, you can modify the `file_categories` dictionary in the script. You can define your own categories and associate them with specific file extensions.

For example, if you want to add a new category called "Scripts" for JavaScript files, you can modify the `file_categories` dictionary as follows:

``
file_categories = {
    # ...
    'Scripts': ['.py', '.sh', '.js', '.php', '.pl'],
    # ...
}
``

Make sure to include the leading dot (e.g., .js) for each file extension.

## Limitations

- The script organizes files only within a single folder. It does not traverse subdirectories.

- The script moves files based on their extensions and categories. If you have files without recognized extensions or categories, they will be moved to the "Misc" directory.

## Example Output

Here's an example output of the script:

``
Organizing folder at C:\Users\Username\Downloads
Setting up directories: 100%|███████████████████████████████████████████████████| 15/15 [00:00<00:00, 1923.08it/s]
Moving files: 100%|████████████████████████████████████████████████████████████████| 20/20 [00:00<00:00, 1111.11it/s]
Total time taken: 0.04 seconds
Total files moved: 20
``

The output shows the progress of setting up directories and moving files, along with the total time taken and the number of files moved.

## Summary

The file organization script is a handy tool to automatically organize files in a folder based on their extensions. It provides a convenient way to keep your files organized and easily accessible. By using predefined categories, the script ensures that files are placed in appropriate directories.
