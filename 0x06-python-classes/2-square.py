#!/usr/bin/python3
""" Square module """


class Square:
    """ A class that defines a square

    Attributes:
        size (obj,'int'): size of the square
    """

    def __init__(self, size=0) -> None:
        """ Initializes square class

        Args:
            size (obj:'int') size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        """ Only positive integers allowed for attribute size

        """
        else:
            self.__size = size
        """ Set private attribute of square size to var size

        """
