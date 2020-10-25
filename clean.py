import os
from os import walk
import shutil
import time

# downloads folder path
DOWNLOADS_PATH = r"C:\Users\rijan\Downloads"


def get_file_names(path=DOWNLOADS_PATH):
    """This function adds all the files in a set directory to a list."""
    file_names = []
    for (dirpath, dirnames, filenames) in walk(path):
        file_names.extend(filenames)
        break
    return dirnames, file_names


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


def create_dir(dirnames, keys):
    """This function creats the a new directory for each file extension type."""
    count = 0
    for i in range(len(keys)):
        if keys[i] not in dirnames:
            path = DOWNLOADS_PATH + r"/" + keys[i]
            os.makedirs(path)
            count += 1
        else:
            print("{} is already there, skipping".format(keys[i]))
    print("{} new folders created\n".format(count))


def move_to_dirs(keys, values):
    """This function moves the files into their respective directory."""
    for i in range(len(keys)):
        for j in range(len(values)):
            if keys[i] in values[j]:
                try:
                    shutil.move(DOWNLOADS_PATH + r"/" + values[j],
                                DOWNLOADS_PATH + r"/" + keys[i])
                except Exception as e:
                    os.remove(DOWNLOADS_PATH + r"/" + values[j])
                    print("{} occured.".format(e))
                    print("The file was deleted.")


if __name__ == '__main__':
    start = time.time()
    print("Getting File Names\n")
    dirnames, file_names = get_file_names(DOWNLOADS_PATH)
    print("{} files found in downloads folder.\n".format(len(file_names)))
    print("Getting Ready To Create Folders\n")
    keys = find_keys(file_names)
    print("Creating Folders\n")
    create_dir(dirnames, keys)
    print("Moving!!!!\n")
    move_to_dirs(keys, file_names)
    print("Finished\n")
    print("Time taken: {:.2}".format(time.time() - start))
