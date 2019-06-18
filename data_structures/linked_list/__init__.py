from __future__ import annotations

from abc import ABCMeta, abstractmethod
from typing import Any, Optional


class Node(metaclass=ABCMeta):
    """
    The most simple Node class, only contains `value` and `next` properties, and there
    is no any security mechanism for node properties modification

    Any enhanced Node class should inherit this class
    """

    def __init__(self, value: Any, next: Optional[Node] = None):
        """

        :param value:
        :type value: Any
        """
        self.value: Any = value
        self.next: Optional[Node] = next

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
        pass
