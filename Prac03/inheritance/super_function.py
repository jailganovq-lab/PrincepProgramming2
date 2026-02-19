class Person:
    def __init__(self, name):
        self.name = name
        print("Person конструкторы шақырылды")

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade
        print("Student конструкторы шақырылды")

s = Student("Айжан", 95)

class Animal:
    def speak(self):
        print("Жануар дыбыс шығарады")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Ит үреді")

d = Dog()
d.speak()

class A:
    def show(self):
        print("A класы")

class B(A):
    def show(self):
        super().show()
        print("B класы")

class C(B):
    def show(self):
        super().show()
        print("C класы")

obj = C()
obj.show()
