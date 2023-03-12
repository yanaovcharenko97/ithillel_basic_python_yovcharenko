def get_input_str(prompt="", options=None, allow_digits=False):
    entry_str = input(prompt).strip().capitalize()
    if options is not None:
        if not entry_str or entry_str not in \
                [option.capitalize() for option in options]:
            print("Invalid input. Please re-enter")
            entry_str = get_input_str(prompt, options)
    elif allow_digits:
        if not entry_str.isdigit():
            print("Invalid input. Please re-enter")
            entry_str = get_input_str(prompt, options, allow_digits)
    elif not entry_str:
        print("Invalid input. Please re-enter")
        entry_str = get_input_str(prompt, options, allow_digits)

    return entry_str
