def list_chain(*iterables):
    chain_list = []

    for item in iterables:
        chain_list.extend(item)

    return chain_list


def test():
    chain_list = list_chain([1, 2, 3], {'5': 5}, tuple(), (6, 7), range(8, 10))
    assert chain_list == [1, 2, 3, '5', 6, 7, 8, 9]


def main():
    chain_list = list_chain([1, 2, 3], {'5': 5}, tuple(), (6, 7), range(8, 10))
    
    print("Chain_list:", chain_list)


if __name__ == "__main__":
    main()
