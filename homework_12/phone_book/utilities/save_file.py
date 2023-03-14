"""
This module contains functions that enable the user to save changes made to the phone book.

Functions:
save_phonebook_to_new_file(): allows the user to save a new copy of the phone
book in a new file. The user is prompted to enter a file name and confirm the save operation.
save_phonebook_to_actual_file(): overwrites the existing phone book file with
the current version of the phone book. The user is prompted to confirm the save operation.
save_changes_for_phonebook(): this function is called when the user decides to
save the phone book changes.
It calls save_phonebook_to_actual_file() if the user confirms to overwrite the existing file.

Dependencies:
json.dump(): a built-in module to convert the phone book dictionary into a
JSON string and write it to a file.
utilities.input.get_input_str_from_user(): a function to get input string from the user.
__main__.phone_book: a dictionary containing the phone book entries.
__main__.file_name: a string variable containing the name of the file where the phone book is stored.

Note: This module assumes that the phone_book dictionary is already populated with phone book entries.
"""


from json import dump
from utilities.input import get_input_str_from_user
import __main__


def save_phonebook_to_new_file():
    new_file_name = get_input_str_from_user(prompt="Enter the file name:\n")
    response_from_user = get_input_str_from_user(prompt="Are you sure you want to "
                                                        "save the file? (yes/no): ",
                                                 options=["yes", "no"]).lower()
    if response_from_user == "yes":
        with open(new_file_name, "w") as f:
            dump(__main__.phone_book, f)
        print(f"\nPhone book saved to file '{new_file_name}' successfully.")
    elif response_from_user == "no":
        print("\nSave to file operation aborted.")


def save_phonebook_to_actual_file():
    response_from_user = get_input_str_from_user(prompt="Are you sure you want to "
                                                        "overwrite the file? (yes/no): ",
                                                 options=["yes", "no"]).lower()
    if response_from_user == "yes":
        with open(__main__.file_name, "w") as f:
            dump(__main__.phone_book, f)
        print(f"\nPhone book saved to file "
              f"'{__main__.file_name}' successfully.")


def save_changes_for_phonebook():
    response_from_user = get_input_str_from_user(prompt="Save changes to "
                                                        "current file? (yes/no): ",
                                                 options=["yes", "no"]).lower()
    if response_from_user == "yes":
        __main__.save_phonebook_to_file()
