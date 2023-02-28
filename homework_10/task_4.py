from random import randint


def get_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.\n")
        else:
            return value


def get_str(prompt, valid_options):
    while True:
        value = input(prompt).lower()
        if value in valid_options:
            return value
        print("Please enter a valid option.\n")


def guess_number():
    number = randint(1, 100)
    while True:
        guess = get_integer("\nI picked a number from 1 to 100. Try to guess it: ")
        if guess > number:
            print("Oops... My number is less than yours.")
        elif guess < number:
            print("Oh no... My number is bigger than yours.")
        else:
            print(f"\nYippee! You guessed! My number is {number}!")
            return


def computer_guess():
    number = get_integer("\nEnter a number between 1 and 100 for me to guess: ")
    lower_bound = 1
    upper_bound = 100
    guess = (lower_bound + upper_bound) // 2
    while True:
        print(f"\nMy number is {guess}")
        feedback = get_str("Is my number correct, less, or bigger? Enter C, L, or B: ", ["c", "l", "b"])
        if feedback == "c":
            print(f"\nYippee! I guessed! Your number is {number}!")
            return
        elif feedback == "l":
            lower_bound = guess + 1
        else:
            upper_bound = guess - 1
        guess = (lower_bound + upper_bound) // 2


def main():
    while True:
        print("Choose a game:")
        game = get_str("Enter 'G' to guess my number, or 'C' to have the computer guess your number: ", ["g", "c"])
        if game == "g":
            guess_number()
        else:
            computer_guess()
        repeat = get_str("\nDo you want to play again? Enter YES or NO: ", ["yes", "no"])
        if repeat == "no":
            break
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
