def square(number):
    return number ** 2

result = square(4)
print("Квадраты:", result)
def calculate(a, b):
    add = a + b
    subtract = a - b
    multiply = a * b
    return add, subtract, multiply

result = calculate(10, 5)

print("Қосу:", result[0])
print("Азайту:", result[1])
print("Көбейту:", result[2])
def check_pass(score):
    if score >= 50:
        return "Өтті"
    else:
        return "Құлады"

print(check_pass(75))
print(check_pass(40))
