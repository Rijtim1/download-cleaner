from config import DOWNLOAD_PATH, DELETE_IF_OLDER_THAN_MONTHS
import os
import shutil
import time


class Clean:
    def __init__(self):
        self.dirnames = []
        self.file_names = []
        self.keys = []
        self.count = 0
        self.start = time.time()
        self.last_month = time.strftime(
            "%d-%m-%Y", time.localtime(time.time() - 60 * 60 * 24 * DELETE_IF_OLDER_THAN_MONTHS)
        )

    def get_file_names(self, path):
        """This function gets the file names in the downloads folder."""
        for dirname, dirnames, filenames in os.walk(path):
            self.dirnames.append(dirname)
            self.file_names.append(filenames)

    def find_keys(self):
        """This function finds the keys in the file names."""
        for i in range(len(self.file_names)):
            for j in range(len(self.file_names[i])):
                if self.file_names[i][j] not in self.keys:
                    self.keys.append(self.file_names[i][j])

    def create_dir(self, dirnames, keys):
        """This function creates the directories."""
        for i in range(len(keys)):
            if keys[i] not in dirnames:
                path = DOWNLOAD_PATH + r"/" + keys[i]
                try:
                    os.makedirs(path)
                except IOError:
                    pass
                self.count += 1
            else:
                print("{} is already there, skipping".format(keys[i]))

    def move_to_dirs(self, keys, values):
        """This function moves the files to their respective directories."""
        for i in range(len(keys)):
            for j in range(len(values)):
                if keys[i] in values[j]:
                    try:
                        shutil.move(
                            DOWNLOAD_PATH + r"/" + values[j],
                            DOWNLOAD_PATH + r"/" + keys[i],
                        )
                    except Exception as e:
                        os.remove(DOWNLOAD_PATH + r"/" + values[j])
                        print("{} occured.".format(e))
                        print("The file was deleted.")

    def delete_if_older(self):
        """This function deletes the directories if the directory date modified is older than a month"""
        for dirname in self.dirnames:
            if os.path.getmtime(dirname) < time.mktime(
                time.strptime(self.last_month, "%d-%m-%Y")
            ):
                shutil.rmtree(dirname)

    def run(self):
        """This function runs the program."""
        self.get_file_names(DOWNLOAD_PATH)
        self.find_keys()
        self.create_dir(self.dirnames, self.keys)
        self.move_to_dirs(self.keys, self.file_names)
        self.delete_if_older()
        print("{} directories were created.".format(self.count))
        print("{} directories were deleted.".format(self.count))
        print("{} seconds were taken.".format(time.time() - self.start))

if __name__ == "__main__":
    Clean().run()
