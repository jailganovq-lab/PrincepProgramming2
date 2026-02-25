class Animal:
    def speak(self):
        print("Жануар дыбыс шығарады")

class Dog(Animal):
    pass #pass → ештеңе қоспаймыз деген сөз.

d = Dog()
d.speak()

class Animal:
    def speak(self):
        print("Жануар дыбыс шығарады")

class Cat(Animal):
    def speak(self):
        print("Мысық мияулайды")

c = Cat()
c.speak()

class Person:
    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"Аты: {self.name}")

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name) #класстың методын шақыру.
        self.grade = grade

    def info(self):
        super().info()
        print(f"Бағасы: {self.grade}")

s = Student("Айбек", 90)
s.info()
