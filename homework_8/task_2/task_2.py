def copy_deep(obj):
    if type(obj) is list:
        new_list = []
        for item in obj:
            new_list.append(copy_deep(item))
        return new_list
        
    elif type(obj) is tuple:
        new_tuple = ()
        for item in obj:
            new_tuple += (copy_deep(item),)
        return new_tuple
        
    else:
        return obj


def main():
    lst1 = ['a', 1, 2.0, ['b']]
    lst2 = copy_deep(lst1)
    lst1[3].append(0)
    
    print(lst1[3], lst2[3])


if __name__ == "__main__":
    main()
