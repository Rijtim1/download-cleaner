# Clean Class Documentation

## [![Workflow](https://github.com/Rijtim1/download-cleaner/actions/workflows/workflow.yml/badge.svg)](https://github.com/Rijtim1/download-cleaner/actions/workflows/workflow.yml)

The Clean class provides functionality to organize files in a specified directory based on their file extension. The class has the following methods:

### `__init__(self, path)`

- `path`: A string representing the directory path to be organized.
- Initializes the path attribute with the specified directory path and sets the start time of the organization process.

### `list_files(self)`

- Retrieves a list of all files in the directory specified by the `path` attribute.
- Populates the files attribute with a list of only the file names (not directories) from the retrieved list.

### `get_file_extension(self)`

- Iterates over each file in the `files` attribute and extracts its file extension.
- Populates the `extensions` attribute with a list of unique file extensions.

### `setup(self, args)`

- `args`: A list of command-line arguments to configure the file organization process.
- Creates a directory structure based on the file `extensions` present in the extensions attribute.
- Displays a progress bar during the directory creation process.
- Creates directories only if they do not already exist.
- If dry run mode is not enabled (a command-line argument), directories are created using the `os.mkdir()` function.

### `move_files(self, args)`

- `args`: A list of command-line arguments to configure the file organization process.
- Creates a mapping of file extensions to file categories.
- Displays a progress bar during the file movement process.
- Moves files to their corresponding directory based on their file extension and file category.
- Deletes files that already exist in their destination directory.
- If dry run mode is not enabled (a command-line argument), files are moved using the `shutil.move()` function.
