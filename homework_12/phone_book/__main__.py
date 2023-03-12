from copy import deepcopy
from json import load
from utilities.input import get_input_str
from utilities.decorator import decorator
from utilities.print import print_entry, print_error, print_prompt
from utilities.save_file import save_new_file, save_actual_file, save_changes
import argparse


parser = argparse.ArgumentParser(description="Phone book")
parser.add_argument("url", type=str, help="The path to the file")
parser.add_argument("-v", "--verbose", action="store_true", help="Enable decorators")
args = parser.parse_args()
decorator_off = args.verbose

running = True
unsaved_changes = False
file_name = ""
phone_book = []


@decorator(decorator_off)
def print_phonebook():
    print()
    print()
    print("#########  Phone book  ##########")
    print()

    number = 1
    for entry in phone_book:
        print_entry(number, entry)
        number += 1


@decorator(decorator_off)
def add_entry_phonebook():
    global phone_book
    surname = get_input_str(prompt="    Enter surname: ")
    name = get_input_str(prompt="    Enter name: ")
    age = int(input("    Enter age: "))
    phone_number = get_input_str(prompt="    Enter phone num.: ")
    email = get_input_str(prompt="    Enter email: ")
    entry = {"surname": surname, "name": name, "age": age, "phone_number": phone_number, "email": email}
    phone_book.append(entry)
    global unsaved_changes
    unsaved_changes = True


@decorator(decorator_off)
def find_entry_name_phonebook():
    name = get_input_str(prompt="    Enter name: ")
    idx = 1
    found = False

    for entry in phone_book:

        if entry["name"] == name:
            print_entry(idx, entry)
            idx += 1
            found = True

    if not found:
        print_error("Not found!!")


@decorator(decorator_off)
def find_entry_age_phonebook():
    age = int(get_input_str(prompt="    Enter age: ", allow_digits=True))
    idx = 1
    found = False

    for entry in phone_book:

        if entry["age"] == age:
            print_entry(idx, entry)
            idx += 1
            found = True

    if not found:
        print_error("Not found!!")


@decorator(decorator_off)
def find_email_by_name():
    name = get_input_str(prompt="    Enter name: ")
    found = False

    for entry in phone_book:

        if entry["name"] == name:
            print(f"\n{name}'s email:\n   ", entry["email"])
            found = True

    if not found:
        print_error("Not found!!")


@decorator(decorator_off)
def delete_entry_name_phonebook():
    name = get_input_str(prompt="    Enter name: ")
    copy_name_phonebook = deepcopy(phone_book)
    found = False

    for entry in copy_name_phonebook:

        if entry["name"] == name:
            phone_book.pop(copy_name_phonebook.index(entry))
            global unsaved_changes
            unsaved_changes = True

    if not found:
        print_error("Not found!!")


@decorator(decorator_off)
def count_all_entries_in_phonebook():
    print("Total number of entries: ", len(phone_book))


@decorator(decorator_off)
def print_phonebook_by_age():
    print()
    print()
    print("#########  Phone book by age  ##########")
    print()

    number = 1
    phone_book_age = sorted(phone_book, key=lambda x: x["age"])

    for entry in phone_book_age:
        print_entry(number, entry)
        number += 1


@decorator(decorator_off)
def increase_age():
    number_of_years = int(get_input_str(prompt="    Enter number of years: ", allow_digits=True))

    for entry in phone_book:
        entry["age"] += number_of_years

    global unsaved_changes
    unsaved_changes = True


@decorator(decorator_off)
def avr_age_of_all_persons():
    age_of_all_persons = [entry["age"] for entry in phone_book]
    average_age_of_all_persons = sum(age_of_all_persons) / len(age_of_all_persons)

    print(f"Average age of all persons:\n~ {average_age_of_all_persons} years ~")


@decorator(decorator_off)
def save_to_file():
    if file_name is None:
        save_new_file()
    else:
        response = get_input_str(prompt="Save the data to the actual file or create a new one? (actual/new): ",
                                 options=["actual", "new"])

        if response.lower() == "actual":
            save_actual_file()
        elif response.lower() == "new":
            save_new_file()


def open_file(name):
    global file_name
    global phone_book

    try:
        with open(name, 'r') as f:
            phone_book = load(f)

    except FileNotFoundError:
        print_error(f"File '{name}' not found")
    file_name = name


@decorator(decorator_off)
def load_from_file():
    global file_name
    global phone_book
    global unsaved_changes

    if unsaved_changes:
        save_changes()

    file_name = get_input_str(prompt="Enter the name of the file to be opened:\n")
    phone_book = []
    unsaved_changes = False

    try:
        with open(file_name, 'r') as f:
            phone_book = load(f)
        unsaved_changes = False

    except FileNotFoundError:
        print_error(f"File '{file_name}' not found")


@decorator(decorator_off)
def exit_file():
    global running
    global unsaved_changes

    if unsaved_changes:
        save_changes()

    running = False


def main():
    open_file(args.url)
    while running:

        try:
            menu = {
                '1': print_phonebook,
                '2': print_phonebook_by_age,
                '3': add_entry_phonebook,
                '4': find_entry_name_phonebook,
                '5': find_entry_age_phonebook,
                '6': delete_entry_name_phonebook,
                '7': count_all_entries_in_phonebook,
                '8': avr_age_of_all_persons,
                '9': increase_age,
                'e': find_email_by_name,

                '0': exit,
                's': save_to_file,
                'l': load_from_file,
            }

            print_prompt()
            user_input = input("phonebook> ")
            menu[user_input]()

        except Exception as ex:
            print_error("Something went wrong. Try again...")


if __name__ == '__main__':
    main()
