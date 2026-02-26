def squares(a, b):
    for i in range(a, b + 1):
        yield i**2
n,b=map(int, input().split())

for value in squares(n, b):
    print(value)