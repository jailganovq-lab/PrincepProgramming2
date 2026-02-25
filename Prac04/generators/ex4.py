def squares(a, b):
    for i in range(a, b + 1):
        yield i**2
n=int(input())
b=int(input())
for value in squares(n, b):
    print(value, end=" ")