def calculate(operation, first, second, make_int=False, message=None):
    """
    If `make_int` is True, it should truncate this result to an integer 
    (otherwise, you can return the natural result of the ops).
     """
    if operation == 'add':
        result = first + second
    elif operation == 'subtract':
        result = first - second
    elif operation == 'multiply':
        result = first * second
    elif operation == 'divide':
        result = first / second
    else:
        raise ValueError("Invalid Operation")
        # return ("operations could only be:'add', 'subtract', 'multiply', or 'divide'")

    if message is None:
        message = 'The result is'

    if make_int: 
        result = int(result)

    return f"{message} {result}"