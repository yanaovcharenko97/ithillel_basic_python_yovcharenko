print("To find out if the chess knight can be on the desired square of the chessboard in one move, please enter:\n")

x1_letter, y1_number = input("the square from which the knight starts its move - ")
x2_letter, y2_number = input("the square where the knight should go - ")

letter_designations = "abcdefgh"

x1_numer = 0
for i in range(len(letter_designations)):
    if letter_designations[i] == x1_letter[0]:
        x1_numer = i

x2_numer = 0
for i in range(len(letter_designations)):
    if letter_designations[i] == x2_letter[0]:
        x2_numer = i

dx = abs(x1_numer - x2_numer)
dy = abs(int(y1_number) - int(y2_number))

if dy == 2 and dx == 1 or dx == 2 and dy == 1:
    print('\nYES. The knight can go to this square in one move.')
else:
    print('\nNO. The knight cannot go to this square in one move.')
