def leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        result = "YES"
    else:
        result = "NO"
    return result


def test():
    result = leap_year(1600)
    print(result)
    assert result == "YES"
    
    result = leap_year(1900)
    print(result)
    assert result == "NO"
    
    result = leap_year(2100)
    print(result)
    assert result == "NO"


def main():
    year = int(input("Please enter a year to find out if it's a leap year or not: "))
    result = leap_year(year)

    print("\n" + result)


if __name__ == "__main__":
    main()
