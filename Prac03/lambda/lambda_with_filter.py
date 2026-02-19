numbers = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x ** 2, numbers))

print(squared)  # [1, 4, 9, 16, 25]

celsius = [0, 20, 30, 40]

fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))

print(fahrenheit)

list1 = [1, 2, 3]
list2 = [4, 5, 6]

sum_lists = list(map(lambda x, y: x + y, list1, list2))

print(sum_lists)  # [5, 7, 9]
