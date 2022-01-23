#!/usr/bin/python3


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class "square"
    """
    def __init__(self, size):
        """
        The constructor
        """
        if self.integer_validator("size", size):
            self.__size = size
            super().__init__(size, size)
    def area(self):
        """
        The area
        """
        return self.__size ** 2
    def __str__(self):
        """
        The string
        """
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
