from random import randint


def diff_min_max(num_limit, lower_bound, upper_bound):
    number_list = [randint(lower_bound, upper_bound) for _ in range(num_limit)]
    my_max = number_list[0]
    my_min = number_list[0]

    for i in range(num_limit):
        if i > my_max:
            my_max = i
        if i < my_min:
            my_min = i

    return my_max - my_min


def main():
    difference_between_maximum_minimum = diff_min_max(10, 1, 100)

    print("The difference between the maximum and minimum value:", difference_between_maximum_minimum)


if __name__ == "__main__":
    main()
