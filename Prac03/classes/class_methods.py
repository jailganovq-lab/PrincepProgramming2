class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} үріп жатыр!"

d1 = Dog("Ақтөс")
print(d1.bark())

class Student:
    school_name = "Python Academy"

    def __init__(self, name):
        self.name = name

    @classmethod
    def get_school_name(cls):
        return cls.school_name

print(Student.get_school_name())

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

print(MathUtils.add(5, 3))
print(MathUtils.multiply(4, 6))
