"""
This module contains the following linked lists:

 * Singly Linked List
 * Doubly Linked List
"""
from __future__ import annotations

from abc import ABCMeta, abstractmethod
from collections.abc import Collection
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


class LinkedList(Collection, metaclass=ABCMeta):
    def __init__(self, *args):
        self.head: Optional[Node] = None
        self._init(*args)

    @abstractmethod
    def _init(self, *args) -> None:
        """

        :param args:
        :return:
        :rtype: None
        """

    @abstractmethod
    def __contains__(self, item) -> bool:
        """

        :param item:
        :return:
        :rtype: bool
        """

    @abstractmethod
    def __iter__(self):
        """

        :return:
        """

    @abstractmethod
    def __len__(self) -> int:
        """

        :return:
        :rtype: int
        """
