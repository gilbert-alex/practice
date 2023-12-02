'''
Examples of string methods
'''

# loop to uppercase every character
before = input("Before: ")
print("After: ", end="")
for c in before:
    print(c.upper(), end="")
print()

# method to uppercase every character
after = before.upper()
print(f"After: {after}")

print(before)
print()