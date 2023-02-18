def kin(grain):
    letter_designations = "abcdefgh"
    count = 0
    for i in range(8):
        for j in range(8):
            number_grain = 2**count

            if number_grain >= grain:
                cell_name = letter_designations[i] + str(j+1)
                return cell_name
            else:
                grain -= number_grain

            count += 1


def main():
    print("To find out from which cell of the chessboard the Raja had to give the grain: ")
    kg_grain = float(input("enter the amount of grain in kilograms - "))
    grain = kg_grain / (3.5 * 10**-5)
    result = kin(grain)
    print(f"\nTo give {kg_grain} kg of grain, the Raja had to start from chessboard: {result}")


if __name__ == "__main__":
    main()
