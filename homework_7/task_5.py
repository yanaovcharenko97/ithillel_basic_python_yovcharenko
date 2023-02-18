import random


number = random.randrange(1, 11)
n = 0

while n != number:
    n = int(input("I picked a number from 1 to 10. Try to guess it!: "))
    
    if n > number:
        print("\nOops... \nMy number IS LESS than yours\n")
    elif n < number:
        print("\nOh no... \nMy number IS BIGGER than yours\n")
        
print(f"\nYippee! \nYou guessed it! \nMy number is {n}")
