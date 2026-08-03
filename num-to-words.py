"""
Program: Convert Number to Words

Input:
    A numeric string (e.g., 123)

Output:
    The corresponding words for each digit.
    Example:
        Input : 123
        Output: One Two Three
"""

# List containing the word representation of digits.
digit_words = [
    "Zero", "One", "Two", "Three", "Four",
    "Five", "Six", "Seven", "Eight", "Nine"
]

# Read the number from the user.
number = input("Enter a number: ")

# Display the data type of the input.
print(type(number))

# Convert each digit into its corresponding word.
for digit in number:
    print(digit_words[int(digit)], end=" ")