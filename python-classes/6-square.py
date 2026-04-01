#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """Defines a square."""

    def __init__(self, position = (0, 0), size=0):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size
    
    @property
    def position(self):
        return self.__position
    
    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value
    
    def position(self, value):
        if not isinstance(value, int):
            raise TypeError("position must be a tuple of 2 positive integers")
        
        self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
