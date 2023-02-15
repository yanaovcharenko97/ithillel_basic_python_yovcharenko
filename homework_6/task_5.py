def leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False


def test():
    result = leap_year(1600)
    print(result)
    assert result is True
    
    result = leap_year(1900)
    print(result)
    assert result is False
    
    result = leap_year(2100)
    print(result)
    assert result is False


def main():
    year = int(input("Please enter a year to find out if it's a leap year or not: "))
    result = leap_year(year)

    if result is True:
        print("\nYES")
    else:
        print("\nNO")


if __name__ == "__main__":
    main()
