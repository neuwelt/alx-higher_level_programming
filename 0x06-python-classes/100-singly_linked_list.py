#!/usr/bin/python3
"""Defines the classes for a singly-linked list."""


class Node:
    """Represents a node in a singly-linked list."""

    def __init__(new, data, next_node=None):
        """Initializes a new Node.
        Args:
            data (int): The data of the new Node.
            next_node (Node): The next node of the new Node.
        """
        new.data = data
        new.next_node = next_node

    @property
    def data(new):
        """Sets the data of the Node."""
        return (new.__data)

    @data.setter
    def data(new, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        new.__data = value

    @property
    def next_node(new):
        """Get/set the next_node of the Node."""
        return (new.__next_node)

    @next_node.setter
    def next_node(new, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        new.__next_node = value


class SinglyLinkedList:
    """Represents a singly-linked list."""

    def __init__(new):
        """Initialize a new SinglyLinkedList."""
        new.__head = None

    def sorted_insert(new, value):
        """Insert a new Node to the SinglyLinkedList.
        The node is inserted into the list at the correct
        ordered numerical position.
        Args:
            value (Node): The new Node to insert.
        """
        net = Node(value)
        if new.__head is None:
            net.next_node = None
            new.__head = net
        elif new.__head.data > value:
            net.next_node = new.__head
            new.__head = net
        else:
            tmp = new.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            net.next_node = tmp.next_node
            tmp.next_node = net

    def __str__(new):
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        tmp = new.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
