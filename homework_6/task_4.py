def circles_intersect(x1, y1, r1, x2, y2, r2):
    d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

    if d == 0 and r1 == r2:
        result = "Circles coincide"
    elif d > r1 + r2:
        result = "Circles do not intersect"
    elif d < abs(r2 - r1):
        result = "Circles do not intersect. One of the circles is contained within the other"
    else:
        result = "Circles intersect at two points"
    return result


def test():
    result = circles_intersect(1, 1, 3, 1, 1, 3)
    print("Result:", result)
    assert result == "Circles coincide"

    result = circles_intersect(1, 7, 2, 2, 4, 1)
    print("Result:", result)
    assert result == "Circles do not intersect"

    result = circles_intersect(1, 7, 2, 2, 4, 31)
    print("Result:", result)
    assert result == "Circles do not intersect. One of the circles is contained within the other"

    result = circles_intersect(1, 1, 3, 5, 5, 4)
    print("Result:", result)
    assert result == "Circles intersect at two points"


def main():
    print("Please enter the coordinates of the center of the circles and their radii")
    print("Circle 1:")
    x1 = float(input("x1 = "))
    y1 = float(input("y1 = "))
    r1 = float(input("r1 = "))
    print("Circle 2:")
    x2 = float(input("x2 = "))
    y2 = float(input("y2 = "))
    r2 = float(input("r2 = "))

    result = circles_intersect(x1, y1, r1, x2, y2, r2)

    print("\n" + result)


if __name__ == "__main__":
    main()
