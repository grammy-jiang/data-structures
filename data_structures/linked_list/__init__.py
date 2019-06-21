"""
This module contains the following linked lists:

 * Singly Linked List
 * Doubly Linked List
"""
from __future__ import annotations

from abc import ABCMeta, abstractmethod
from collections.abc import Collection, Reversible
from typing import Any, Optional


class Node(metaclass=ABCMeta):  # pylint: disable=too-few-public-methods
    """
    The most simple Node class, only contains `value` and `next` properties, and there
    is no any security mechanism for node properties modification

    Any enhanced Node class should inherit this class
    """

    def __init__(self, value: Any, next_: Optional[Node] = None):
        """

        :param value:
        :type value: Any
        :param next_:
        :type next_: Optional[Node]
        """
        self.value: Any = value
        self.next: Optional[Node] = next_

    @classmethod
    @abstractmethod
    def after_node(cls, value: Any, node: Node) -> Node:
        """
        Create a node with the given value, and after the given node

        :param value: The value that the node contains
        :type value: Any
        :param node: The node which `next` points to this node
        :type node: Node
        :return: The node created
        :rtype: Node
        """


class LinkedList(Collection, Reversible, metaclass=ABCMeta):
    """
    The abstract class of Linked List
    """

    def __init__(self, *args):
        """

        :param args:
        """
        self.head: Optional[Node] = None
        self._init(*args)

    @abstractmethod
    def _init(self, *args) -> None:
        """
        Initial this linked list with the given arguments

        :param args:
        :return:
        :rtype: None
        """

    def __bool__(self) -> bool:
        """
        if this linked list is empty return False, otherwise return True
        :return:
        :rtype: bool
        """
        return self.head is not None

    def __contains__(self, item) -> bool:
        """
        Check if the given item exists in this linked list

        :param item:
        :return:
        :rtype: bool
        """
        for node in self:
            if item is node:
                return True

        return False

    @abstractmethod
    def __iter__(self):
        """
        Return an iterator of this linked list
        :return:
        """

    def __len__(self) -> int:
        """
        Return the length of this linked list

        :return:
        :rtype: int
        """
        length = 0
        for _ in self:
            length += 1
        return length

    @abstractmethod
    def __reversed__(self):
        """
        Return an reversed iterator of this linked list

        :return:
        """

    @property
    def tail(self) -> Optional[Node]:
        """
        The tail node of this singly linked list

        :return:
        :rtype: Optional[Node}
        """
        node: Optional[Node] = None

        for node in self:
            pass

        return node
