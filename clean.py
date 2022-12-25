from config import *
import os
import shutil
import time
import user_path_util
import multiprocessing

class Clean:
    def __init__(self, path):
        self.path = path
        self.start = time.time()
                            
    def list_files(self):
        items = os.listdir(self.path)
        self.files = [item for item in items if os.path.isfile(f"{self.path}\\{item}")]
        
    def get_file_extension(self):
        self.extentions = []
        for files in self.files:
            self.extentions.append(os.path.splitext(files)[1])
        
    def setup(self):
        for ext in self.extentions:
            for key, value in file_categories.items():
                if ext in value:
                    category_dir = f"{self.path}\\{key}"
                    if not os.path.exists(category_dir):
                        os.mkdir(category_dir)
                    extension_dir = f"{category_dir}\\{ext}"
                    if not os.path.exists(extension_dir):
                        os.mkdir(extension_dir)
    
    def move_files(self, files):
        # Create a mapping of file extensions to file categories
        extension_map = {}
        for category, extensions in file_categories.items():
            for extension in extensions:
                extension_map[extension] = category
        # Move the files to the correct folders
        for file in files:
            # Get the file extension
            extension = os.path.splitext(file)[1]
            # Check if the file extension is in the extension map
            if extension in extension_map:
                # Get the file category for the extension
                category = extension_map[extension]
                # Build the destination path for the file
                destination = os.path.join(self.path, category, extension)
                # Move the file to the destination
                try:
                    shutil.move(os.path.join(self.path, file), destination)
                except shutil.Error:
                    os.remove(os.path.join(self.path, file))


def main():
    # Use saved path or prompt user for path
    path = user_path_util.get_path()
    # Check if the path is valid
    if os.path.exists(path):
        # Organize the folder at the specified path
        print(f"Organizing folder at {path}")
        clean = Clean(path)
        clean.list_files()
        clean.get_file_extension()
        clean.setup()
        # Split the list of files into chunks
        chunk_size = len(clean.files) // multiprocessing.cpu_count()
        if chunk_size == 0:
            file_chunks = [clean.files]
        else:
            file_chunks = [clean.files[i:i + chunk_size] for i in range(0, len(clean.files), chunk_size)]
        # Create a pool of worker processes
        with multiprocessing.Pool() as pool:
            # Use the map() method to apply the move_files() method to each chunk of files in parallel
            pool.map(clean.move_files, file_chunks)
    else:
        print(f"Error: path {path} does not exist.")

if __name__ == "__main__":
    main()
