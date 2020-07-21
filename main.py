import os
from os import walk
import shutil

DOWNLOADS_PATH = r"C:\Users\rijan\Downloads"
f = []
keys = []
values = []
for (dirpath, dirnames, filenames) in walk(DOWNLOADS_PATH):
    f.extend(filenames)
    break
for items in f:
    if items[-3:] in keys:
        pass
    else:
        keys.append(items[-3:])
for i in range(len(keys)):
    for items in f:
        if keys[i] in items:
            values.append(items)
for key in keys:
    path = r"C:\Users\rijan\Downloads" + r"/" + key
    try:
        os.mkdir(path)
        print('{} successfully created in {}'.format(key, path))
    except:
        print("Exception occured and was handled properly")
for i in range(len(keys)):
    for j in range(len(values)):
        if keys[i] in values[j]:
            try:
                shutil.move(r"C:\Users\rijan\Downloads"+r"/"+values[j], r"C:\Users\rijan\Downloads"+r"/"+keys[i])
            except:
                print("Exception happend but was handeled I think lol")
