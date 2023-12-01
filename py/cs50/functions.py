'''
Demonstrates the use of a function "main" to /
replace "int main()" of C.
This will also nicely place main first /
in the program.
Remember that main() must be called last.
'''

# bark 3 times with loops
i = 0
while i < 3:
    print("Woof")
    i += 1

for j in range(3):
    print("arf")

# abstracts action into a more readable 'main'
# double spaces between functions.
def main():
    bark(3)


# bark some number of times
def bark(n):
    for i in range(n):
        print('bark')


main()