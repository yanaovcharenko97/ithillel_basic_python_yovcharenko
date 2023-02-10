def triangle_square_and_perimeter(a, b):
    square = (a * b) / 2
    perimeter = (a**2 + b**2)**0.5 + a + b
    return square, perimeter


print('Please enter the length of the legs the triangle')

leg_a, leg_b = int(input('Leg a - ')), int(input('Leg b - '))
result_square, result_perimeter = triangle_square_and_perimeter(leg_a, leg_b)

print('\nSquare =', result_square)
print('Perimeter =', result_perimeter)
