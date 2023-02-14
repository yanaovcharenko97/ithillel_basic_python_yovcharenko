def is_even(number):
    remainder = number % 2

    if remainder == 0:
        result = "Yes, it is an even number"
    else:
        result = "No, it is not an even number. It is an odd number."
    return result


def test():
    result = is_even(0)
    print("Result:", result)
    assert result == "Yes, it is an even number"
    
    result = is_even(1)
    print("Result:", result)
    assert result == "No, it is not an even number. It is an odd number."
    
    result = is_even(2)
    print("Result:", result)
    assert result == "Yes, it is an even number"
    
    result = is_even(356981427)
    print("Result:", result)
    assert result == "No, it is not an even number. It is an odd number."
    
    result = is_even(2684222)
    print("Result:", result)
    assert result == "Yes, it is an even number"


def main():
    number = int(input("Please enter a number to find out if it is even or not: "))
    result = is_even(number)

    print("\n" + result)


if __name__ == "__main__":
    main()
