# Assignment 1 : Make a simple calculator using 2 inputs
x = int(input("Enter the first number :"))
y = int(input("Enter the second number :"))

# Arithmetic operators
print("Add =", x + y)
print("Sub =", x - y)
print("Mul =", x * y)
print("Div =", x / y)
print("Mod =", x % y)
print("Exp =", x ** y)
print("Floor div =", x // y)

# Comparison operators
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

# Logical operators
print("And =", x > 3 and 10 < y)
print("Or =", x > 4 or 8 < y)
print("not =", (not (x < 3 and y > 10)))
