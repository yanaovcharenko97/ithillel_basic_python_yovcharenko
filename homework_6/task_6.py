def sign_x(x):
    if x > 0:
        sign = 1
    elif x < 0:
        sign = -1
    else:
        sign = 0
    return sign


def test():
    result = sign_x(-365)
    print("Sign =", result)
    assert result == -1
    
    result = sign_x(421)
    print("Sign =", result)
    assert result == 1
    
    result = sign_x(0)
    print("Sign =", result)
    assert result == 0


def main():
    x = float(input("Please enter a number to find out to find out its sign: "))
    result = sign_x(x)

    print(f"\nSign({x}) =", result)


if __name__ == "__main__":
    main()
