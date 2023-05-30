#!/usr/bin/python3
""" Square module """


class Square:

    """Define a Square class

    Attributes:
        (size,'int'): size of square
        (area,'int'): area of square
    """
    def __init__(self, size=0, position=(0, 0)):
        """ Initialize square class

        Args:
        size (obj:'int') size of square
        """
        self.size = size
        self.position = position
        """
        Set private attribute of square size to var size
        Set private attribute of square position to var position

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
        if value < 0:
            raise ValueError("size must be >= 0")
        """
        Attribute value assumes only positive integers
        """

        self.__size = value

    @property
    def position(self):
        """
        define the position os square object
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Define position of value and set to a\
                tuple of 2 positive integers.
        """
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple\
                    of 2 positive integers")
        elif type(value[0]) is not int or value[0] < 0:
            raise TypeError("position must be a tuple\
                    of 2 positive integers")
        elif type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple\
                    of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Define and compute the area of square object
        """
        return self.__size ** 2

    def my_print(self):
        """
         prints in stdout the square with the character #:
        """
        if self.size == 0:
            print()
            return
        for i in range(self.position[1]):
            print()
        for i in range(self.size):
            print((" " * self.position[0]) + ('#' * self.size))
        return
