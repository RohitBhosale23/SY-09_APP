"""
Program: Demonstration of Magic Methods (__init__ and __del__) in Python
"""

class MagicMethods:


    def __init__(self, *args):
    

        # No-argument constructor
        if len(args) == 0:
            print("List of Magic Methods\n")

            # Display all built-in magic methods of the object class
            for method in dir(object):
                if method.startswith("__") and method.endswith("__"):
                    print(method)

        # Single-argument constructor
        elif len(args) == 1:
            print("Numbers:")
            self.input_start(args[0])

        # Two-argument constructor
        elif len(args) == 2:
            print("Numbers:")
            self.input_start(args[0], args[1])

        # Invalid number of arguments
        else:
            raise TypeError(
                f"MagicMethods() takes 0, 1, or 2 arguments but {len(args)} were given."
            )

    def input_start(self, start=0, end=10):
    

        for no in range(start, end + 1):
            print(no, end=" ")

    def __del__(self):
       
        print("\nDestructor called")


# Driver Code
if __name__ == "__main__":

    # Create an object without arguments
    obj1 = MagicMethods()
    print("\n")

    # Create an object with one argument
    obj2 = MagicMethods(1)
    print("\n")

    # Create an object with two arguments
    obj3 = MagicMethods(9, 10)