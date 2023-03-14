"""
This script is a phone book that allows adding, deleting, updating contacts,
and searching them by name, age, and email. It is possible to save the contact
list to a file or open an existing file with phone contacts.

Documentation for the code can be found in the file "Documentation for the Phonebook program.pdf"
"""


from copy import deepcopy
from json import load
from utilities.input import get_input_str_from_user, get_input_int_from_user
from utilities.decorator import print_start_end_process
from utilities.print import print_entry, print_error, print_prompt
from utilities.save_file import save_phonebook_to_new_file, \
    save_phonebook_to_actual_file, save_changes_for_phonebook
import argparse


parser = argparse.ArgumentParser(description="Phone book")
parser.add_argument("url", type=str, help="The path to the file")
parser.add_argument("-v", "--verbose", action="store_true",
                    help="Enable decorators")
args = parser.parse_args()
print_start_end_process_off = not args.verbose

running = True              # a flag variable indicating the state of the program
changes_made_to_phonebook = False     # a flag variable indicating whether changes have been made to the contact list
file_name = ""              # the name of the file with phone contacts
phone_book = []             # the list of contacts


@print_start_end_process(print_start_end_process_off)
def print_phonebook():
    print("\n\n#########  Phone book  ##########")

    for idx, entry in enumerate(phone_book, start=1):
        print_entry(idx, entry)


@print_start_end_process(print_start_end_process_off)
def add_new_entry_to_phonebook():
    global phone_book
    surname      = get_input_str_from_user(prompt="    Enter surname: ")
    name         = get_input_str_from_user(prompt="    Enter name: ")
    age          = get_input_int_from_user(prompt="    Enter age: ")
    phone_number = get_input_str_from_user(prompt="    Enter phone num.: ")
    email        = get_input_str_from_user(prompt="    Enter email: ")
    entry        = {"surname": surname, "name": name, "age": age,
                    "phone_number": phone_number, "email": email}
    phone_book.append(entry)
    global changes_made_to_phonebook
    changes_made_to_phonebook = True


@print_start_end_process(print_start_end_process_off)
def find_entry_by_name_in_phonebook():
    name = get_input_str_from_user(prompt="    Enter name: ")
    found = False

    for idx, entry in enumerate(phone_book, start=1):
        if entry["name"] == name:
            print_entry(idx, entry)
            found = True

    if not found:
        print_error("Contact not found")


@print_start_end_process(print_start_end_process_off)
def find_entry_by_age_in_phonebook():
    age = get_input_int_from_user(prompt="    Enter age: ")
    found = False

    for idx, entry in enumerate(phone_book, start=1):
        if entry["age"] == age:
            print_entry(idx, entry)
            found = True

    if not found:
        print_error("Contact not found")


@print_start_end_process(print_start_end_process_off)
def find_email_by_name_in_phonebook():
    name = get_input_str_from_user(prompt="    Enter name: ")
    found = False

    for idx, entry in enumerate(phone_book):
        if entry["name"] == name:
            print(f"\n{name}'s email:\n   ", entry["email"])
            found = True

    if not found:
        print_error("Contact not found")


@print_start_end_process(print_start_end_process_off)
def delete_entry_by_name_in_phonebook():
    name = get_input_str_from_user(prompt="    Enter name: ")
    copy_of_phone_book = deepcopy(phone_book)
    found = False

    for idx, entry in enumerate(copy_of_phone_book):
        if entry["name"] == name:
            phone_book.pop(idx)
            global changes_made_to_phonebook
            changes_made_to_phonebook = True
            found = True

    if not found:
        print_error("Contact not found")


@print_start_end_process(print_start_end_process_off)
def count_all_entries_in_phonebook():
    print("Total number of entries: ", len(phone_book))


@print_start_end_process(print_start_end_process_off)
def print_phonebook_by_age():
    print("\n\n#########  Phone book by age  ##########\n")

    phone_book_sorted_by_age = sorted(phone_book, key=lambda x: x["age"])

    for idx, entry in enumerate(phone_book_sorted_by_age):
        print_entry(idx + 1, entry)


@print_start_end_process(print_start_end_process_off)
def update_contact_ages():
    years_to_add = get_input_int_from_user(prompt="    Enter number of years: ")

    for idx, entry in enumerate(phone_book):
        phone_book[idx]["age"] += years_to_add

    global changes_made_to_phonebook
    changes_made_to_phonebook = True


@print_start_end_process(print_start_end_process_off)
def calculate_average_age_of_all_persons_in_phonebook():
    try:
        age_of_all_persons_in_phonebook = \
            [entry["age"] for entry in phone_book]
        average_age_of_all_persons = \
            sum(age_of_all_persons_in_phonebook) / len(age_of_all_persons_in_phonebook)

        print("Average age of all persons:\n"
              f"~ {average_age_of_all_persons:.2f} years ~")

    except ZeroDivisionError:
        print_error("Division by zero. The phone book is empty.")


@print_start_end_process(print_start_end_process_off)
def save_phonebook_to_file():
    if file_name is None:
        save_phonebook_to_new_file()
    else:
        response = get_input_str_from_user(
            prompt="Save the data to the actual file or "
                   "create a new one? (actual/new): ",
            options=["actual", "new"])

        if response.lower() == "actual":
            save_phonebook_to_actual_file()
        elif response.lower() == "new":
            save_phonebook_to_new_file()


def open_file(name):
    global file_name
    global phone_book

    try:
        with open(name, "r") as f:
            phone_book = load(f)

    except FileNotFoundError:
        print_error("File not found")
    file_name = name


@print_start_end_process(print_start_end_process_off)
def load_from_file():
    global file_name
    global phone_book
    global changes_made_to_phonebook

    if changes_made_to_phonebook:
        save_changes_for_phonebook()

    file_name = get_input_str_from_user(prompt="Enter the name of the "
                                               "file to be opened:\n")
    phone_book = []
    changes_made_to_phonebook = False

    try:
        with open(file_name, "r") as f:
            phone_book = load(f)
        changes_made_to_phonebook = False

    except FileNotFoundError:
        print_error("File not found")


@print_start_end_process(print_start_end_process_off)
def exit_file():
    global running
    global changes_made_to_phonebook

    if changes_made_to_phonebook:
        save_changes_for_phonebook()

    running = False


def main():
    open_file(args.url)
    while running:

        try:
            menu = {
                "1": print_phonebook,
                "2": print_phonebook_by_age,
                "3": add_new_entry_to_phonebook,
                "4": find_entry_by_name_in_phonebook,
                "5": find_entry_by_age_in_phonebook,
                "6": delete_entry_by_name_in_phonebook,
                "7": count_all_entries_in_phonebook,
                "8": calculate_average_age_of_all_persons_in_phonebook,
                "9": update_contact_ages,
                "e": find_email_by_name_in_phonebook,

                "0": exit,
                "s": save_phonebook_to_file,
                "l": load_from_file,
            }

            print_prompt()
            user_input = get_input_str_from_user(prompt="phonebook> ")
            menu[user_input]()

        except KeyError:
            print_error("Please enter a valid option from the menu.")


if __name__ == "__main__":
    main()
