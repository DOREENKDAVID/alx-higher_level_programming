#!/usr/bin/python3
""" Square module """


class Square:

    """Define a Square class """

    def __init__(self, size=0) -> None:
        """ Initialize square class
        Args:
        (obj:'int') size of square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        """
        Attribute size assumes only positive integers
        """
        else:
            self.__size = size
        """
        Set size as a private attribute of square to var size
        """

    def area(self):
        """
        Define and compute the area of square object
        """
        return self.__size ** 2
