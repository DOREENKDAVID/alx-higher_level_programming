#!/usr/bin/python3
"""
4-inherits_from Module
"""


def inherits_from(obj, a_class):
    """
   To check if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class
        Args:
            obj: initial object
            a_class: class
            Returns: True if the object is an instance of a
                     class that inherited from class else False
    """
    if type(obj) is not a_class and isinstance(obj, a_class):
        return True
    return False
