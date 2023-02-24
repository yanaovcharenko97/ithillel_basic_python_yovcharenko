from random import randint


def diff_odd_even(num_limit, lower_bound, upper_bound):
    number_list = [randint(lower_bound, upper_bound) for _ in range(num_limit)]
    even_numbers = []
    odd_numbers = []

    for i in number_list:
        if i % 2 == 0:
            even_numbers.append(i)
        if i % 2 != 0:
            odd_numbers.append(i)

    return sum(even_numbers) - sum(odd_numbers)


def main():
    difference_between_maximum_minimum = diff_odd_even(10, 1, 100)

    print("The difference between the sum of all even numbers and the sum of all odd numbers:",
          difference_between_maximum_minimum)


if __name__ == "__main__":
    main()
