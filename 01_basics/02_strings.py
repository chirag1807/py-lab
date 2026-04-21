# 1. String Methods
course = "Python for Beginners"

print(course.upper())
print(course.lower())

print("Python" in course)
print(course.find("for"))   # Returns index or -1 if not found

print(course.replace("Beginners", "Experts"))
print(course.split())


# 2. String Slicing
print("First letter:", course[0])
print("First six letters:", course[0:6])

print("Last character:", course[-1])
print("Last word:", course[-9:])


# 3. f-strings
name = "Chirag"
age = 23

print(f"My name is {name}")
print(f"I am {age} years old")
print(f"Next year I will be {age + 1}")
