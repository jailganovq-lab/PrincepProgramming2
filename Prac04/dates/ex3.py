#task3
#Write a Python program to drop microseconds from datetime.


from datetime import datetime

now = datetime.now()

# Remove microseconds
new_time = now.replace(microsecond=0)

print("Original:", now)
print("Without microsec:", new_time)