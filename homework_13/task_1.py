class Godzilla:
    def __init__(self, stomach_capacity):
        self.stomach_capacity = stomach_capacity
        self.stomach_content = 0

    def eat(self, human_size):
        if self.stomach_content + human_size <= self.stomach_capacity:
            self.stomach_content += human_size
            print(f"~ Godzilla ate a human of size, {human_size} ~")
            if self.stomach_content >= self.stomach_capacity * 0.9:
                print("~ Godzilla is getting full! ~")
        else:
            print("~ Godzilla can't eat anymore, the stomach is full! ~")


def main():
    stomach_capacity = int(input("Enter Godzilla's stomach capacity: "))
    godzilla = Godzilla(stomach_capacity)

    while True:
        human_size = int(input("\nEnter the size of a human to feed Godzilla (or enter 0 to finish): "))
        if human_size == 0:
            break
        godzilla.eat(human_size)


if __name__ == '__main__':
    main()

