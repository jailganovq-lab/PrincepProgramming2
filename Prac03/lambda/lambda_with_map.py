numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)  # [2, 4, 6, 8]

words = ["python", "ai", "code", "programming", "it"]

long_words = list(filter(lambda word: len(word) > 4, words))

print(long_words)

numbers = [-10, 5, -3, 8, 0, -1, 12]

positive_numbers = list(filter(lambda x: x > 0, numbers))

print(positive_numbers)  # [5, 8, 12]
