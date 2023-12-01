# duplicate of mario w/ a try statement
# to control input and exception report

# immitates a 'do while' loop in C

def main():
    # print a vertical line of height
    height = get_height()
    for i in range(height):
        print("#")

    # print a horizontal line of width
    width = height
    for j in range(width):
        print("?", end = '')
    print()
    
    # simplified syntax
    print("$" * width)


def get_height():
    while True:
        try:
            n = int(input("Height: "))
            if n > 0:
                return n
        except ValueError:
            print("Not an integer")


main()