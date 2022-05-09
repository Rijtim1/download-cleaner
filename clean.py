from config import DOWNLOAD_PATH
import os
import shutil
import time


class Clean:

    def __init__(self):
        self.file_names = []
        self.keys = []
        self.start = time.time()
        self.debug = False

    def get_file_names(self):
        """This function gets the file names in the downloads folder."""
        self.root_dir, self.dirs, self.file_names = os.walk(
            DOWNLOAD_PATH).__next__()
        if self.debug:
            print(self.root_dir, self.dirs, self.file_names)

    def find_file_extension(self):
        """This function finds the keys in the file names."""
        for i in range(len(self.file_names)):
            _, extension = self.file_names[i].split(".")
            if extension not in self.keys:
                self.keys.append(extension)
        self.keys = list(set(self.keys))
        if self.debug:
            print(self.keys)

    def create_dir(self):
        """This function creates the directories."""
        count = 0
        for i in range(len(self.keys)):
            if self.keys[i] not in self.dirs:
                os.mkdir(os.path.join(self.root_dir, self.keys[i]))
                count += 1
        print("{} directories were created.".format(count))

    def move_to_dirs(self):
        """This function moves the files to their respective directories."""
        count = 0
        for i in range(len(self.file_names)):
            _, extension = self.file_names[i].split(".")
            if extension in self.keys:
                try:
                    shutil.move(
                        os.path.join(self.root_dir, self.file_names[i]),
                        os.path.join(self.root_dir, extension))
                    count += 1
                except Exception as e:
                    print(e + "deleting file...")
                    # delete the file
                    os.remove(os.path.join(self.root_dir, self.file_names[i]))
        print("{} files were moved.".format(count))

    def run(self):
        """This function runs the program."""
        self.get_file_names()
        self.find_file_extension()
        self.create_dir()
        self.move_to_dirs()
        print("{} seconds were taken.".format(time.time() - self.start))


if __name__ == "__main__":
    Clean().run()
