"""
The get_input_str function can be used to prompt the user for
a string input, and optionally validate it against a list of accepted options.
The get_input_int function can be used to prompt the user for an
integer input and repeatedly ask for input until a valid integer is entered.

The get_input_str function takes in an optional prompt string and an
optional list of options for input validation.
It prompts the user to enter a string input, removes any leading/trailing white
spaces and capitalizes the first letter of the input string.
If options are provided, the function validates the user input by checking
whether it exists in the list of valid options (ignoring case).
If the input is not valid, the function prints an error message and recursively
calls itself with the same prompt and options until a valid input is provided.
If no options are provided and the input string is empty, the function prints
an error message and recursively calls itself with the same prompt and options
until a non-empty input string is provided.
The function returns the validated input string.

The get_input_int function can be used to prompt the user for
an integer input, and repeatedly ask for input until a valid integer is entered.
This function takes in a required prompt string, which is used to prompt the user
to enter an integer input.
The function calls the get_input_str function to get a string input from
the user, and attempts to convert it to an integer using the built-in int() function.
If the conversion fails (ValueError), the function prints an error message and
continues to prompt the user for input until a valid integer is provided.
The function returns the validated integer.
"""


def get_input_str(prompt="", options=None):
    entry_str = input(prompt).strip().capitalize()
    if options is not None:
        if not entry_str or entry_str.lower() not in \
                [option.lower() for option in options]:
            print("Invalid input. Please re-enter")
            entry_str = get_input_str(prompt, options)
    elif not entry_str:
        print("Invalid input. Please re-enter")
        entry_str = get_input_str(prompt, options)

    return entry_str


def get_input_int(prompt):
    while True:
        try:
            value = int(get_input_str(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")
