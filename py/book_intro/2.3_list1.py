# counting how many times an item is in list
print('\nCounting instances in a list')
grades = ['C', 'B', 'A', 'D', 'C', 'B', 'C']
b_grades = grades.count('B')
look_for = 'C'
c_grades = grades.count(look_for)
print(grades)
print('There are ' + str(b_grades) + ' B grades in the list.')
print('There are ' + str(c_grades) + ' ' + (look_for) + ' grades in the list')
print('There are ' + str(grades.count('F')) + ' F grades in the list')

# finding the index of a list's item
print('\nIndex of a list item')
print(grades)
look_for = 'A'
print(str(look_for) + ' is at index ' + str(grades.index('A')))

# if statement to handle error if item isnt in list
look_for = 'F'
if look_for in grades:
    print(str(look_for) + ' is at index ' + str(grades.index(look_for)))
else:
    print(str(look_for) + " isn't in the list.")


# create example to return index of all instances in list

# alphabetizing and sorting lists
names = ["Zara", "Lupe", "Hong", "Alberto", "Take", "Tyler"]
names1 = ["zara", "Lupe", "hong", "Alberto", "Take", "tyler"]
numbers = [14, 0, 56, -4, 99, 56, 11.23]

print("\nSort names alphabetically")
print(names)
names.sort()
print(names)

print("\nHandle upper and lower characters in sort")
print(names1)
names1.sort(key=lambda s: s.lower())
print(names1)


print("\nSort numbers ascending and decending")
print(numbers)
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

print("\nSorting datetime")
import datetime as dt

datelist = []
datelist.append(dt.date(2020,12,31))
datelist.append(dt.date(2019,1,31))
datelist.append(dt.date(2018,2,28))
datelist.append(dt.date(2020,1,1))

datelist.sort(reverse=True)
for date in datelist:
    print(f'{date:%m/%d/%Y}')


# copy and reverse
print("\nCopy and Reverse a list")
print(names)
backward_names = names.copy()
backward_names.reverse()
print(backward_names)