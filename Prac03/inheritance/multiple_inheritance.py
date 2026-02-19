class Father:
    def skills(self):
        print("Бағдарламалау біледі")

class Mother:
    def talent(self):
        print("Сурет сала алады")

class Child(Father, Mother):
    pass

c = Child()
c.skills()
c.talent()

class A:
    def show(self):
        print("A класы")

class B:
    def show(self):
        print("B класы")

class C(A, B):
    pass

obj = C()
obj.show()

class A:
    def greet(self):
        print("Сәлем A")

class B:
    def greet(self):
        print("Сәлем B")

class C(A, B):
    def greet(self):
        super().greet()
        print("Сәлем C")

c = C()
c.greet()
