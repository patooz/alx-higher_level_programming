#!/usr/bin/python3
""" singly list classes """


class Node:
    """ this is the node in a singly list """
    def __init__(self, data, next_node=None):
        """ starting the node """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ takes data to the node """
        return (self.__data)

    @dat.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ sets the next node """
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ class for singly list """
    def __init__(self):
        """ initializes a singly list """
        self.__head = None

    def sorted_insert(self, value):
        """ inserts a new node to the singly list """
        brand = Node(value)
        if self.__head is None:
            brand.next_node = None
            self.__head = brand
        elif self.__head.data > value:
            brand.next_node = self.__head
            self.__head = brand
        else:
            tmp = self.__head
            while (tmp.next_node is not None and tmp.next_node.data < value):
                tmp = tmp.next_node
            brand.next_node = tmp.next_node
            tmp.next_node = brand

        def __str__(self):
            """ prints the singly linked list """
            values = []
            tmp = self.__head
            while tmp is not None:
                values.append(str(tmp.data))
                tmp = tmp.next_node
            return ('\n'.join(values))
