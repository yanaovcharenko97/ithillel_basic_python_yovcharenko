def index(lst, elem):
    for idx, item in enumerate(lst):
        if lst[idx] == elem:
            return idx


def test():
    result = index([1, 2, 3, 4, 5], 3)
    print(result)
    assert result == 2

    result = index([1, 2, 3, 4, 5], 7)
    print(result)
    assert result is None


def main():
    lst = ["a", "b", 12, 46, [2, 7, 5], 456]
    elem = 12
    result = index(lst, elem)

    print(result)


if __name__ == "__main__":
    main()
