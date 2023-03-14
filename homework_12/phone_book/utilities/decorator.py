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
