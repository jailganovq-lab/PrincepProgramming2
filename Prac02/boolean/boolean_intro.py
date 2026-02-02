# 1. Boolean типін тексеру
is_active = True
print(type(is_active))  # <class 'bool'>
# 2. Boolean мәнін input арқылы алу
answer = input("Are you ready? (yes/no): ")
is_ready = answer == "yes"

print(is_ready)
# 3. Сан нөлге тең бе — Boolean нәтиже
number = 0
is_zero = number == 0

print(is_zero)  # True
# 4. Boolean айнымалыны қайта тағайындау
logged_in = False
print(logged_in)

logged_in = True
print(logged_in)
# 5. Boolean мәнін print ішінде қолдану
has_money = True

print("Has money:", has_money)
