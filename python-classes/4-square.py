#!/usr/bin/python3
"""This module defines a Square class."""


class Square:
    """Defines a square."""

    def __init__(self, size=0):
        self.__size = size

    def area(self):
        return self.__size ** 2
    
    def size(self, value):
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
