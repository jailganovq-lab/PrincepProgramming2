import re

# 1. Match a string that has 'a' followed by zero or more 'b'
print("1 Task")
text1 = "abbb"
pattern1 = r"ab*"
print("Match:", bool(re.fullmatch(pattern1, text1)))
print()


# 2. Match a string that has 'a' followed by two to three 'b'
print("2 Task")
text2 = "abb"
pattern2 = r"ab{2,3}"
print("Match:", bool(re.fullmatch(pattern2, text2)))
print()


# 3. Find sequences of lowercase letters joined with underscore
print("3 Task")
text3 = "hello_world test_case example"
pattern3 = r"[a-z]+_[a-z]+"
print("Result:", re.findall(pattern3, text3))
print()


# 4. Find sequences of one uppercase letter followed by lowercase letters
print("4 Task")
text4 = "Hello World Python Programming"
pattern4 = r"[A-Z][a-z]+"
print("Result:", re.findall(pattern4, text4))
print()


# 5. Match string that has 'a' followed by anything ending with 'b'
print("5 Task")
text5 = "a123b"
pattern5 = r"a.*b"
print("Match:", bool(re.fullmatch(pattern5, text5)))
print()


# 6. Replace space, comma, or dot with colon
print("6 Task")
text6 = "Hello, world. Python is cool"
result6 = re.sub(r"[ ,\.]", ":", text6)
print("Result:", result6)
print()


# 7. Convert snake_case to camelCase
print("7 Task")
snake = "hello_world_python"
words = snake.split("_")
camel = words[0] + "".join(word.capitalize() for word in words[1:])
print("Result:", camel)
print()


# 8. Split string at uppercase letters
print("8 Task")
text8 = "HelloWorldPython"
result8 = re.findall(r"[A-Z][^A-Z]*", text8)
print("Result:", result8)
print()


# 9. Insert spaces between words starting with capital letters
print("9 Task")
text9 = "HelloWorldPython"
result9 = re.sub(r"([A-Z])", r" \1", text9).strip()
print("Result:", result9)
print()


# 10. Convert camelCase to snake_case
print("10 Task")
text10 = "helloWorldPython"
snake_case = re.sub(r"([A-Z])", r"_\1", text10).lower()
print("Result:", snake_case)