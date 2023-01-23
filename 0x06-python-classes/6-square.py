#!/usr/bin/python3
"""Defines the class of a Square."""


class Square:
    """Represents a square."""

    def __init__(new, size=0, position=(0, 0)):
        """Initializes a new square.
        Args:
            size (int): Size of the new square.
            position (int, int): The position of the new square.
        """
        new.size = size
        new.position = position

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

    @property
    def position(new):
        """Sets the current position of the square."""
        return (new.__position)

    @position.setter
    def position(new, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        new.__position = value

    def area(new):
        """Returns the current area of the square."""
        return (new.__size * new.__size)

    def my_print(new):
        """Prints the square with the # character."""
        if new.__size == 0:
            print("")
            return

        [print("") for a in range(0, new.__position[1])]
        for i in range(0, new.__size):
            [print(" ", end="") for b in range(0, new.__position[0])]
            [print("#", end="") for c in range(0, new.__size)]
            print("")
