#!/usr/bin/python3
""" Square module """


class Square:

    """Define a Square class """

    def __init__(self, size=0) -> None:
        """
        Intializes the attributes

        Args:
            size: size of square
        """
        self.size = size

    @property
    def size(self):
        """ Gets the attribute to be used in square class """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Calculate area of a square """
        return self.__size ** 2
