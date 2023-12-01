# creating a formula for use in code
"""
syntax:
def hello():
"""

def hello(x): # Practice function
    """ A docstring describing the function """
    print('hello ' + str(x))

x = 'alex'
number = 5

print('\nA function with arg input')
hello(x)
hello(number)

# function with optional arguements
def bye(user_name = 'nobody'):
    print('bye ' + str(user_name))

print('\nA function with optional args')
bye()
bye(x)
bye(number)

# passing multiple arguements to a function
def hello_multi(first_name, last_name, datestring): # Practice function
    ''' A docstring describing the function '''
    print('Hello ' + first_name + ' ' + last_name)
    print('The date is ' + datestring)

import datetime as dt
fname = 'Alex'
lname = 'Gilbert'
datestring = str(dt.date.today())
hello_multi('Alex', 'Gilbert', datestring)

# example of multi and optional args
# optional args must be entered last
def hello_mo (first_name, last_name, datestring = ''):
    msg = 'Hello ' + first_name + ' ' + last_name
    if len(datestring) > 0:
        msg += ' you mentioned ' + datestring
    print(msg)

print('\nA function with multi and optional args')
hello_mo(fname, lname, datestring)
hello_mo(fname, lname)

# using keyword arguements (kwargs) to pass values to a formula
print('\nA formula with values passed with kwargs')
appt_date = '12/30/2019'
last = 'smith'
first = 'john'
hello_mo (datestring = appt_date, first_name = first, last_name = last)

# passing list values to a formula
# functions to do recieve a mutable list; rather they get a pointer to the list
# if a function is to change a list it must first make a copy
original_list = [5, 2, 6, 8, 3, 4, 7]

def alphabetize(original_list = []):
    sorted_list = original_list.copy()
    sorted_list.sort()
    final_list = ''
    for item in sorted_list:
        final_list += str(item) + ", "
    final_list = final_list[:-2]
    print(final_list)
    return(final_list)

print('\nA formula with list values')
alphalist = alphabetize(original_list)
print(alphalist)

# creating a formula with an arbitrary number of args
# def sorter(*args)
# the items passed become a tuple in the function (immutable)

def sorter(*args):
    newlist = list(args)
    newlist.sort()
    print(newlist)

print('\nUsing a formula with variable arg count')
sorter(402, 503, 182, 827, 189)

# returning a value from a function

# anonymous (lambda) functions
