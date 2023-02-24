def get_max_digit(number):
    max_digit = ""

    for i in str(number):
        if i > max_digit:
            max_digit = i

    return int(max_digit)


def main():
    number = input("Please enter any 12 digit number: ")
    max_digit = get_max_digit(number)

    print(f"\nThe largest digit of {number} is {max_digit}")


if __name__ == "__main__":
    main()
