# items in a set do not have index numbers (no specific order)
# initialized with {}
# items within a set cannot be changed
# sets cannot be reordered or sorted


sample_set = {1.98, 98.9, 74.95, 2.5, 1, 16.3}
print(sample_set)

print("\nLength of set")
print(len(sample_set))

print("\nCheck for items in a set")
print(2.5 in sample_set)
print(50 in sample_set)

print("\nAdd a single item to set")
item_add = 11.23
print(item_add)
sample_set.add(item_add)
# a set never contains more than one instance of a value
sample_set.add(item_add)
print(sample_set)

print("\nAdd multiple items")
# added items should be defined as a list[]
sample_set.update([88, 123.45, 2.98])
print(sample_set)

print("\nCopies of sets may be be in the same order")
ss2 = sample_set.copy()
print(ss2)

print("\nLoop to print f-string")
for x in sample_set:
    print(f"{x:>6.2f}")