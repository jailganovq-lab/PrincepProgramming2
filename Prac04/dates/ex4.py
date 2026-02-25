#task4
#Write a Python program to calculate two date difference in seconds.


from datetime import datetime , timedelta 
today = datetime.now()

yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print(yesterday)
print(tomorrow)
dif = tomorrow - yesterday
second = dif.total_seconds()
print(int(second))