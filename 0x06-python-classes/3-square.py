#!/usr/bin/python3

class Square:

    """Define a Square class """

    """ Attributes:
        (size,'int'): size of square
    """
    def __init__(self, size=0):
        """ Initialize square class
        Args:
        (obj:'int') size of square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        """
        Attribute size assumes only positive integers
        """

        self.__size = size
        """
        Set size as a private attribute of square to var size
        """

    def area(self):
        """
        Define and compute the area of square object
        """
        return self.__size ** 2
