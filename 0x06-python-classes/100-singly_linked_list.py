#!/usr/bin/python3
""" Defining Node and SinglyLinkedList classes """


class Node:
    """ Node class """

    def __init__(self, data, next_node=None):
        """
        intitialize a Node instance

        Args:
            data (int): data to store in the node
            next_node (Node): next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ get the data in the node """
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ get the next node """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ SinglyLinkedList class """

    def __init__(self):
        """
        initialize a SinglyLinkedList instance
        """
        self.__head = None

    def __str__(self):
        """
        print representation of SinglyLinkedList class
        """
        ptr = self.__head
        s = ""
        while ptr is not None and ptr.next_node is not None:
            s += "{:d}\n".format(ptr.data)
            ptr = ptr.next_node
        s += "{}".format("" if ptr is None else ptr.data)
        return s

    def sorted_insert(self, value):
        """
        insert a new Node into the correct position in the list
        (increasing order)
        """
        if type(value) is not int:
            raise TypeError("value must be an integer")

        new = Node(value)
        ptr = self.__head
        if ptr is None or ptr.data >= value:
            new.next_node = ptr
            self.__head = new
            return
        while (ptr is not None
                and ptr.next_node is not None
                and new.data > ptr.next_node.data):
            ptr = ptr.next_node
        new.next_node = ptr.next_node
        ptr.next_node = new
