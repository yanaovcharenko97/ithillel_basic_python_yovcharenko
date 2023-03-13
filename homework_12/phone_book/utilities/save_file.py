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
