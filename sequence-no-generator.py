"""
Program: Generate Numbers from 1 to 100 Without Using
         Loops, if-else Statements, Iterators, or Repeated Statements

"""

class NumberGenerator:
    

    # Class (static) variable shared among all objects.
    NO = 1

    def __init__(self):
       
        print(NumberGenerator.NO, end=" ")
        NumberGenerator.NO += 1

    def __del__(self):
        pass


if __name__ == "__main__":

    # Create 100 objects using list comprehension.
    # Each object creation invokes the constructor,
    # printing numbers from 1 to 100.
    objects = [NumberGenerator() for _ in range(100)]