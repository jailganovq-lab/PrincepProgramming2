names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]

# enumerate(): index + value
for i, name in enumerate(names):
    print(i, name)

# zip(): combine two lists
for name, score in zip(names, scores):
    print(name, score)

values = ["10", "20", "30", "abc"]

converted = []

for v in values:
    # type checking before conversion
    if v.isdigit():
        num = int(v)   # string → int
        converted.append(num)
    else:
        print(f"Cannot convert '{v}' to int")

print("Converted list:", converted)

