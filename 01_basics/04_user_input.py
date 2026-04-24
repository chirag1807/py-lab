# Getting User Input

print("--- Basic Input ---")
# The input() function pauses execution and waits for the user to type something
# It ALWAYS returns a string (str), regardless of what the user types
name = input("Enter your name: ")
print(f"Hello, {name}!\n")

print("--- Converting Input Data Types ---")
# Because input() returns a string, we cannot do math with it directly
age_str = input("Enter your age: ")

# We must cast (convert) the string to an integer
age = int(age_str)

print(f"Next year, you will be {age + 1} years old.")
print(f"Type of age_str: {type(age_str).__name__}")
print(f"Type of age: {type(age).__name__}\n")

print("--- Input in a single line ---")
# You can wrap the input() directly inside the cast to save lines
height = float(input("Enter your height in meters (e.g., 1.75): "))
print(f"Your height is {height}m.")
