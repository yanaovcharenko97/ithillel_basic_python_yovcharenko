from random import randint


def diff_min_max(num_limit, lower_bound, upper_bound):
    number_list = [randint(lower_bound, upper_bound) for _ in range(num_limit)]

    return max(number_list) - min(number_list)


def main():
    difference_between_maximum_minimum = diff_min_max(10, 1, 100)

    print("The difference between the maximum and minimum value:", difference_between_maximum_minimum)


if __name__ == "__main__":
    main()
    