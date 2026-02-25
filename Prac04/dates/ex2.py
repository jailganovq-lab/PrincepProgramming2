#task2
#Write a Python program to print yesterday, today, tomorrow.

from datetime import datetime , timedelta

today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print(today)
print(yesterday)
print(tomorrow)
