def get_max_digit(number):
    max_digit = 0
    while number > 0:
        digit = number % 10
        if digit > max_digit:
            max_digit = digit
        number //= 10

    return max_digit


def main():
    number = int(input("Please enter any 12 digit number: "))
    max_digit = get_max_digit(number)
    print(f"\nThe largest digit of {number} is {max_digit}")


if __name__ == "__main__":
    main()
