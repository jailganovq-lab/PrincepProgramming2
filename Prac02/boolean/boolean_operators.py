# 1
a = 10
b = 5

print(a > 5 and b < 10)  # True

# 2
x = 3
y = 8

print(x > 5 or y > 5)  # True

# 3
is_raining = False

print(not is_raining)  # True

# 4
age = 20
has_id = True

if age >= 18 and has_id:
    print("Access granted")
else:
    print("Access denied")

# 5
is_weekend = False
is_holiday = True

can_relax = not is_weekend or is_holiday
print(can_relax)  # True
