def chess_knight(start, end):
    x1_number = ord(start[0])
    y1_number = int(start[1])
    x2_number = ord(end[0])
    y2_number = int(end[1])

    dx = abs(x1_number - x2_number)
    dy = abs(y1_number - y2_number)

    return dx == 1 and dy == 2 or dx == 2 and dy == 1


def test():
    result = chess_knight("a1", "c2")
    print("Result", result)
    assert result is True

    result = chess_knight("b2", "b3")
    print("Result", result)
    assert result is False


def main():
    print("To find out if the chess knight can be on the desired square "
          "of the chessboard in one move, please enter:")

    start = input("the square from which the knight starts its move - ")
    end = input("the square where the knight should go - ")

    result = chess_knight(start, end)
    
    if result is True:
        print("\nYES. The knight can go to this square in one move.")
    else:
        print("\nNO. The knight cannot go to this square in one move.")


if __name__ == "__main__":
    main()
