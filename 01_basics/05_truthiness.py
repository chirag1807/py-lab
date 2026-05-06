# Truthiness and Falsiness Demonstrations

print("--- Truthiness & Falsiness ---")

# Values that evaluate to False
false_values = [False, None, 0, 0.0, "", [], {}, set()]
for idx, val in enumerate(false_values, start=1):
    if val:
        print(f"{idx}. Unexpected truthy: {val!r}")
    else:
        print(f"{idx}. Correctly falsy: {val!r}")

print("\n--- Truthy Values ---")
# Values that evaluate to True
truthy_values = [True, 1, -1, 0.1, "non-empty", [1], {"a": 1}, (1,)]
for idx, val in enumerate(truthy_values, start=1):
    if val:
        print(f"{idx}. Correctly truthy: {val!r}")
    else:
        print(f"{idx}. Unexpected falsy: {val!r}")

print("\n--- Simple Conditional Example ---")
user_input = input("Enter a non‑empty string to see a truthy check: ")
if user_input:
    print(f"You entered: '{user_input}' – this is truthy.")
else:
    print("You entered an empty string – this is falsy.")
