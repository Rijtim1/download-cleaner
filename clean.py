import os
from os import walk
import shutil
import time

DOWNLOADS_PATH = r"C:\Users\rijan\Downloads"


def get_file_names(path=DOWNLOADS_PATH):
    """This function adds all the files in a set directory to a list."""
    file_names = []
    for (dirpath, dirnames, filenames) in walk(path):
        file_names.extend(filenames)
        break
    return file_names


def find_keys(file_names):
    """This function looks at each of the files in the list the function above creates,
            and stores the file extension on a list. This will later be used to create
            the dir where the respective files will move to."""
    keys = []
    for items in file_names:
        dot = items.rindex(".")
        if items[dot+1:] in keys:
            pass
        else:
            keys.append(items[dot+1:])
    return keys


def create_dir(keys):
    """This function creats the a new directory for each file extension type."""
    for key in keys:
        path = DOWNLOADS_PATH + r"/" + key
        try:
            os.mkdir(path)
            print('{} successfully created in {}'.format(key, path))
        except Exception as e:
            print("{} occured".format(e))
            print("But was handled properly")


def move_to_dirs(keys, values):
    """This function moves the files into their respective directory."""
    for i in range(len(keys)):
        for j in range(len(values)):
            if keys[i] in values[j]:
                try:
                    shutil.move(DOWNLOADS_PATH + r"/" + values[j],
                                DOWNLOADS_PATH + r"/" + keys[i])
                except Exception as e:
                    print("{} happened".format(e))
                    print("But was handeled")


if __name__ == '__main__':
    start = time.time()
    print("Getting File Names")
    file_names = get_file_names(DOWNLOADS_PATH)
    print("{} files found in downloads folder.".format(len(file_names)))
    print("Getting Ready To Create Folders")
    keys = find_keys(file_names)
    print("Creating Folders")
    print("{} new folders created".format(len(keys)))
    create_dir(keys)
    print("Moving!!!!")
    move_to_dirs(keys, file_names)
    print("Finished")
    print("Time taken: {:.2}".format(time.time() - start))
