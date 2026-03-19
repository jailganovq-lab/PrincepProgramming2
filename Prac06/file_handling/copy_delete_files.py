import shutil

# create backup
shutil.copy("data.txt", "data_backup.txt")

print("Backup done")


import os

filename = "data.txt"

if os.path.exists(filename):
    os.remove(filename)
    print("file removed")
else:
    print("file do not exist")
