square = lambda x: x ** 2

print(square(5))  # 25

add = lambda a, b: a + b

result = add(10, 15)
print("Қосынды:", result)

students = [
    ("Айжан", 85),
    ("Ержан", 92),
    ("Дана", 78)
]


sorted_students = sorted(students, key=lambda student: student[1])

print(sorted_students)
