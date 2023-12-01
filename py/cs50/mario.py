# print a vertical row of variable height

def main():
    height = get_height()
    for i in range(height):
        print("#")


# will crash if non-int input
    # see try.py
def get_height():
    while True:
        n = int(input("Height: "))
        if n > 0:
            return n


main()