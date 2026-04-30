# User Input

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"Hello {name}, you are {age} years old")

# Age Check
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# Logical Check
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Both > 10:", a > 10 and b > 10)
print("At least one < 5:", a < 5 or b < 5)
print("First not greater than second:", not (a > b))
