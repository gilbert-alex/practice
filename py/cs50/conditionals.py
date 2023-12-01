''' Conditionals, boolean expressions,
relational operators
'''

# prompt user for integers
x = int(input("What's x? "))
y = int(input("What's y? "))

# compare integers with conditionals
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")

# logical operators
print()
s = input("Do you agree? ")

# check if you agree
if s == "Y" or s == "y":
    print("Agreed.")
elif s == "N" or s == "n":
    print("Not agreed.")

# a better approach using lists

if s in ["y", "Y", "Yes"]:
    print("Agreed.")
if s in ['n','N',"No"]:
    print("Not agreed.")

# a method using .lower - a method of the /
# string class(object)

s = s.lower()

if s in ['y','yes']:
    print("Agreed.")
if s in ["n","no"]:
    print("Not agreed.")

