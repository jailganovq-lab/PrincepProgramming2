def introduce(name, age):
    print(f"Менің атым {name}, жасым {age}")

introduce("Али", 20)
def greet(name, message="Сәлем"):
    print(f"{message}, {name}!")

greet("Айжан")
greet("Ержан", "Қайырлы күн")
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def user_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print("Қосынды:", sum_all(1, 2, 3, 4, 5))

user_info(name="Дана", age=22, city="Алматы")
