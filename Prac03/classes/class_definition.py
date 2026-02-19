class Person:
    def greet(self):
        print("Сәлем! Мен адаммын.")

p1 = Person()
p1.greet()

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Аты: {self.name}, Жасы: {self.age}")

s1 = Student("Айбек", 20)
s1.info()

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

calc = Calculator()

print("Қосу:", calc.add(10, 5))
print("Азайту:", calc.subtract(10, 5))
print("Көбейту:", calc.multiply(10, 5))
