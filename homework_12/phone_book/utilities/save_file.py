from json import dump
from utilities.input import get_input_str
import __main__


def save_new_file():
    new_file_name = get_input_str(prompt="Enter the file name:\n")
    response = get_input_str(prompt="Are you sure you want to save the file? (yes/no): ", options=["yes", "no"])
    if response.lower() == "yes":
        with open(new_file_name, 'w') as f:
            dump(__main__.phone_book, f)
        print(f"\nPhone book saved to file '{new_file_name}' successfully.")
    elif response.lower() == 'no':
        print("\nSave to file operation aborted.")


def save_actual_file():
    response = get_input_str(prompt="Are you sure you want to overwrite the file? (yes/no): ",
                             options=["yes", "no"])
    if response.lower() == "yes":
        with open(__main__.file_name, 'w') as f:
            dump(__main__.phone_book, f)
        print(f"\nPhone book saved to file '{__main__.file_name}' successfully.")


def save_changes():
    response = get_input_str(prompt="Save changes to current file? (yes/no): ", options=["yes", "no"])
    if response.lower() == "yes":
        __main__.save_to_file()
