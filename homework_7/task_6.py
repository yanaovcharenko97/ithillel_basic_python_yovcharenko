def fibonacci(n):
    fibonacci_1 = 1
    fibonacci_2 = 1

    i = 0
    while i < n - 2:
        fibonacci_sum = fibonacci_1 + fibonacci_2
        fibonacci_1 = fibonacci_2
        fibonacci_2 = fibonacci_sum
        i += 1

    return fibonacci_2


def test():
    result = fibonacci(1)
    print("Fibonacci =", result)
    assert result == 1

    result = fibonacci(2)
    print("Fibonacci =", result)
    assert result == 1

    result = fibonacci(7)
    print("Fibonacci =", result)
    assert result == 13

    result = fibonacci(10)
    print("Fibonacci =", result)
    assert result == 55


def main():
    n = int(input("Please enter a number to find out which number "
                  "from the fibonacci sequence corresponds to this position: "))
    result = fibonacci(n)

    print(f"\nFibonacci number corresponding to position {n}:", result)


if __name__ == "__main__":
    main()
    