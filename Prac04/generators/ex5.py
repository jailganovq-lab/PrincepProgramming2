def squares(b):
    for i in range(b, -1, -1):
        yield i 
n=int(input())

for value in squares(n):
    print(value, end=" ")