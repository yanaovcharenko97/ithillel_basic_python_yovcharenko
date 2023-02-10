from math import pi, cos


def degrees2radians(degrees):
    radians = degrees * pi / 180
    return radians


result_1 = cos(degrees2radians(60))
result_2 = cos(degrees2radians(45))
result_3 = cos(degrees2radians(40))

print('cos 60°:', result_1)
print('cos 45°:', result_2)
print('cos 40°:', result_3)
