def index(lst, elem):
    for i in range(len(lst)):
        if lst[i] == elem:
            return i


def test():
    result = index([1, 2, 3, 4, 5], 3)
    assert result == 2

    result = index([1, 2, 3, 4, 5], 7)
    assert result is None


def main():
    lst = ["a", "b", 12, 46, [2, 7, 5], 456]
    elem = 12
    result = index(lst, elem)
    print(result)


if __name__ == "__main__":
    main()
