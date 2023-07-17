#!/usr/bin/python3
"""Create a class - 'Square'"""


class Square():
    """Implement a class - 'Square'"""
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """Initialise instances of the class"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return (self.width * self.height)

    def PermiterOfMySquare(self):
        """Perimeter of the square"""
        return 2 * (self.width + self.height)

    def __str__(self):
        """String representation of the class"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
