def copy_deep(obj):
    if type(obj) is list:
        new_list = [copy_deep(i) for i in obj]
        return new_list

    elif type(obj) is tuple:
        new_tuple = (copy_deep(i) for i in obj)
        return tuple(new_tuple)

    else:
        return obj


def main():
    lst1 = ('a', 1, 2.0, ['b'])
    lst2 = copy_deep(lst1)
    lst1[3].append(0)

    print(lst1[3], lst2[3])


if __name__ == "__main__":
    main()
