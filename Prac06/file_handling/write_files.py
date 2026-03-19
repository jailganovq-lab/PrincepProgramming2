with open("data.txt", "w") as file:
    file.write("Hello, this is sample data\n")
    file.write("Python file handling practice\n")

print("file opened and information was written")


# append new data
with open("data.txt", "a") as file:
    file.write("New line added\n")
    file.write("Another line\n")

# read again to verify
with open("data.txt", "r") as file:
    print("new file:")
    print(file.read())