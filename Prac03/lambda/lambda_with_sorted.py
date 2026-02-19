numbers = [5, 2, 9, 1, 7]

sorted_numbers = sorted(numbers, key=lambda x: x, reverse=True)

print(sorted_numbers)  # [9, 7, 5, 2, 1]

words = ["python", "ai", "code", "programming", "it"]

sorted_words = sorted(words, key=lambda word: len(word))

print(sorted_words)

students = [
    {"name": "Айжан", "grade": 85},
    {"name": "Ержан", "grade": 92},
    {"name": "Дана", "grade": 78}
]

sorted_students = sorted(students, key=lambda student: student["grade"])

for student in sorted_students:
    print(student)
