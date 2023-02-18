def sum_symbol_codes(first, last):
    first = ord(first)
    last = ord(last)
    sum_codes = 0

    for i in range(first, last + 1):
        sum_codes += i
    return sum_codes


def test():
    result = sum_symbol_codes("a", "d")
    print("result:", result)
    assert result == 394

    result = sum_symbol_codes("a", "f")
    print("result:", result)
    assert result == 597


def main():
    print("Please enter first and last symbols to find sum of unicode codes between them "
          "(including first and last symbols)")
    
    first = input("\nFirst symbol: ")
    last = input("Last symbol: ")
    sum_codes = sum_symbol_codes(first, last)

    print(f"\nSum of unicode codes of all symbols between {first} and {last}: {sum_codes}")


if __name__ == "__main__":
    main()
