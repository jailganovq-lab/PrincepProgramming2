def greet():
    print("Сәлем, Python үйренуші!")

greet()
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print("Қосынды:", result)
def is_even(number):
    return number % 2 == 0

def check_number(num):
    if is_even(num):
        print(num, "жұп сан")
    else:
        print(num, "тақ сан")

check_number(10)
check_number(7)
