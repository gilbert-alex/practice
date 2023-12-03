# examples for working with lists
# initialized with []

# lists
students = ['Mark', 'Amber', 'Todd', 'Anita', 'Sandy']
scores = [1, 2, 3, 4, 5, 6]

# access a list item with index
print('Access items with an index')
print(students[2])

# loop through a list
print('\nPrinting list items with a loop')
for student in students:
    print(student)
print()
for score in scores:
    print(score, end = ',')

# check for an item in a list (returns True/False)
print('\nCheck list for item')
has_anita = 'Anita' in students
print(has_anita)

has_bob = 'Bob' in students
print(has_bob)

# getting the length of a list
print('\nLength of a list')
print(len(students))
print(len(scores))

# append item to list with string literal & variable
print('\nAppend new list items')
students.append('Goober')
new_student = 'Amanda'
students.append(new_student)
print(students)

# insert item to list at an index
print('\nInsert new list items')
students.insert(0, 'John')
print(students)
scores.insert(2,9)
print(scores)

# change an item in a list
print('\nChange a list item')
students[3] = 'Sarah'
print(students)
scores[6] = 15
print(scores)

# combining lists
print('\nCombine lists')
list1 = ['Zara', 'Lupe']
list2 = ['Huey', 'Dewey']
list1.extend(list2)
print(list1)

# removing list items
print('\nRemoving list items')
letters = ['A', 'B', 'C', 'D', 'C', 'E', 'C']
letters.remove('C')
# only removes the first occurance
print(letters)

while 'C' in letters:
    letters.remove('C')
    # loop to remove all 'C' itmes
print(letters)

# removing item by index with .pop
letter_removed = letters.pop(1)
print('Removed: ' + letter_removed)
print(letters)

# .pop method defaults to last index in list
letter_removed = letters.pop()
print('Removed: ' + letter_removed)
print(letters)

# example with a list of integers
number_removed = scores.pop()
print('Removed: ' + str(number_removed))
print(scores)

# del[] (delete) to remove letters
# does not return a value
# del without an index will delete entire list
del letters[0]
print(letters)
"""
del letters
print(letters)
"""

# clear a list to remove items but not list
letters.clear()
print(letters)

