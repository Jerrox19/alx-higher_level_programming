#!/usr/bin/python3
""" contains file 2-square.py
    defines the class square
"""


class Square:
    """ a ckass Square that defines a square
        Args:
            __size (int) - size of square
    """
    def __init__(self, size=0):
        """Instantiation with optional size"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
