'''
def solve(a):
    return a[-1]
a = {1, 2, 3, 4}
print(solve(a) ** 2)
'''
#error: cant subscript a set

# edited
def solve(a):
    return a[-1]
a = [1, 2, 3, 4] # works with a list
print(solve(a) ** 2)

b = (1, 2, 3, 4) # works with a tuple
print(solve(a) ** 2)