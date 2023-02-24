def copy_deep(obj):
    if type(obj) is dict:
        new_dict = dict(obj)
        return new_dict
    
    elif type(obj) is list:
        new_list = [copy_deep(i) for i in obj]
        return new_list

    elif type(obj) is tuple:
        new_tuple = (copy_deep(i) for i in obj)
        return tuple(new_tuple)

    else:
        return obj


def main():
    obj_1 = {'a': "a", "1": 1, "2": 2.0, 3: "b"}
    obj_2 = copy_deep(obj_1)
    obj_1[3] = "c"

    print(obj_1)
    print(obj_2)
    print(obj_1[3], obj_2[3])


if __name__ == "__main__":
    main()
