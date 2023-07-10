#!/usr/bin/python3
""" square class """
Rectangle = __import__(9-rectangle.py).Rectangle

class Square(Rectangle):
    """ square class inherits from the rectangle class """
    def __init__(self, size):
        """ init """
        self.integer_validator("size",size)
        self.__size = size
        super().__init__(size, size)
