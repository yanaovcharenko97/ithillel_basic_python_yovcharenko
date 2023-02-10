from math import pi


def cone_square_and_volume(radius, height):
    length = (radius**2 + height**2)**0.5
    square = pi * radius * length + pi * radius**2
    volume = (1/3) * pi * height * radius**2
    return square, volume


print('Please enter radius and height of the cone')

a, b = int(input('Radius - ')), int(input('Height - '))
result_square, result_volume = cone_square_and_volume(a, b)

print('\nSquare =', result_square)
print('Volume =', result_volume)
