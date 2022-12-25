from config import *
import os
import shutil
import time
import user_path_util
import multiprocessing
import tqdm
import argparse

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
        
    def setup(self, args):
        # Display a progress bar for the setup process
        with tqdm.tqdm(total=len(self.extentions), desc="Setting up directories") as pbar:
            for ext in self.extentions:
                for key, value in file_categories.items():
                    if ext in value:
                        category_dir = f"{self.path}\\{key}"
                        if not os.path.exists(category_dir):
                            # Check if dry run mode is enabled
                            if not args.dry_run:
                                os.mkdir(category_dir)
                        extension_dir = f"{category_dir}\\{ext}"
                        if not os.path.exists(extension_dir):
                            # Check if dry run mode is enabled
                            if not args.dry_run:
                                os.mkdir(extension_dir)
                # Update the progress bar
                pbar.update(1)

    
    def move_files(self, files_and_args):
        files, args = files_and_args
        # Create a mapping of file extensions to file categories
        extension_map = {}
        for category, extensions in file_categories.items():
            for extension in extensions:
                extension_map[extension] = category
        # Display a progress bar for the file movement process
        with tqdm.tqdm(total=len(files), desc="Moving files") as pbar:
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
                    # Check if dry run mode is enabled
                    if not args.dry_run:
                        # Move the file to the destination
                        try:
                            shutil.move(os.path.join(self.path, file), destination)
                        except shutil.Error:
                            os.remove(os.path.join(self.path, file))
                # Update the progress bar
                pbar.update(1)

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dry-run', action='store_true', help='show what changes would be made without actually moving the files')
    return parser.parse_args()

def get_path():
    # Use saved path or prompt user for path
    return user_path_util.get_path()

def organize_folder(path, args):
    # Organize the folder at the specified path
    print(f"Organizing folder at {path}")
    clean = Clean(path)
    clean.list_files()
    clean.get_file_extension()
    clean.setup(args)
    # Split the list of files into chunks
    chunk_size = len(clean.files) // multiprocessing.cpu_count()
    if chunk_size == 0:
        file_chunks = [clean.files]
    else:
        file_chunks = [clean.files[i:i + chunk_size] for i in range(0, len(clean.files), chunk_size)]
    # Create a pool of worker processes
    with multiprocessing.Pool() as pool:
        # Use the map() method to apply the move_files() method to each chunk of files in parallel
        pool.map(clean.move_files, [(chunk, args) for chunk in file_chunks])

    # Display the total time taken to organize the folder and the number of files moved
    print(f"Total time taken: {time.time() - clean.start:.2f} seconds")
    print(f"Total files moved: {len(clean.files)}")

def main():
    args = parse_arguments()
    path = get_path()
    if os.path.exists(path):
        organize_folder(path, args)
    else:
        print(f"Invalid path: {path}")


if __name__ == "__main__":
    main()