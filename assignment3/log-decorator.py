import logging
from functools import wraps

# One time setup
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
# Use 'a' to append to the log file
handler = logging.FileHandler("./decorator.log", "a")
logger.addHandler(handler)

def logger_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Format positional parameters
        pos_params = list(args) if args else "none"
        # Format keyword parameters
        key_params = kwargs if kwargs else "none"
        
        # Execute the function
        result = func(*args, **kwargs)
        
        # Log the details
        logger.log(logging.INFO, f"function: {func.__name__}")
        logger.log(logging.INFO, f"positional parameters: {pos_params}")
        logger.log(logging.INFO, f"keyword parameters: {key_params}")
        logger.log(logging.INFO, f"return: {result}")
        
        return result
    return wrapper

# Task 1.1: No parameters, returns nothing
@logger_decorator
def say_hello():
    print("Hello, World!")

# Task 1.2: Variable positional arguments, returns True
@logger_decorator
def check_args(*args):
    return True

# Task 1.3: Variable keyword arguments, returns logger_decorator
@logger_decorator
def return_decorator(**kwargs):
    return "logger_decorator"

# Mainline code
if __name__ == "__main__":
    say_hello()
    check_args(1, "apple", 3.14)
    return_decorator(user="admin", status="active")