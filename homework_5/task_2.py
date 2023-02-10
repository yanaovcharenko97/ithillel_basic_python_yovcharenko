def triangle_square_and_perimeter(a, b):
    sq = (a * b) / 2
    per = (a**2 + b**2)**0.5 + a + b
    return sq, per


print('Please enter the length of the legs the triangle')

c, d = int(input('Leg 1 - ')), int(input('Leg 2 - '))
res_1, res_2 = triangle_square_and_perimeter(c, d)

print('\nSquare =', res_1)
print('Perimeter =', res_2)
