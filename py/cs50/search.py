# implement linear search

import sys
# a list of names
names = ["Bill", "Charlie", "Fred", "George", "Ginny", "Percy", "Ron"]

# ask for a name
name = input("Name: ")

# search for name
for n in names:
    if n == name:
        print("Found")
        sys.exit(0)
print("Not Found")
sys.exit(1)

# same as
for name in names:
    print("Found")
    sys.exit(0)
print("Not Found")
sys.exit(1)