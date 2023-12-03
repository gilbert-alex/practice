# examples of a for loop with a range of ints
for x in range(1, 10):
    print(x, end = ',')
print("\nAll done")

for x in range(1, 11):
    print(x, end = ',')
print("\nAll done")

# example of a for loop with a list
print()
for x in ['The', 'rain', 'in', 'Spain']:
    print(x)
print("Done")

# example of a for loop with a break condition
print()
answers = ['A', 'C', '', 'D']
for answer in answers:
    if answer == '':
        print('Incomplete')
        break
    print(answer)
print('loop is done')

# example of a for loop with a continue condition
print()
answers = ['A', 'C', '', 'D']
for answer in answers:
    if answer == '':
        print('Incomplete')
        continue
    print(answer)
print('loop is done')

# example of a nexted for loop
# outer loop
for outer in ['first', 'second', 'third']:
    print(outer)
    # inner loop
    for inner in range(3):
        print(inner + 1)

print('Both of loops are done')