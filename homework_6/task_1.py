def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def test():
    result = is_even(0)
    print("Result:", result)
    assert result is True
    
    result = is_even(1)
    print("Result:", result)
    assert result is False
    
    result = is_even(2)
    print("Result:", result)
    assert result is True

    result = is_even(356981427)
    print("Result:", result)
    assert result is False
    
    result = is_even(2684222)
    print("Result:", result)
    assert result is True


def main():
    number = int(input("Please enter a number to find out if it is even or not: "))
    result = is_even(number)

    if result is True:
        print("\nYes, it is an even number")
    else:
        print("\nNo, it is not an even number. It is an odd number.")


if __name__ == "__main__":
    main()
