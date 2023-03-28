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

import unittest
from unittest.mock import patch
from io import StringIO
from copy import deepcopy
from json import load, dump
from utilities.input import get_input_str_from_user, get_input_int_from_user
from utilities.print import print_error, print_prompt
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

    @staticmethod
    def print_entry(number, contact):
        """Takes in an integer number and an object of class entry containing
        information about a person
        """
        print("\n--[ %s ]--------------------------" % number)
        print("| Surname: %20s |" % contact.surname)
        print("| Name:    %20s |" % contact.name)
        print("| Age:     %20s |" % contact.age)
        print("| Phone:   %20s |" % contact.phone_number)
        print("| Email:   %20s |" % contact.email)


class Phonebook:
    """
    The Phonebook class describes a Phonebook object with fields and
    methods for working with the contact book
    """

    @staticmethod
    def print_start_end_process():
        """Prints the start and end of the decorated function's
        execution process
        """
        def wrapper(func):
            def called(*args, **kwargs):
                self = args[0]
                if self.verbose:
                    print("Starting to process your request\n")
                result = func(*args, **kwargs)
                if self.verbose:
                    print("\nThe request has been processed")
                return result

            return called

        return wrapper

    def __init__(self,  file_name: str, verbose: bool, phone_book=None,):
        self.verbose = not verbose
        self.file_name = file_name
        self.changes_made_to_phonebook = False
        if phone_book is None:
            self.phone_book = []
        else:
            self.phone_book = phone_book

    @print_start_end_process()
    def add_new_entry_to_phonebook(self):
        surname = get_input_str_from_user(prompt="    Enter surname: ")
        name = get_input_str_from_user(prompt="    Enter name: ")
        age = get_input_int_from_user(prompt="    Enter age: ")
        phone_number = get_input_str_from_user(prompt="    Enter phone num.: ")
        email = get_input_str_from_user(prompt="    Enter email: ")
        self.phone_book.append(Contact(surname, name, age, phone_number, email))
        self.changes_made_to_phonebook = True

    @print_start_end_process()
    def print_phonebook(self):
        print("\n\n#########  Phone book  ##########")

        for idx, contact in enumerate(self.phone_book, start=1):
            contact.print_entry(idx, contact)

    @print_start_end_process()
    def print_phonebook_by_age(self):
        print("\n\n#########  Phone book by age  ##########\n")
        # sorted phone book by age
        phone_book_sorted_by_age = sorted(self.phone_book, key=lambda x: x.age)

        for idx, contact in enumerate(phone_book_sorted_by_age):
            contact.print_entry(idx + 1, contact)

    @print_start_end_process()
    def find_entry_by_name_in_phonebook(self):
        name = get_input_str_from_user(prompt="    Enter name: ")
        found = False

        for idx, contact in enumerate(self.phone_book, start=1):
            if contact.name == name:
                contact.print_entry(idx, contact)
                found = True

        if not found:
            print_error("Contact not found")

    @print_start_end_process()
    def find_entry_by_age_in_phonebook(self):
        age = get_input_int_from_user(prompt="    Enter age: ")
        found = False

        for idx, contact in enumerate(self.phone_book, start=1):
            if contact.age == age:
                contact.print_entry(idx, contact)
                found = True

        if not found:
            print_error("Contact not found")

    @print_start_end_process()
    def find_email_by_name_in_phonebook(self):
        name = get_input_str_from_user(prompt="    Enter name: ")
        found = False

        for idx, contact in enumerate(self.phone_book):
            if contact.name == name:
                print(f"\n{name}'s email:\n   ", contact.email)
                found = True

        if not found:
            print_error("Contact not found")

    @print_start_end_process()
    def update_contact_ages(self):
        years_to_add = get_input_int_from_user(
            prompt="    Enter number of years: ")

        for idx, contact in enumerate(self.phone_book):
            # add the age to the entry in the phone book
            contact.age += years_to_add

    @print_start_end_process()
    def delete_entry_by_name_in_phonebook(self):
        name = get_input_str_from_user(prompt="    Enter name: ")
        # create a copy of the phonebook to be able to change it
        copy_of_phone_book = deepcopy(self.phone_book)
        found = False

        for idx, contact in enumerate(copy_of_phone_book):
            if contact.name == name:
                self.phone_book.pop(idx)
                found = True

        if not found:
            print_error("Contact not found")
    # indicates that there were changes in the phone book
        self.changes_made_to_phonebook = True

    @print_start_end_process()
    def count_all_entries_in_phonebook(self):
        print("Total number of entries: ", len(self.phone_book))

    @print_start_end_process()
    def calculate_average_age_of_all_persons_in_phonebook(self):
        try:
            # get a list of all ages in the phonebook
            age_of_all_persons_in_phonebook = \
                [contact.age for contact in self.phone_book]
            average_age_of_all_persons = \
                sum(age_of_all_persons_in_phonebook) / len(
                    age_of_all_persons_in_phonebook)

            print("Average age of all persons:\n"
                  f"~ {average_age_of_all_persons:.2f} years ~")

        except ZeroDivisionError:
            # handle the case where the phonebook is empty
            print_error("Division by zero. The phone book is empty.")

    def save_phonebook_to_new_file(self):
        new_file_name = get_input_str_from_user(
            prompt="Enter the file name:\n")
        response_from_user = get_input_str_from_user(
            prompt="Are you sure you want to "
                   "save the file? (yes/no): ",
            options=["yes", "no"]).lower()
        data = []
        for contact in self.phone_book:
            data.append({"surname": contact.surname, "name": contact.name,
                         "age": contact.age,
                         "phone_number": contact.phone_number,
                         "email": contact.email})
        if response_from_user == "yes":
            with open(new_file_name, "w") as f:
                dump(data, f)
            print(
                f"\nPhone book saved to file '{new_file_name}' successfully.")
        elif response_from_user == "no":
            print("\nSave to file operation aborted.")

    def save_phonebook_to_actual_file(self):
        response_from_user = get_input_str_from_user(
            prompt="Are you sure you want to "
                   "overwrite the file? (yes/no): ",
            options=["yes", "no"]).lower()
        data = []
        for contact in self.phone_book:
            data.append({"surname": contact.surname, "name": contact.name,
                         "age": contact.age,
                         "phone_number": contact.phone_number,
                         "email": contact.email})
        if response_from_user == "yes":
            with open(self.file_name, "w") as f:
                dump(data, f)
            print(f"\nPhone book saved to file "
                  f"'{self.file_name}' successfully.")

    def save_changes_for_phonebook(self):
        response_from_user = get_input_str_from_user(
            prompt="Save changes to current file? (yes/no): ",
            options=["yes", "no"]).lower()
        if response_from_user == "yes":
            self.save_phonebook_to_file()

    @print_start_end_process()
    def save_phonebook_to_file(self):
        if self.file_name is None:
            # if there is no file name, save to a new file
            self.save_phonebook_to_new_file()
        else:
            # ask the user whether to save to the current file or a new one
            response = get_input_str_from_user(
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
        if self.changes_made_to_phonebook:
            # save changes to the file
            self.save_changes_for_phonebook()

        file_name = get_input_str_from_user(prompt="Enter the name of the "
                                                   "file to be opened:\n")
        self.phone_book = []
        # reset the flag for tracking changes
        self.changes_made_to_phonebook = False

        try:
            with open(file_name, "r") as f:
                phone_book_load = load(f)
                # reset the flag for tracking changes
            self.changes_made_to_phonebook = False
            for line in phone_book_load:
                self.phone_book.append(Contact(line["surname"],
                                               line["name"],
                                               line["age"],
                                               line["phone_number"],
                                               line["email"]))

        except FileNotFoundError:
            print_error("File not found")

    def open_file(self):
        try:
            with open(self.file_name, "r") as f:
                phone_book_load = load(f)
                # reset the flag for tracking changes
            self.changes_made_to_phonebook = False
            for line in phone_book_load:
                self.phone_book.append(Contact(line["surname"],
                                               line["name"],
                                               line["age"],
                                               line["phone_number"],
                                               line["email"]))

        except FileNotFoundError:
            print_error("File not found")


class Menu:
    """
    The Menu class describes the fields and methods for working with
    the Phonebook class and provides a user interface.
    """

    def __init__(self, file_name, verbose):
        self.running = True
        self.file_name = file_name
        self.verbose = verbose
        self.phonebook = Phonebook(self.file_name, self.verbose)
        self.phonebook.open_file()
        self.open_menu()

    def exit_file(self):
        if self.phonebook.changes_made_to_phonebook:
            self.phonebook.save_changes_for_phonebook()

        # set running to False, which will cause the main loop to exit
        self.running = False

    def open_menu(self):

        while self.running:  # continue running until user chooses to exit

            try:
                menu = {
                    # create a dictionary of menu options mapped to functions
                    "1": self.phonebook.print_phonebook,
                    "2": self.phonebook.print_phonebook_by_age,
                    "3": self.phonebook.add_new_entry_to_phonebook,
                    "4": self.phonebook.find_entry_by_name_in_phonebook,
                    "5": self.phonebook.find_entry_by_age_in_phonebook,
                    "6": self.phonebook.delete_entry_by_name_in_phonebook,
                    "7": self.phonebook.count_all_entries_in_phonebook,
                    "8": self.phonebook.calculate_average_age_of_all_persons_in_phonebook,
                    "9": self.phonebook.update_contact_ages,
                    "e": self.phonebook.find_email_by_name_in_phonebook,

                    "0": self.exit_file,  # map '0' to exit_file() function
                    "s": self.phonebook.save_phonebook_to_file,
                    "l": self.phonebook.load_phonebook_from_file,
                }

                print_prompt()  # print the command prompt
                user_input = get_input_str_from_user(prompt="phonebook> ")
                # call the function mapped to the user's input
                menu[user_input.lower()]()

            except KeyError:
                print_error("Please enter a valid option from the menu.")


class TestPhonebook(unittest.TestCase):
    def setUp(self):
        self.phonebook = Phonebook(file_name="test_phonebook.json",
                                   verbose=True)

    def tearDown(self):
        self.phonebook = None

    def test_print_phonebook(self):
        # Add some test data to the phone book
        test_contact_1 = Contact(
            "Doe", "John", 30, "+1234567890", "johndoe@example.com")
        test_contact_2 = Contact(
            "Smith", "Jane", 25, "+0987654321", "janesmith@example.com")
        self.phonebook.phone_book = [test_contact_1, test_contact_2]

        # Redirect stdout to a buffer, so we can capture the output
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.phonebook.print_phonebook()
            expected_output = "\n\n#########  Phone book  ##########\n"
            expected_output += "1: John Doe, 30 years old\n"
            expected_output += "2: Jane Smith, 25 years old\n"
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_calculate_average_age_of_all_persons_in_phonebook(self):
        expected_output = "Average age of all persons:\n~ 27.50 years ~\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.phonebook.calculate_average_age_of_all_persons_in_phonebook()
            self.assertEqual(fake_out.getvalue(), expected_output)

        # Test case for empty phonebook
        self.phonebook.phone_book = []
        expected_output = "Error: Division by zero. The phone book is empty.\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.phonebook.calculate_average_age_of_all_persons_in_phonebook()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_count_all_entries_in_phonebook(self):
        expected_output = "Total number of entries:  2\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.phonebook.count_all_entries_in_phonebook()
            self.assertEqual(fake_out.getvalue(), expected_output)

        # Test case for empty phonebook
        self.phonebook.phone_book = []
        expected_output = "Total number of entries:  0\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.phonebook.count_all_entries_in_phonebook()
            self.assertEqual(fake_out.getvalue(), expected_output)


def main():
    parser = argparse.ArgumentParser(description="Phone book")
    parser.add_argument("url", type=str, help="The path to the file")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="Enable decorators")
    args = parser.parse_args()
    print(args.verbose)
    Menu(args.url, args.verbose)


if __name__ == "__main__":
    main()
