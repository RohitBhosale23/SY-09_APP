# Define a decorator function
def decorator(func):
    # Wrapper function that adds extra functionality
    def wrapper():
        # Code executed before the original function
        print("Before function call")

        # Call the original function
        func()

        # Code executed after the original function
        print("After function call")

    # Return the wrapper function (do not call it here)
    return wrapper


# Apply the decorator to the greet() function
@decorator
def greet():
    """Display a greeting message."""
    print("Hello")


# Call the decorated function
greet()