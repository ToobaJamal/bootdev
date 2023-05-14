'''
Finish implementing the empty methods of the Rectangle and Square classes.

Keep in mind that a square is just a rectangle where the length and width are equal. You shouldn't have to duplicate any code between the two classes.
'''

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2 * (self.length + self.width)


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

