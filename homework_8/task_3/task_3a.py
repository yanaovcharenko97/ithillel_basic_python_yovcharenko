def sorted_list_number_value(original_list):
    return sorted(original_list, key=float)


def main():
    original_list = [5, '9', 0, '452', 6.5, '6', 1, 2]
    sorted_copy_list = sorted_list_number_value(original_list)
    
    print("Original list:", original_list)
    print("Sorted copy list:", sorted_copy_list)


if __name__ == "__main__":
    main()
