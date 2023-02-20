def change_numbers(start, end):
    list_number = []

    for i in range(start, end + 1):
        if i % 3 == 0 and i % 5 == 0:
            list_number.append("FizzBuzz")
        elif i % 3 == 0:
            list_number.append("Fizz")
        elif i % 5 == 0:
            list_number.append("Buzz")
        else:
            list_number.append(i)

    return "\n".join(map(str, list_number))


def main():
    start = int(input("Please enter start number: "))
    end = int(input("Please enter end number: "))
    result = change_numbers(start, end)

    print(result)


if __name__ == "__main__":
    main()
