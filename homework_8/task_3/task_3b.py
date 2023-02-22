def sorted_list_value_first_digit(original_list):
    return sorted(original_list, key=lambda item: int(str(item)[0]))


def main():
    original_list = [472, 326, 1, 999.0, '1101000', '99', 9, '20', 863, '0']
    sorted_copy_list = sorted_list_value_first_digit(original_list)
    print("Original list:", original_list)
    print("Sorted copy list:", sorted_copy_list)


if __name__ == "__main__":
    main()
