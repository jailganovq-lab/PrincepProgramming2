class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} үріп жатыр!"

d1 = Dog("Ақтөс")
print(d1.bark())

class Student:
    school_name = "Python Academy"

    def __init__(self, name): # init Бұл — әр объектке жеке берілетін айнымалы.
        self.name = name

    @classmethod
    def get_school_name(cls): # Class method - cls - Классқа ортақ мәліметпен жұмыс істейді- cls классқа сілтеме.
        return cls.school_name

print(Student.get_school_name())

class MathUtils:
    @staticmethod # Бірақ классқа да, объектке де тәуелді емес
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

print(MathUtils.add(5, 3))
print(MathUtils.multiply(4, 6))
