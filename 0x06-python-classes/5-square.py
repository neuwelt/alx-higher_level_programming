#!/usr/bin/python3
"""Defines the class of a Square."""


class Square:
    """Represents a square."""

    def __init__(new, size):
        """Initializes a new square.
        Args:
            size (int): Size of the new square.
        """
        new.size = size

    @property
    def size(new):
        """Sets the current size of the square."""
        return (new.__size)

    @size.setter
    def size(new, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        new.__size = value

    def area(new):
        """Returns the current area of the square."""
        return (new.__size * new.__size)

    def my_print(new):
        """Print the square with the # character."""
        for a in range(0, new.__size):
            [print("#", end="") for b in range(new.__size)]
            print("")
        if new.__size == 0:
            print("")
