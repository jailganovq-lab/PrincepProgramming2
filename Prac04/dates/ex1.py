#task1
# Write a Python program to subtract five days from current date.
from datetime import datetime, timedelta
#timedelta for increasing or decreasing time

current_date = datetime.now()


new_date = current_date - timedelta(days=5)

print("Current date:", current_date.strftime("%Y-%m-%d"))
print("Date 5 days ago:", new_date.strftime("%Y-%m-%d"))