from config import *
import os
import shutil
import time
import datetime


class Clean:

    def __init__(self):
        self.file_names = []
        self.keys = []
        self.start = time.time()
        self.debug = False

    def get_file_names(self):
        """This function gets the file names in the downloads folder."""
        self.root_dir = DOWNLOAD_PATH
        with os.scandir(self.root_dir) as entries:
            self.file_names = [entry.name for entry in entries if entry.is_file()]
        if self.debug:
            print(self.root_dir, self.file_names)


    def find_file_extension(self):
        """This function finds the file extensions and stores them in a dictionary."""
        extension_dict = {}
        for i in range(len(self.file_names)):
            extension = self.file_names[i].split(".")[-1]
            if extension not in extension_dict:
                extension_dict[extension] = os.path.join(self.root_dir, extension)
        self.extension_dict = extension_dict
        if self.debug:
            print(self.extension_dict)

    def create_dir(self):
        """This function creates the directories, if they do not already exist."""
        count = 0
        for i in range(len(self.keys)):
            if self.keys[i] not in self.dirs:
                try:
                    os.mkdir(os.path.join(self.root_dir, self.keys[i]))
                    count += 1
                except FileExistsError:
                    # the file/directory with the same name already exists
                    pass
        print("{} directories were created.".format(count))


    def move_to_dirs(self):
        """This function moves the files to their respective directories, and removes duplicates."""
        count = 0
        for file_name in self.file_names:
            extension = file_name.split(".")[-1]
            file_path = os.path.join(self.root_dir, file_name)
            destination_path = self.extension_dict[extension]
            if os.path.exists(os.path.join(destination_path, file_name)):
                # delete the duplicate file
                os.remove(file_path)
            else:
                try:
                    shutil.move(file_path, destination_path)
                    count += 1
                except Exception as e:
                    print(str(e) + " deleting file...")
                    # delete the file
                    os.remove(file_path)
        print("{} files were moved.".format(count))

    def deletion_check(self):
        """This function checks if the files are older than the specified number of months."""
        last_month = datetime.datetime.now() - datetime.timedelta(days=DELETE_IF_UNUSED_AFTER)
        count = 0
        for i in range(len(self.dirs)):
            if self.dirs[i] in self.keys:
                if os.path.getmtime(os.path.join(self.root_dir, self.dirs[i])) < last_month:
                    shutil.rmtree(os.path.join(self.root_dir, self.dirs[i]))
                    count += 1
        print("{} directories were deleted.".format(count))

    def run(self):
        """This function runs the program."""
        self.get_file_names()
        self.find_file_extension()
        self.create_dir()
        self.move_to_dirs()
        # self.deletion_check()
        print("{} seconds were taken.".format(time.time() - self.start))


if __name__ == "__main__":
    Clean().run()
