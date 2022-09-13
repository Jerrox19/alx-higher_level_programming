#!/usr/bin/python3
""" contains file 2-square.py
    defines the class square
"""


class Square:
    """ a class Square that defines a square
        Args:
            __size (int) - size of square
            __position (int, int) - postion
    """
    def __init__(self, size=0, position=(0, 0)):
        """Instantiation with optional size"""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """getter of positon"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter of positon"""
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or value([0]) < 0:
            raise TypeError("osition must be a tuple of 2 positive integers")
        if type(value[1]) != int or value([1]) < 0:
            raise TypeError("osition must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            row = self.__size * "#"
            if self.__positon[0] == 0:
                for i in range(self.__size):
                    print(row)
            else:
                position = " " * self.__position[0]
                for i in range(self.__size):
                    print(position)
                    print(row)
