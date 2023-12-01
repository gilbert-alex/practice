# examples of a while loop
# modules
import random

# fig 2-11
counter = 65
while counter < 91:
    # value in counter must be converted to a string for concat
    # use typce cast str for a literal and chr to convert to ASCII
    print(str(counter) + " = " + chr(counter))
    counter += 1
print('done')

# example of a while loop with continue statement
# fig 2-13
# prints 10 random odd integers
print()
print("Odd numbers")
counter = 0
while counter < 10:
    number = random.randint(1,999)
    if int(number / 2) == number / 2:
        # int(n / 2) will drop decimal from an odd int
        # result != n/2 (which will have a decimal)
        continue
    print(number)
    counter += 1
print("loop is done")

# example of a while loop with a break statement
# print an unknown number of integers not divisible by 5
print()
print('Numbers which are not evenely divisible by 5')
counter = 0
while counter < 5:
    number = random.randint(1,999)
    if int(number / 5) == number / 5:
        break
    print(number)
    counter += 1
print('counter is: ' + str(counter))
print('loop is done')