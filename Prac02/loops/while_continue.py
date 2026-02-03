i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

i = 0

while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)



numbers = [3, -1, 5, -7, 2]
i = 0

while i < len(numbers):
    if numbers[i] < 0:
        i += 1
        continue
    print(numbers[i])
    i += 1
