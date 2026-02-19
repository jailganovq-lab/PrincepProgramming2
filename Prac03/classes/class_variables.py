class Student:
    school_name = "Python Academy"  # Class variable

    def __init__(self, name):
        self.name = name  # Instance variable

s1 = Student("Айжан")
s2 = Student("Ержан")

print(s1.school_name)
print(s2.school_name)


class Car:
    wheels = 4  # Class variable

c1 = Car()
c2 = Car()

Car.wheels = 6  # Класс арқылы өзгерту

print(c1.wheels)
print(c2.wheels)

class User:
    user_count = 0  # Class variable

    def __init__(self, username):
        self.username = username
        User.user_count += 1

u1 = User("admin")
u2 = User("guest")
u3 = User("moderator")

print("Қолданушылар саны:", User.user_count)

