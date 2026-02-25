n = int(input())

numbers = []
for i in range(0, n + 1):
    if i % 3 == 0 and i % 4 ==0:
        numbers.append(str(i))

print(",".join(numbers))