"""
Program: Convert Number to Words Using a Dictionary

Input:
    A numeric string (e.g., 123)

Output:
    The corresponding words for each digit.
    Example:
        Input : 123
        Output: One Two Three
"""

# Dictionary containing the word representation of digits.
digit_words = {
    0: "Zero",
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
}

# Read the number from the user.
number = input("Enter a number: ")

# Display the data type of the dictionary.
print(type(digit_words))

# Convert each digit into its corresponding word.
for digit in number:
    print(digit_words[int(digit)], end=" ")