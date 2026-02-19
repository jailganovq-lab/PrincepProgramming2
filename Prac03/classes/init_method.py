class Person:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} объектісі құрылды")

p1 = Person("Али")

class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def info(self):
        print(f"Көлік: {self.brand}, Жылы: {self.year}")

c1 = Car("Toyota", 2022)
c1.info()

class User:
    def __init__(self, username, role="Қолданушы"):
        self.username = username
        self.role = role

    def show(self):
        print(f"Пайдаланушы: {self.username}, Рөлі: {self.role}")

u1 = User("admin", "Әкімші")
u2 = User("guest")

u1.show()
u2.show()
