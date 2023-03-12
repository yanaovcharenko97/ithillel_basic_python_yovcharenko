from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def is_inside(self, point):
        distance = sqrt((point.x - self.center.x) ** 2 + (point.y - self.center.y) ** 2)
        return distance < self.radius


def test():
    p = Point(1, 1)
    c = Circle(Point(1, 1), 1)
    result = c.is_inside(p)
    print(result)
    assert result is True

    p = Point(2, 2)
    c = Circle(Point(1, 1), 1)
    result = c.is_inside(p)
    print(result)
    assert result is False


def main():
    x = float(input("Enter x-coordinate of point: "))
    y = float(input("Enter y-coordinate of point: "))
    p = Point(x, y)
    x_center = float(input("\nEnter x-coordinate of circle center: "))
    y_center = float(input("Enter y-coordinate of circle center: "))
    radius = float(input("Enter circle radius: "))
    c = Circle(Point(x_center, y_center), radius)
    result = c.is_inside(p)

    if result is True:
        print("\nThis point is inside the circle")
    else:
        print("\nThis point is not inside the circle")


if __name__ == '__main__':
    main()
    