"""
This module defines a Circle class with a nested Point class. The Circle class
represents a circle with a center point and a radius. The Point class represents
a point in a two-dimensional plane with x and y coordinates.

Classes:
Circle: A class representing a circle with a center point and a radius.
Point: A class representing a point in a two-dimensional plane with x and y coordinates.

Functions:
test_circle() -> None: A function to test the Circle class's is_inside method.
get_float_input(prompt: str) -> float: A function to prompt the user for a float input.
main() -> None: A function to prompt the user for input to create a Circle object and
a Point object and determine whether the point is inside the circle.

Usage:
To test the Circle class, call the test function.
To use the Circle class to determine whether a point is inside a circle, call the main function.

Example:

Create a Circle object
c = Circle(Point(0, 0), 5)

Create a Point object
p = Point(3, 4)

Check if the point is inside the circle
result = c.is_inside(p)

Print the result
print(result) # Output: True
"""

from math import sqrt


class Circle:
    class Point:
        def __init__(self, x: float, y: float) -> None:
            self.x = x
            self.y = y

    def __init__(self, center: Point, radius: float) -> None:
        self.center = center
        self.radius = radius

    def is_inside(self, point: Point) -> bool:
        distance = sqrt((point.x - self.center.x) ** 2 + (point.y - self.center.y) ** 2)
        return distance < self.radius


def test_circle():
    p = Circle.Point(1, 1)
    c = Circle(Circle.Point(1, 1), 1)
    result = c.is_inside(p)
    print(result)
    assert result is True

    p = Circle.Point(2, 2)
    c = Circle(Circle.Point(1, 1), 1)
    result = c.is_inside(p)
    print(result)
    assert result is False


def get_float_input(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    x = get_float_input("Enter x-coordinate of point: ")
    y = get_float_input("Enter y-coordinate of point: ")
    p = Circle.Point(x, y)
    x_center = get_float_input("\nEnter x-coordinate of circle center: ")
    y_center = get_float_input("Enter y-coordinate of circle center: ")
    radius = get_float_input("Enter circle radius: ")
    c = Circle(Circle.Point(x_center, y_center), radius)
    result = c.is_inside(p)

    if result is True:
        print("\nThis point is inside the circle")
    else:
        print("\nThis point is not inside the circle")


if __name__ == '__main__':
    main()
