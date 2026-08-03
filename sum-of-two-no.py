"""
Program: Sum of Two Numbers

Input:
    Two integer values.

Output:
    Displays the sum of the two entered numbers.
"""


class SumOfTwoNumbers:
   

    # Class variables
    no_1 = 0
    no_2 = 0

    def input_values(self):
       
        self.no_1 = int(input("Enter First No : "))
        self.no_2 = int(input("Enter Second No : "))

    def sum_of_two_numbers(self):
       
        total = self.no_1 + self.no_2
        print("Sum:", total)


if __name__ == "__main__":
   
    sum_of_numbers = SumOfTwoNumbers()
    sum_of_numbers.input_values()
    sum_of_numbers.sum_of_two_numbers()