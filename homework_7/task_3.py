import math


def calculate_wheat_chess_position(kg_grain):
    grain = int(kg_grain / 0.000035)
    letter_designations = "abcdefgh"
    cell_index = int(math.log2(grain))
    cell_name = letter_designations[cell_index // 8] + str(cell_index % 8 + 1)

    return cell_name


def main():
    print("To find out from which cell of the chessboard the Raja had to give the grain: ")
    kg_grain = float(input("enter the amount of grain in kilograms - "))

    result = calculate_wheat_chess_position(kg_grain)

    print(f"\nTo give {kg_grain} kg of grain, the Raja had to start from chessboard: {result}")


if __name__ == "__main__":
    main()
    