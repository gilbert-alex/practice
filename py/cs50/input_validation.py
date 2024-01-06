def main():
    number = get_number()
    bark(number)


def get_number():
    while True:
        n = int(input("Bark how many times? "))
        if n >= 0:
            return n


def bark(n):
    for _ in range(n):
        print("bark")


main()