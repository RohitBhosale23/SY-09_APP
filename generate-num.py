"""
Program: Sequence Number Generator

Input:
    Starting number (integer)

Output:
    Displays the sequence of numbers from the starting number to 100.
"""

class SequenceGenerator:
    """
    A class to generate and display a sequence of numbers.
    """

    def no_generator(self, start=0):
        """
        Generate and display numbers from the given starting number to 100.

        Args:
            start (int, optional): The starting number of the sequence.
                Defaults to 0.

        Returns:
            None
        """
        for number in range(start, 101):
            print(number, end=" ")

    def input_start(self):
        """
        Accept the starting number from the user and generate the sequence.

        Prompts the user to enter an integer and displays numbers from
        the entered value up to 100.

        Returns:
            None
        """
        start_no = int(input("Enter Start No: "))
        self.no_generator(start=start_no)


if __name__ == "__main__":
    """
    Program execution starts here.
    """
    sequence_generator = SequenceGenerator()
    sequence_generator.input_start()