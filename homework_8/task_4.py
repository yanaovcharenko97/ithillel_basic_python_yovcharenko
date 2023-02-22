def prime_numbers(start, end):
    list_prime_numbers = []
    for number in range(start, end + 1):
        if number == 1:
            continue
        is_prime = True
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            list_prime_numbers.append(number)

    return list_prime_numbers


def main():
    result = prime_numbers(1, 100)
    print(result)


if __name__ == "__main__":
    main()