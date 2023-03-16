"""
This module implements a Godzilla class that can eat humans and keep track of its stomach capacity.
It also includes a function to get integer input and a main function that allows the user to
simulate feeding Godzilla with different humans.
"""


class Godzilla:
    """
    The Godzilla class represents a creature that can eat humans and
    keep track of its stomach capacity.    """
    def __init__(self, stomach_capacity):
        self.stomach_capacity = stomach_capacity
        self.stomach_content = 0

    def eat(self, human_size):
        """
        Try to eat a human of a given size.
        If the human is smaller than the remaining capacity of the stomach,
        it is eaten and the stomach content is increased by the human's size.
        Otherwise, the human is not eaten and a message is printed.
        """
        if self.stomach_content + human_size <= self.stomach_capacity:
            self.stomach_content += human_size
            print(f"~ Godzilla ate a human of size {human_size} ~")
            if self.stomach_content >= self.stomach_capacity * 0.9:
                print("~ Godzilla is getting full! ~")
        else:
            print("~ Godzilla can't eat anymore, the stomach is full! ~")


def test_godzilla():
    # Test eating a human smaller than stomach capacity
    godzilla = Godzilla(10)
    godzilla.eat(5)
    assert godzilla.stomach_content == 5

    # Test eating a human larger than stomach capacity
    godzilla.eat(10)
    assert godzilla.stomach_content == 5

    # Test eating a human that makes the stomach almost full
    godzilla.eat(4)
    assert godzilla.stomach_content == 9

    # Test eating a human that fills the stomach to capacity
    godzilla.eat(1)
    assert godzilla.stomach_content == 10

    # Test eating a human when the stomach is already full
    godzilla.eat(2)
    assert godzilla.stomach_content == 10

    # Test eating multiple humans
    godzilla = Godzilla(15)
    godzilla.eat(5)
    godzilla.eat(7)
    godzilla.eat(4)
    assert godzilla.stomach_content == 16

    print("All tests pass")


def get_int_input(prompt: str):
    """
    Get an integer from the user.

    This function takes a string prompt as an argument
    and repeatedly asks the user to input an integer
    until a valid integer is entered.
    """
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")


def main():
    """
    This function simulates feeding Godzilla with different humans. It first asks the user to enter the
    stomach capacity of Godzilla. Then, it repeatedly asks the user to enter the size of a human to feed
    Godzilla until the user enters 0 to finish. It calls the eat() method of the Godzilla object with the
    human size as the argument. If the stomach is almost full, it prints a warning message. Finally, it
    asks the user if they want to play again.
    """
    while True:
        stomach_capacity = get_int_input("Enter Godzilla's stomach capacity: ")
        godzilla = Godzilla(stomach_capacity)

        while True:
            human_size = get_int_input("\nEnter the size of a human to feed "
                                       "Godzilla (or enter 0 to finish): ")
            if human_size == 0:
                break
            godzilla.eat(human_size)

        play_again = input("\nDo you want to play again? (y/n) ")
        if play_again.lower() != 'y':
            break


if __name__ == '__main__':
    main()
