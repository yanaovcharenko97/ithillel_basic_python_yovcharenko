import cmath


def solve_quadratic_equation(a, b, c):
    d = b**2 - 4*a*c

    if d == 0:
        x1 = -b / (2*a)
        x2 = None
    elif d < 0:
        x1 = (-b - cmath.sqrt(d)) / (2 * a)
        x2 = (-b + cmath.sqrt(d)) / (2 * a)
    else:
        x1 = (-b - d ** 0.5) / (2 * a)
        x2 = (-b + d ** 0.5) / (2 * a)

    return x1, x2


def test():
    x1, x2 = solve_quadratic_equation(1, 2, -3)
    print("x1 =", x1)
    assert x1 == -3
    print("x2 =", x2)
    assert x2 == 1
    
    x1, x2 = solve_quadratic_equation(-4, 28, -49)
    print("x1 =", x1)
    assert x1 == 3.5
    print("x2 =", x2)
    assert x2 is None
    
    x1, x2 = solve_quadratic_equation(1, 2, 5)
    print("x1 =", x1)
    assert x1 == -1-2j
    print("x2 =", x2)
    assert x2 == -1+2j


def main():
    print("Enter the coefficients for the equation\nax^2 + bx + c = 0:")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    x1, x2 = solve_quadratic_equation(a, b, c)

    if x2 is None:
        print("\nx =", x1)
    else:
        print(f"\nx1 = {x1}\nx2 = {x2}")


if __name__ == "__main__":
    main()
