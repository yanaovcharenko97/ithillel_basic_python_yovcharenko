def get_input_str_from_user(prompt="", options=None):
    entry_str = input(prompt).strip().capitalize()
    if options is not None:
        if not entry_str or entry_str.lower() not in \
                [option.lower() for option in options]:
            print("Invalid input. Please re-enter")
            entry_str = get_input_str_from_user(prompt, options)
    elif not entry_str:
        print("Invalid input. Please re-enter")
        entry_str = get_input_str_from_user(prompt, options)

    return entry_str


def get_input_int_from_user(prompt):
    while True:
        try:
            value = int(get_input_str_from_user(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")
