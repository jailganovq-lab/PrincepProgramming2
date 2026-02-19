class Animal:
    def speak(self):
        print("Жануар дыбыс шығарады")

class Dog(Animal):
    def speak(self):
        print("Ит үреді")

d = Dog()
d.speak()

class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

r = Rectangle(5, 4)
print("Ауданы:", r.area())

class Employee:
    def get_role(self):
        print("Қызметкер")

class Manager(Employee):
    def get_role(self):
        super().get_role()
        print("Менеджер")

m = Manager()
m.get_role()
