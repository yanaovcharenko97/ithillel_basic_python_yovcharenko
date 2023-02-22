def get_max_digit(number):
    max_digit = 0
    for i in str(number):
        if int(i) > max_digit:
            max_digit = int(i)

    return max_digit


def main():
    number = int(input("Please enter any 12 digit number: "))
    max_digit = get_max_digit(number)
    print(f"\nThe largest digit of {number} is {max_digit}")


if __name__ == "__main__":
    main()
