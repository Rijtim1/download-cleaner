import os
from os import walk
import shutil

DOWNLOADS_PATH = r"C:\Users\rijan\Downloads"


def get_file_names(path=DOWNLOADS_PATH):
    f = []
    for (dirpath, dirnames, filenames) in walk(DOWNLOADS_PATH):
        f.extend(filenames)
        break
    return f


def find_keys(file_names):
    keys = []
    for items in file_names:
        if items[-3:] in keys:
            pass
        else:
            keys.append(items[-3:])
    return keys


def find_values(file_names, keys):
    values = []
    for i in range(len(keys)):
        for items in file_names:
            if keys[i] in items:
                values.append(items)
    return values


def create_dir(keys):
    for key in keys:
        path = r"C:\Users\rijan\Downloads" + r"/" + key
        try:
            os.mkdir(path)
            print('{} successfully created in {}'.format(key, path))
        except Exception as e:
            print("{} occured".format(e))
            print("But was handled properly")


def move_to_dirs(keys, values):
    for i in range(len(keys)):
        for j in range(len(values)):
            if keys[i] in values[j]:
                try:
                    shutil.move(r"C:\Users\rijan\Downloads" + r"/" + values[j],
                                r"C:\Users\rijan\Downloads" + r"/" + keys[i])
                except Exception as e:
                    print("{} happened".format(e))
                    print("But was handeled")


if __name__ == '__main__':
    file_names = get_file_names(DOWNLOADS_PATH)
    keys = find_keys(file_names)
    values = find_values(file_names, keys)
    create_dir(keys)
    move_to_dirs(keys, values)
