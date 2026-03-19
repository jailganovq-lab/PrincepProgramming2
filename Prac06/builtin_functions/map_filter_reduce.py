numbers = [1, 2, 3, 4, 5, 6]

# map(): square each number
squared = list(map(lambda x: x**2, numbers))
print("Squared:", squared)

# filter(): keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Evens:", evens)


from functools import reduce

numbers = [1, 2, 3, 4, 5]

# reduce(): find product of all numbers
product = reduce(lambda x, y: x * y, numbers)
print("Product:", product)