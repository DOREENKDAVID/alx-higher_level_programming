#!/usr/bin/python3
""" Rectangle module """


class Rectangle:

    """
    Declare a rectangle class
    """
    def __init__(self, width=0, height=0):
        """initialize class by setting attributes
        height and width
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        getter for the private instance attribute width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the private instance attribute width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        getter for the private instance attribute height
        """
        return self._height

    @height.setter
    def height(self, value):
        """
        Setter for the private instance attribute height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value