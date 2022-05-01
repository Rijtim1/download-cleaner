import os
from os import walk
import shutil
import time
import config


def get_file_names(path=config.DOWNLOAD_PATH):
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
        if items[dot + 1 :] in keys:
            pass
        else:
            keys.append(items[dot + 1 :])
    return keys


def create_dir(dirnames, keys):
    """This function creats the a new directory for each file extension type."""
    count = 0
    for i in range(len(keys)):
        if keys[i] not in dirnames:
            path = config.DOWNLOAD_PATH + r"/" + keys[i]
            try:
                os.makedirs(path)
            except IOError:
                pass
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
                    shutil.move(
                        config.DOWNLOAD_PATH + r"/" + values[j],
                        config.DOWNLOAD_PATH + r"/" + keys[i],
                    )
                except Exception as e:
                    os.remove(config.DOWNLOAD_PATH + r"/" + values[j])
                    print("{} occured.".format(e))
                    print("The file was deleted.")


def delete_if_older(num_months):
    """This function deletes the directory if the directory date modified is older than a month"""
    # get the date of the last month
    # last_month = time.strftime("%d-%m-%Y", time.localtime(time.time() - 60 * 60 * 24 * 30))
    last_month = time.strftime(
        "%d-%m-%Y", time.localtime(time.time() - 60 * 60 * 24 * num_months)
    )
    # get the list of all the directories in the downloads folder
    dir_list = os.listdir(config.DOWNLOAD_PATH)
    # iterate through the list of directories
    for dir in dir_list:
        # get the date of the last modified file in the directory
        last_modified_date = time.strftime(
            "%d-%m-%Y",
            time.localtime(os.path.getmtime(config.DOWNLOAD_PATH + r"/" + dir)),
        )
        # if the last modified date is older than a month, delete the directory
        if last_modified_date < last_month:
            shutil.rmtree(config.DOWNLOAD_PATH + r"/" + dir)
            print("{} was deleted.".format(dir))


if __name__ == "__main__":
    start = time.time()
    print("Getting File Names\n")
    dirnames, file_names = get_file_names(config.DOWNLOAD_PATH)
    print("{} files found in downloads folder.\n".format(len(file_names)))
    print("Getting Ready To Create Folders\n")
    keys = find_keys(file_names)
    print("Creating Folders\n")
    create_dir(dirnames, keys)
    print("Moving!!!!\n")
    move_to_dirs(keys, file_names)
    print("Finished\n")
    print("Deleting Folders if older than a month\n")
    delete_if_older(config.DELETE_IF_OLDER_THAN_MONTHS)
    print("Time taken: {:.2}".format(time.time() - start))
