"""
This script is a phone book that allows adding, deleting, updating contacts,
and searching them by name, age, and email. It is possible to save the contact
list to a file or open an existing file with phone contacts.

How to run
The program can be run from the command line by navigating to the
directory containing the script
and typing the following command:
python phonebook.py <file_name> [-v]
where file_name is the name of the file to be used for storing contacts.
The -v argument is
optional and can be used to enable the display of process start and end
messages.
"""

from copy import deepcopy
from json import load, dump
from utilities.input import get_input_str, get_input_int
from utilities.print import print_error, print_prompt
from utilities.decorator import verbose_start_and_end
import argparse


class Contact:
    """Represents a contact in the phone book"""

    def __init__(self, surname, name, age, phone_number, email):
        """Create a new contact with given attributes"""
        self.surname = surname
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.email = email

    def print_entry(self, number, contact):
        """Displays information about a contact"""
        print("\n--[ %s ]--------------------------" % number)
        print("| Surname: %20s |" % contact.surname)
        print("| Name:    %20s |" % contact.name)
        print("| Age:     %20s |" % contact.age)
        print("| Phone:   %20s |" % contact.phone_number)
        print("| Email:   %20s |" % contact.email)

    def to_dict(self, contact):
        data = {}
        data["surname"] = contact.surname,
        data["name"] = contact.name,
        data["age"] = contact.age,
        data["phone_number"] = contact.phone_number,
        data["email"] = contact.email

        return data

    @staticmethod
    def to_object(line):
        obj = Contact(line["surname"], line["name"], line["age"],
                      line["phone_number"], line["email"])

        return obj


class Phonebook:
    """Describes the Phonebook object with contact book methods"""

    def __init__(self,  file_name: str, verbose: bool):
        self.verbose = verbose
        self.file_name = file_name
        self.changes_made = False
        self.phone_book = []
        self.__open_file()

    @verbose_start_and_end
    def add_new_entry(self):
        surname = get_input_str(prompt="    Enter surname: ")
        name = get_input_str(prompt="    Enter name: ")
        age = get_input_int(prompt="    Enter age: ")
        phone_number = get_input_str(prompt="    Enter phone num.: ")
        email = get_input_str(prompt="    Enter email: ")
        self.phone_book.append(Contact(surname, name, age, phone_number, email))
        self.changes_made = True

    @verbose_start_and_end
    def print_phonebook(self):
        print("\n\n#########  Phone book  ##########")

        for idx, contact in enumerate(self.phone_book, start=1):
            contact.print_entry(idx, contact)

    @verbose_start_and_end
    def print_phonebook_by_age(self):
        print("\n\n#########  Phone book by age  ##########\n")
        # sorted phone book by age
        phone_book_sorted_by_age = sorted(self.phone_book, key=lambda x: x.age)

        for idx, contact in enumerate(phone_book_sorted_by_age):
            contact.print_entry(idx + 1, contact)

    @verbose_start_and_end
    def find_entry_by_name(self):
        name = get_input_str(prompt="    Enter name: ")
        found = False

        for idx, contact in enumerate(self.phone_book, start=1):
            if contact.name == name:
                contact.print_entry(idx, contact)
                found = True

        if not found:
            print_error("Contact not found")

    @verbose_start_and_end
    def find_entry_by_age(self):
        age = get_input_int(prompt="    Enter age: ")
        found = False

        for idx, contact in enumerate(self.phone_book, start=1):
            if contact.age == age:
                contact.print_entry(idx, contact)
                found = True

        if not found:
            print_error("Contact not found")

    @verbose_start_and_end
    def find_email_by_name(self):
        name = get_input_str(prompt="    Enter name: ")
        found = False

        for idx, contact in enumerate(self.phone_book):
            if contact.name == name:
                print(f"\n{name}'s email:\n   ", contact.email)
                found = True

        if not found:
            print_error("Contact not found")

    @verbose_start_and_end
    def update_contact_ages(self):
        years_to_add = get_input_int(
            prompt="    Enter number of years: ")

        for idx, contact in enumerate(self.phone_book):
            # add the age to the entry in the phone book
            contact.age += years_to_add

        self.changes_made = True

    @verbose_start_and_end
    def delete_entry_by_name(self):
        name = get_input_str(prompt="    Enter name: ")
        # create a copy of the phonebook to be able to change it
        copy_of_phone_book = deepcopy(self.phone_book)
        found = False

        for idx, contact in enumerate(copy_of_phone_book):
            if contact.name == name:
                self.phone_book.pop(idx)
                found = True
                self.changes_made = True

        if not found:
            print_error("Contact not found")
    # indicates that there were changes in the phone book

    @verbose_start_and_end
    def count_all_entries(self):
        print("Total number of entries: ", len(self.phone_book))

    @verbose_start_and_end
    def average_age(self):
        try:
            # get a list of all ages in the phonebook
            age_of_all_persons = [contact.age for contact in self.phone_book]
            len_all_person = len(age_of_all_persons)
            sum_age = sum(age_of_all_persons)
            average_age_of_all_persons = sum_age / len_all_person

            print("Average age of all persons:\n"
                  f"~ {average_age_of_all_persons:.2f} years ~")

        except ZeroDivisionError:
            # handle the case where the phonebook is empty
            print_error("Division by zero. The phone book is empty.")

    def serialize(self):
        data = []

        for contact in self.phone_book:
            data.append(contact.to_dict(contact))

        return data

    def __write_to_file(self, file_name):
        data = self.serialize()

        with open(file_name, "w") as f:
            dump(data, f)

        print(f"\nPhone book saved to file "
              f"'{file_name}' successfully.")

    def save_phonebook_to_new_file(self):
        new_file_name = get_input_str(
            prompt="Enter the file name:\n")
        response_from_user = get_input_str(
            prompt="Are you sure you want to "
                   "save the file? (yes/no): ",
            options=["yes", "no"]).lower()

        if response_from_user == "yes":
            self.__write_to_file(new_file_name)

    def save_phonebook_to_actual_file(self):
        response_from_user = get_input_str(
            prompt="Are you sure you want to "
                   "overwrite the file? (yes/no): ",
            options=["yes", "no"]).lower()

        if response_from_user == "yes":
            self.__write_to_file(self.file_name)

    def save_changes(self):
        response_from_user = get_input_str(
            prompt="Save changes to current file? (yes/no): ",
            options=["yes", "no"]).lower()

        if response_from_user == "yes":
            self.save_phonebook_to_file()

    @verbose_start_and_end
    def save_phonebook_to_file(self):
        # ask the user whether to save to the current file or a new one
        response = get_input_str(
            prompt="Save the data to the actual file or "
                   "create a new one? (actual/new): ",
            options=["actual",
                     "new"])

        if response.lower() == "actual":
            self.save_phonebook_to_actual_file()
        elif response.lower() == "new":
            self.save_phonebook_to_new_file()

    def load_phonebook_from_file(self):
        # check if there are unsaved changes in the phone book
        if self.changes_made:
            # save changes to the file
            self.save_changes()

        self.file_name = get_input_str(prompt="Enter the name of the "
                                              "file to be opened:\n")
        self.phone_book = []
        # reset the flag for tracking changes
        self.changes_made = False

        self.__open_file()

    def __open_file(self):
        try:
            with open(self.file_name, "r") as f:
                phone_book_load = load(f)

            # reset the flag for tracking changes
            self.changes_made = False
            for line in phone_book_load:
                self.phone_book.append(Contact.to_object(line))

        except FileNotFoundError:
            print_error("File not found")


class Menu:
    """Describes methods for working with the Phonebook class and provides a user interface"""

    def __init__(self, file_name, verbose):
        self.running = True
        self.file_name = file_name
        self.verbose = verbose
        self.phonebook = Phonebook(self.file_name, self.verbose)
        self.open_menu()

    def exit_file(self):
        if self.phonebook.changes_made:
            self.phonebook.save_changes()

        # set running to False, which will cause the main loop to exit
        self.running = False

    def open_menu(self):
        while self.running:  # continue running until user chooses to exit

            try:
                menu = {
                    # create a dictionary of menu options mapped to functions
                    "1": self.phonebook.print_phonebook,
                    "2": self.phonebook.print_phonebook_by_age,
                    "3": self.phonebook.add_new_entry,
                    "4": self.phonebook.find_entry_by_name,
                    "5": self.phonebook.find_entry_by_age,
                    "6": self.phonebook.delete_entry_by_name,
                    "7": self.phonebook.count_all_entries,
                    "8": self.phonebook.average_age,
                    "9": self.phonebook.update_contact_ages,
                    "e": self.phonebook.find_email_by_name,

                    "0": self.exit_file,  # map '0' to exit_file() function
                    "s": self.phonebook.save_phonebook_to_file,
                    "l": self.phonebook.load_phonebook_from_file,
                }

                print_prompt()  # print the command prompt
                user_input = get_input_str(prompt="phonebook> ")
                # call the function mapped to the user's input
                menu[user_input.lower()]()

            except KeyError:
                print_error("Please enter a valid option from the menu.")


def main():
    parser = argparse.ArgumentParser(description="Phone book")
    parser.add_argument("url", type=str, help="The path to the file")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="Enabling verbose mode: each action will be "
                             "wrapped with statement about action start and end")
    args = parser.parse_args()
    print(args.verbose)
    Menu(args.url, args.verbose)


if __name__ == "__main__":
    main()
