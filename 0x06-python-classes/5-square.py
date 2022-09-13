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
        self.__size = size

    @property
    def size(self):
        """getter of size"""
        return self.__size

    @size.setter
    def size(self, user_input):
        """setter of size"""
        if type(user_input) != int:
            raise TypeError("size must be an integer")
        elif user_input < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = user_input

    def area(self):
        """returns the area of square"""
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            row = self.__size * "#"
            for i in range(self.__size):
                print(row)
