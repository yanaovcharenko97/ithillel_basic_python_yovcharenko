def print_start_end_process(print_start_end_process_off):
    def wrapper(func):
        def called(*args, **kwargs):
            result = func(*args, **kwargs)
            if print_start_end_process_off is True:
                print("Starting to process your request")
                func()
                print("The request has been processed")
            return result
        return called
    return wrapper
