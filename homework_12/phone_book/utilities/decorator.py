"""
A decorator function that prints the start and end of the decorated function's execution process.

Args:
print_start_end_process_off (bool): A boolean flag to turn off/on the print statements. If True, the print
statements will be turned off.

Returns:
wrapper (function): A function that wraps the decorated function.

Example usage:
    @print_start_end_process(True)
    def my_function():
        # function logic here
"""


def print_start_end_process(print_start_end_process_off):
    def wrapper(func):
        def called(*args, **kwargs):
            if print_start_end_process_off:
                print("Starting to process your request\n")
            result = func(*args, **kwargs)
            if print_start_end_process_off:
                print("\nThe request has been processed")
            return result
        return called
    return wrapper
