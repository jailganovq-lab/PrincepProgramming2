import shutil

# copy file
shutil.copy("example.txt", "parent/child/example_copy.txt")

# move file
shutil.move("example.txt", "parent/example_moved.txt")

print("File copied and moved!")