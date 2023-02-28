def copy_deep(obj, copied=None):
    if copied is None:
        copied = {}

    if id(obj) in copied:
        return copied[id(obj)]

    if type(obj) is dict:
        new_dict = {}
        copied[id(obj)] = new_dict
        for key, value in obj.items():
            new_dict[copy_deep(key)] = copy_deep(value, copied)
        return new_dict

    elif type(obj) is list:
        new_list = []
        copied[id(obj)] = new_list
        for i in obj:
            new_list.append(copy_deep(i, copied))
        return new_list

    elif type(obj) is tuple:
        new_tuple = tuple(copy_deep(i, copied) for i in obj)
        copied[id(obj)] = new_tuple
        return new_tuple

    else:
        return obj


def test_copy_deep():
    test_data = [1, 2, [4, 5, 6], {'A': 'B', 'c': [3658]}, 2.0, {'e': 0}]
    test_data[3]['d'] = test_data
    test_data[-1]['f'] = test_data[-1]
    copy = copy_deep(test_data)
    print(test_data)
    print(copy)
    print(copy[3]['c'] is not test_data[3]['c'])  # True
    print(copy[3]['d'] is not test_data[3]['d'])  # True
    print(copy[3]['d'] is copy)  # True
    print(copy[-1] is not test_data[-1])  # True
    print(copy[-1] is copy[-1]['f'])  # True


test_copy_deep()
