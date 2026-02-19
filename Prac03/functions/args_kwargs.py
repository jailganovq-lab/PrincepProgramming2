def multiply_all(*numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

print(multiply_all(2, 3, 4))  # 24
def print_student_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_student_info(name="Айбек", age=19, city="Шымкент")

def show_data(*args, **kwargs):
    print("Позициялық аргументтер:")
    for arg in args:
        print(arg)

    print("\nАтаулы аргументтер:")
    for key, value in kwargs.items():
        print(f"{key} = {value}")

show_data(10, 20, 30, name="Дана", course="Python")
