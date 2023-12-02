'''
example of command line arguements with /
with sys library
'''

from sys import argv
import sys

# prints a command line arguement
if len(argv) == 2:
    print(f"hello, {argv[1]}")
else:
    print("hello, world")

# print each part of argv
for i in range(len(argv)):
    print(f"{i + 1}: {argv[i]}")

for arg in argv[1:]:
    print(arg)

# exits with explict value, importing sys
if len(sys.argv) != 2:
    print("Missing command-line arguement")
    sys.exit(1)

print(f"hello, {sys.argv[1]}")
sys.exit(0)
