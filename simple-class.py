"""
Program: Name Input and Display

Input:
    Name (string)

Output:
    Displays the entered name.
"""


class Simple:
    

    # Class variable
    var_input = ""

    def input_name(self):
        
        self.var_input = input("Enter the Name: ")

    def show_name(self):
        
        print("Name:", self.var_input)


if __name__ == "__main__":
    
    simple = Simple()
    simple.input_name()
    simple.show_name()