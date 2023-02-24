def group_by_surname(list_of_enrollees):
    count_students = {"A-I": 0, "J-P": 0, "Q-T": 0, "U-Z": 0}

    for student in list_of_enrollees:
        surname = student.split()[-1]

        if 'A' <= surname[0] <= 'I':
            count_students["A-I"] += 1
        elif 'J' <= surname[0] <= 'P':
            count_students["J-P"] += 1
        elif 'Q' <= surname[0] <= 'T':
            count_students["Q-T"] += 1
        elif 'U' <= surname[0] <= 'Z':
            count_students["U-Z"] += 1

    return count_students["A-I"], count_students["J-P"], count_students["Q-T"], count_students["U-Z"]


def test():
    count_students = group_by_surname(['Will Smith', 'Emma Watson', 'George Clooney', 'Jay Z', 'David Beckham'])
    assert count_students == (2, 0, 1, 2)


def main():
    list_of_enrollees = ['Will Smith', 'Emma Watson', 'George Clooney', 'Jay Z', 'David Beckham']
    count_students = group_by_surname(list_of_enrollees)

    print(f"In the A-I group: {count_students[0]} enrollees\n"
          f"In the J-P group: {count_students[1]} enrollees\n"
          f"In the Q-T group: {count_students[2]} enrollees\n"
          f"In the U-Z group: {count_students[3]} enrollees\n")


if __name__ == "__main__":
    main()
