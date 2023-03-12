def print_start_end_process(print_start_end_process_off):
    def wrapper(func):
        def called():
            if print_start_end_process_off is True:
                print("Starting to process your request")
                func()
                print("The request has been processed")
            else:
                func()
        return called
    return wrapper
