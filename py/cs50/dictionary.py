# implements a phone book

people = {
    "Carter": "+1-617-495-1000",
    "David": "+1-949-468-2750"
}

# search for name
# key is the input string and used to index the dict
# value is what's returned
name = input("Name: ")
if name in people:
    print(f"Number: {people[name]}")

