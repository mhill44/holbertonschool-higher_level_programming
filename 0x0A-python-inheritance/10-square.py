#!/usr/bin/python3
""" Square class """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ A Square class """
    def __init__(self, size):
        """ Initializes the square """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
    def area(self):
        """ Returns: Returns the area of the square """
        return self.__size ** 2
