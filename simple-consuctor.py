"""
Program: Constructor Demonstration

Input:
    None

Output:
    Displays a message when the object is destroyed.
"""


class SimpleConstructor:
   

    def __init__(self, name):
       
        self.name = name

    def __init__(self):
       
        pass

    def show_name(self):
       
        print("Name:", self.name)

    def run(self):
        
        pass

    def __del__(self):
        
        print("I am deleting class")


if __name__ == "__main__":
   
    simple_constructor = SimpleConstructor()
    simple_constructor.run()