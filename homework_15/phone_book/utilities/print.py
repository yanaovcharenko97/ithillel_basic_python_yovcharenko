"""
The following functions are part of a phonebook program:

print_entry(number, entry):
This function takes in an integer number and a dictionary entry containing
information about a person. It prints the person's information formatted in a
table with five columns (surname, name, age, phone number, email). The number
parameter is used to label the entry in the printed output.

print_error(message):
This function takes in a string message and prints an error message with the
message parameter.

print_info(message):
This function takes in a string message and prints an informational message
with the message parameter.

print_prompt():
This function prints a welcome message and a list of actions that can be
performed with the phonebook program. These actions include printing entries,
adding new entries, finding entries, deleting entries, and more. The user can
select an action by typing a corresponding number or letter.
Additionally, the user can save the phonebook to a file, load the phonebook
from a file, or exit the program.
"""


def print_entry(number, contact):
    print("\n--[ %s ]--------------------------" % number)
    print("| Surname: %20s |" % contact.surname)
    print("| Name:    %20s |" % contact.name)
    print("| Age:     %20s |" % contact.age)
    print("| Phone:   %20s |" % contact.phone_number)
    print("| Email:   %20s |" % contact.email)


def print_error(message):
    print("ERROR: %s" % message)
    
    
def print_info(message):
    print("INFO: %s" % message)
    
    
def print_prompt():
    print("\n\n\n~ Welcome to phonebook ~")
    print("Select one of actions below:")
    print("     1 - Print phonebook entries")
    print("     2 - Print phonebook entries (by age)")
    print("     3 - Add new entry")
    print("     4 - Find entry by name")
    print("     5 - Find entry by age")
    print("     6 - Delete entry by name")
    print("     7 - The number of entries in the phonebook")
    print("     8 - Avr. age of all persons")
    print("     9 - Increase age by num. of years")
    print("     e - Find email by name")
    print("-----------------------------")
    print("     s - Save to file")
    print("     l - Load from file")
    print("     0 - Exit\n")
