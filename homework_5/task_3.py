from math import pi


def cone_square_and_volume(radius, height):
    length = (radius**2 + height**2)**0.5
    sq = pi * radius * length + pi * radius**2
    vol = (1/3) * pi * height * radius**2
    return sq, vol


print('Please enter radius and height of the cone')

a, b = int(input('Radius - ')), int(input('Height - '))
res_1, res_2 = cone_square_and_volume(a, b)

print('Square =', res_1)
print('Volume =', res_2)
