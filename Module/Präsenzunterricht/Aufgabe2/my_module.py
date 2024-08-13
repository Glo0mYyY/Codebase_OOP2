class Shape:
    def __init__(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
    def display_info(self):
        print("This is a Circle with a area of " + str(self.area()))
    
class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2
    
    def display_info(self):
        print("This is a Square with a area of " + str(self.area()))
