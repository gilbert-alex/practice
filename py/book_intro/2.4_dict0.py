# single key dictionary
# examples of syntax, functions, and methods

people = {
    'htankaka': 'Haru Tanaka',
    'ppatel': 'Priya Patel',
    'bagarcia': 'Benjamin Alberto Garcia',
    'zmin': 'Zhang Min',
    'afarooqu': 'Ayesha Farooqu',
    'hajackson': 'Hanna Jackson',
    'papetel': 'Pratyush Aarav Patel',
    'hrjackson': 'Henry Jackson'
}

# show value by calling key
print(people['zmin'])

# show value by calling key in variable
person = 'hrjackson'
print(people[person])

# length of dictionary
print('\nLength of dictionary')
howmany = len(people)
print(howmany)

# check if item is in dictionary (T/F)
print('\nCheck if item is in dictionary')
print('hrjackson' in people)
print('schmeedledorp' in people)

# .get
# if key value is not in dict .get returns 'none'
# improvement over calling by key value which would crash
print('\nReturn data with .get')
person = 'bagarcia'
print(people.get(person))
person = 'schmeedledorp'
print(people.get(person))
# can change the default return value of 'none'
print(people.get(person,'Key not here'))

# change the value of a dict item
print('\nChange value of an item')
print(people['hrjackson'])
people['hrjackson'] = 'Hanna Jackson-Smith'
print(people['hrjackson'])

# add or change an item with .update
# if key does not exist a new item will be added
# if key does exist the value will be updated
print('\nAdd/Update item')
people.update({'hrjackson': 'Henrietta Jackson'})
people.update({'wwiggins': 'Wanda Wiggins'})
# print people with for loop
for person in people.keys():
    print(person + ' = ' + people[person])

# print keys of a dictionary
print('\nPrinting items from a dictionary:')
print('Keys')
for person in people:
    print(person)

# print values of a dictionary
print('\nValues: Option 1')
for person in people:
    print(people[person])

print('\nValues: Option 2')
for person in people.values():
    print(person)

print('\nFor loop with .items method')
for key, value in people.items():
    print(key, ' = ', value)

# copy a dictionary
print('\nCopying a dictionary')

numbers = {
    100: 1000,
    200: 2000,
    300: 3000,
}
numbers2 = numbers.copy()
print(numbers2)

# deleting a dictionary item
print('\nDeleting a dictionary item')
print(numbers2)
del numbers2[200]
print(numbers2)
# delete without specifying a key will delete the entire list
# including the existence of the list
"""
del numbers2
print(numbers2)
"""

# clear a list
print('\nClear a list')
print(numbers2)
numbers2.clear()
print(numbers2)

# .pop method
# can store a value (but not key) in a variable
print(people)
adios = people.pop('zmin')
print(adios)
print(people)

# .popitem method
# returns key value pair of removed item
# always removes the last item
print('\n.popitem method')
print(people)
adios = people.popitem()
print(adios)
print(people)