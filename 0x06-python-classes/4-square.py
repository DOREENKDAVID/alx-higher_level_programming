#!/usr/bin/python3

class Square:

    """Define a Square class """

    """ Attributes:
        (size,'int'): size of square
        (area,'int'): area of square
    """
    def __init__(self, size=0):
        """ Initialize square class

        Args:
        size (obj:'int') size of square
        """
        self.__size = size
        """
        Set private attribute of square size to var size

        """

    @property
    def size(self):
        """
        define size attribute of square object
        """
        return self.__size

    def area(self):
        """
        Define and compute the area of square object
        """
        return self.__size ** 2

    @size.setter
    def size(self, value):
        """ Define size of square object to change to value

        Args:
            size (obj:'int') size of the square
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        """
        Attribute value assumes only positive integers
        """

        self.__size = value
