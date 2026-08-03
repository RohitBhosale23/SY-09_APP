"""
Program    : Calculate the Area of a Rectangle

Formula:
    Area = Length X Breadth

Input:
    Length of the rectangle
    Breadth of the rectangle

Output:
    Area of the rectangle

Approach:
    1. Accept the length and breadth from the user.
    2. Store the values as instance variables.
    3. Calculate the area using the formula:
           Area = Length X Breadth
    4. Display the calculated area.
"""


class Area:
    

    def __init__(self):
        
        self.length = float(input("Enter length   : "))
        self.breadth = float(input("Enter breadth  : "))

    def calculate_area(self):
        
        area = self.length * self.breadth
        print(f"\nArea of Rectangle = {area}")
        return area


if __name__ == "__main__":
    rectangle = Area()
    rectangle.calculate_area()