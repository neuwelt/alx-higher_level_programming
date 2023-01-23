#!/usr/bin/python3
"""Defines the class of a Square."""


class Square:
    """Represents a square."""

    def __init__(new, size=0):
        """Initializes a new square.
        Args:
            size (int): Size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        new.__size = size

    def area(new):
        """Return the current area of the square."""
        return (new.__size * new.__size)
