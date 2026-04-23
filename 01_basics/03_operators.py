# Basic Operators

print("--- Arithmetic Operators ---")
a = 10
b = 3

print(f"a = {a}, b = {b}\n")

# Addition (+)
print(f"Addition (a + b): {a + b}")

# Subtraction (-)
print(f"Subtraction (a - b): {a - b}")

# Multiplication (*)
print(f"Multiplication (a * b): {a * b}")

# Division (/) - Always returns a float
print(f"Division (a / b): {a / b}")

# Floor Division (//) - Returns an integer, rounding down
print(f"Floor Division (a // b): {a // b}")

# Modulo / Remainder (%)
print(f"Modulo (a % b): {a % b}")

# Exponentiation / Power (**)
print(f"Exponentiation (a ** b): {a ** b}")


print("\n--- Augmented Assignment Operators ---")
x = 10
print(f"Initial x: {x}")

x += 5  # Equivalent to x = x + 5
print(f"After x += 5: {x}")

x -= 3  # Equivalent to x = x - 3
print(f"After x -= 3: {x}")

x *= 2  # Equivalent to x = x * 2
print(f"After x *= 2: {x}")

x /= 4  # Equivalent to x = x / 4
print(f"After x /= 4: {x}")


print("\n--- Comparison Operators ---")
p = 5
q = 8

print(f"p = {p}, q = {q}\n")

print(f"Equal to (p == q): {p == q}")
print(f"Not equal to (p != q): {p != q}")
print(f"Greater than (p > q): {p > q}")
print(f"Less than (p < q): {p < q}")
print(f"Greater than or equal to (p >= q): {p >= q}")
print(f"Less than or equal to (p <= q): {p <= q}")
