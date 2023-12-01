# examples working with tuples
# immutible
# initialized with ()

prices = (29.95, 9.98, 4.95, 79.98, 2.95)
print(prices)
lookfor = 4.95
print("lookfor: " + str(lookfor))

print("\nLength of tuple")
print(str(len(prices)) + " items in prices")

print("\nCount of item")
print(str(lookfor) + " is in prices " + str(prices.count(4.95)) + " times")

print("\nCheck if included (T/F)")
print(lookfor in prices)

print("\nIndex of item")
if lookfor in prices:
    print("Index: " + str(prices.index(lookfor)))
else:
    print("Item not found")

print("\nLoop to print f-string")
for price in prices:
    print(f"${price:.2f}")

"""
values in a tuple cannot be changed in any way.
assignment operators cannot be used
list methods .append, .clear, .copy, .extend, .insert, .pop, .remove,
.reverse, and .sort cannot be used
"""