# The Basics

# 1. Hello World
print("Hello, World!")

# 2. Variables & Data Types
my_name = "Chirag"       # str (string)
my_age = 23              # int (integer)
height = 1.75            # float (decimal number)
is_learning = True       # bool (boolean)

# Printing variables using f-strings
print(f"My name is {my_name}, I am {my_age} years old and my height is {height}m.")
print(f"Is learning python? {is_learning}")

# Checking data types using type() function
print("\n--- Checking Data Types ---")
print(f"Type of my_name: {type(my_name).__name__}")
print(f"Type of my_age: {type(my_age).__name__}")
print(f"Type of height: {type(height).__name__}")
print(f"Type of is_learning: {type(is_learning).__name__}")


# 3. Variable Syntax & Assignment

print("\n--- Variable Syntax ---")

# Basic assignment
x = 10
y = "Hello"

# Multiple assignment
a, b, c = 1, 2, 3
print(f"a={a}, b={b}, c={c}")

# Same value to multiple variables
p = q = 100
print(f"p={p}, q={q}")

# Swapping variables
a, b = b, a
print(f"After swapping: a={a}, b={b}")


# 4. Variable Reassignment

print("\n--- Variable Reassignment ---")
x = 10
print(f"x initially: {x}")

x = x + 10
print(f"x after x = x + 10: {x}")

x = 5
print(f"x after reassignment to 5: {x}")


# 5. References in Python

print("\n--- Reference Behavior ---")
a = 10
b = a

print(f"a: {a}, b: {b}")

b = 20
print("After changing b:")
print(f"a: {a}, b: {b}")   # a unchanged


# 6. Mutable vs Immutable

print("\n--- Mutable vs Immutable ---")

# Immutable example
num1 = 10
num2 = num1
num2 += 5

print("Immutable example:")
print(f"num1: {num1}, num2: {num2}")

# Mutable example
list1 = [1, 2]
list2 = list1

list2.append(3)

print("Mutable example:")
print(f"list1: {list1}, list2: {list2}")


# 7. Identity vs Equality

print("\n--- Identity vs Equality ---")
x = [1, 2]
y = x

print(f"x == y: {x == y}")   # True (same value)
print(f"x is y: {x is y}")   # True (same object)


# 8. Memory Check using id()

print("\n--- Memory Addresses (id) ---")
x = 10
y = 10

print(f"id(x): {id(x)}")
print(f"id(y): {id(y)}")
