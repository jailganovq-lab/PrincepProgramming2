import os

# create nested directories: parent/child/grandchild
os.makedirs("parent/child/grandchild", exist_ok=True)

print("Directories created!")


import os

path = "parent"

# list all items
items = os.listdir(path)
print("All items:", items)

# separate files and folders
for item in items:
    full_path = os.path.join(path, item)
    if os.path.isfile(full_path):
        print("File:", item)
    elif os.path.isdir(full_path):
        print("Folder:", item)

import os

path = "parent"

for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith(".txt"):
            print("Found .txt file:", os.path.join(root, file))