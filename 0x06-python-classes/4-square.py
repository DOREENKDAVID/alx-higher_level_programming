#!/usr/bin/python3
""" Square module """


class Square:

    """Define a Square class

     Attributes:
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

    @size.setter
    def size(self, value):
        """ Define size of square object to change to value

        Args:
            size (obj:'int') size of the square
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        """
        Attribute value assumes only positive integers
        """

    else:
        self.__size = value

    def area(self):
        """
        Define and compute the area of square object
        """
        return self.__size ** 2
